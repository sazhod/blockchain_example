# Created by Sazhod at 16.02.2024
import datetime

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

contract_address = '0x8A791620dd6260079BF849Dc5567aDC3F2FdC318'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET' and request.args.get('public_key'):
        session['public_key'] = request.args.get('public_key')
        return redirect(url_for('index'))

    if request.method == 'POST':
        session.pop('public_key')

    token_balance = ''
    token_symbol = ''

    if 'public_key' in session:
        public_key = session['public_key']

        contract = get_contract()
        checksum_address = get_checksum_address(public_key)
        token_balance = get_token_balance(contract, checksum_address)
        token_symbol = get_token_symbol(contract)

        # balance = w3.eth.get_balance(Web3.to_checksum_address(public_key))

    return render_template('index.html', token_balance=token_balance, token_symbol=token_symbol)


@app.route('/profile')
def profile():
    return render_template('profile.html')


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
