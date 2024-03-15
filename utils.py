from web3 import Web3
import json
import uuid

HARDHAT_URL = r"http://127.0.0.1:8545/"
DECIMALS = 6

BASE_URL = r'http://127.0.0.1:5000/'

w3 = Web3(Web3.HTTPProvider(HARDHAT_URL))

path_to_token_contract_json = r'hardhat/artifacts/contracts/TokenContract.sol/TokenContract.json'
token_contract_address = '0xb409013acE408Bf661E232Fc181297371f45F633'

path_to_nft_contract_json = r'hardhat/artifacts/contracts/NftContract.sol/NftContract.json'
nft_contract_address = '0xd5A48FAc93B8fec2A1c2aD81608e3681F5F0a3a6'

with open(path_to_token_contract_json) as file:
    token_contract_json = json.load(file)

with open(path_to_nft_contract_json) as file:
    nft_contract_json = json.load(file)


token_contract_abi = token_contract_json.get('abi')
nft_contract_abi = nft_contract_json.get('abi')


def create_ref_code(symbol, public_key, year):
    return f'{symbol} - {public_key[2:6]}{year}'


def get_token_contract():
    return w3.eth.contract(address=token_contract_address, abi=token_contract_abi)


def get_nft_contract():
    return w3.eth.contract(address=nft_contract_address, abi=nft_contract_abi)


def get_checksum_address(public_key):
    return w3.to_checksum_address(public_key)


def get_token_balance(contract, checksum_address):
    return contract.functions.balanceOf(checksum_address).call() / 10 ** DECIMALS


def get_token_symbol(contract):
    return contract.functions.symbol().call()


def get_owner():
    return w3.eth.accounts[0].lower()


def create_nft(contract, to, nft_id, amount, metadata):

    result = contract.functions.createNft(to, nft_id, amount, metadata).transact({
        'gas': 899000,
        'gasPrice': 1000000000
    })


def create_json_data_for_nft(title, description, image, cost, nft_id):
    data = {
        'title': title,
        'description': description,
        'image': image,
        'cost':  cost
    }
    with open(f'NFT/NFTS/{nft_id}.json', 'w') as file:
        json.dump(data, file)
    return json.dumps(data)


def save_image(image):
    path = f'NFT/images/{image.filename}'
    image.save(path)
    return BASE_URL + path


def save_metadata():
    pass
