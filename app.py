# Created by Sazhod at 16.02.2024
import datetime
from tokenize import tokenize

from flask import Flask, render_template, request, redirect, session, url_for
from web3 import Web3
import json


app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

HARDHAT_URL = r"http://127.0.0.1:8545/"

w3 = Web3(Web3.HTTPProvider(HARDHAT_URL))

with open('abi.json') as file:
    abi = json.load(file)

contract_address = '0xb409013acE408Bf661E232Fc181297371f45F633'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET' and request.args.get('public_key'):
        session['public_key'] = request.args.get('public_key')
        return redirect(url_for('index'))

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


def create_ref_code(symbol, public_key, year):
    return f'{symbol} - {public_key[2:6]}{year}'


def get_contract():
    return w3.eth.contract(address=contract_address, abi=abi)


def get_checksum_address(public_key):
    return w3.to_checksum_address(public_key)


def get_token_balance(contract, checksum_address):
    return contract.functions.balanceOf(checksum_address).call()


def get_token_symbol(contract):
    return contract.functions.symbol().call()


def main():
    app.run()


if __name__ == '__main__':
    main()
