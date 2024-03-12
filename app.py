# Created by Sazhod at 16.02.2024
import datetime
from tokenize import tokenize

from flask import Flask, render_template, request, redirect, session, url_for
from utils import *

app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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

        contract = get_contract()
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

    return render_template('marketplace.html', is_owner=is_owner)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
