from web3 import Web3
import json

HARDHAT_URL = r"http://127.0.0.1:8545/"
DECIMALS = 6

w3 = Web3(Web3.HTTPProvider(HARDHAT_URL))

path_to_token_contract_json = r'hardhat/artifacts/contracts/TokenContract.sol/TokenContract.json'
token_contract_address = '0x3D23571FcdEd14560C052066Ca18A53A7723801F'

path_to_nft_contract_json = r'hardhat/artifacts/contracts/NftContract.sol/NftContract.json'
nft_contract_address = '0xcF77ed72438925d7C319cdd57C4CE8AA56BCdAF8'

with open(path_to_token_contract_json) as file:
    token_contract_json = json.load(file)

with open(path_to_nft_contract_json) as file:
    nft_contract_json = json.load(file)


token_contract_abi = token_contract_json.get('abi')
nft_contract_abi = nft_contract_json.get('abi')


def create_ref_code(symbol, public_key, year):
    return f'{symbol} - {public_key[2:6]}{year}'


def get_contract():
    return w3.eth.contract(address=token_contract_address, abi=token_contract_abi)


def get_checksum_address(public_key):
    return w3.to_checksum_address(public_key)


def get_token_balance(contract, checksum_address):
    return contract.functions.balanceOf(checksum_address).call() / 10 ** DECIMALS


def get_token_symbol(contract):
    return contract.functions.symbol().call()


def get_owner():
    return w3.eth.accounts[0].lower()
