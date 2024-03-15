# Created by Sazhod at 16.02.2024
import datetime
from tokenize import tokenize

from flask import Flask, render_template, request, redirect, session, url_for
from utils import *
from flask import send_from_directory


app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
nft_directory = r'NFT/NFTS/'
images_directory = r'NFT/images/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET' and request.args.get('public_key'):
        session['public_key'] = request.args.get('public_key')
        return redirect(url_for('profile'))

    if request.method == 'POST':
        session.pop('public_key')

    return render_template('index.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        session.pop('public_key')
        return redirect(url_for('index'))

    if 'public_key' in session:
        public_key = session['public_key']

        contract = get_token_contract()
        checksum_address = get_checksum_address(public_key)
        token_balance = get_token_balance(contract, checksum_address)
        token_symbol = get_token_symbol(contract)
        ref_code = create_ref_code(token_symbol, public_key, 2023)

        return render_template('profile.html', public_key=public_key,
                               token_balance=token_balance, token_symbol=token_symbol, ref_code=ref_code)
    return render_template('index.html')


@app.route('/marketplace', methods=['GET', 'POST'])
def marketplace():
    is_owner = False
    if 'public_key' in session and session['public_key'] == get_owner():
        is_owner = True

        if request.method == 'POST' and 'image' in request.files and 'title' in request.values and \
                'description' in request.values and 'cost' in request.values and 'count' in request.values:
            # print(request.json)
            nft_id = uuid.uuid4().int
            title = request.values.get('title')
            description = request.values.get('description')
            image_path = save_image(request.files.get('image'))
            print(image_path, nft_id)
            cost = int(request.values.get('cost'))
            count = int(request.values.get('count'))
            data = create_json_data_for_nft(title, description, image_path, cost, nft_id)
            metadata = '{"id": ' + str(nft_id) + '}'
            contract = get_nft_contract()
            create_nft(contract, get_checksum_address(get_owner()), nft_id, count, metadata.encode('utf-8'))

            # token_contract = get_token_contract()
            # from_address = get_checksum_address(get_owner())
            # to_address = get_checksum_address(w3.eth.accounts[1])
            # print(from_address)
            # print(to_address)
            # print(token_contract.functions.transfer(to_address, 100000).transact({'from': from_address,
            #                                                          'gas': 899000, 'gasPrice': 1000000000}))

    return render_template('marketplace.html', is_owner=is_owner)


@app.route('/NFT/NFTS/<path:path>')
def get_json(path):
    return send_from_directory(nft_directory, path)


@app.route('/NFT/images/<path:path>')
def get_image(path):
    return send_from_directory(images_directory, path)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
