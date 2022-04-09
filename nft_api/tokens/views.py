from rest_framework.response import Response
from rest_framework.decorators import api_view
from web3 import Web3
from .models import NFT
from .serializers import NFTSerializer

from json import loads
from os import getenv
from string import ascii_uppercase, ascii_lowercase, digits
from random import choice
from dotenv import load_dotenv

load_dotenv()

INFURA_ENDPOINT = getenv("API_URL")
PRIVATE_KEY = getenv("PRIVATE_KEY")
CHAIN_ID = int(getenv("CHAIN_ID"))

w3 = Web3(Web3.HTTPProvider(INFURA_ENDPOINT))
CONTRACT_ADDRESS = getenv("CONTRACT_ADDRESS")
CONTRACT_ABI = loads(str(getenv("CONTRACT_ABI")))
CONTRACT = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)


def create_nft(owner, genereated_hash, media_url):
    try:
        nonce = w3.eth.get_transaction_count(owner)

        mint_txn = CONTRACT.functions.mint(owner, genereated_hash, media_url).buildTransaction(
            {
                "chainId": CHAIN_ID,
                "gas": 7000000,
                "gasPrice": w3.toWei("3", "gwei"),
                "nonce": nonce,
            }
        )

        signed_txn = w3.eth.account.sign_transaction(
            mint_txn, private_key=PRIVATE_KEY)
        w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_hash = w3.toHex(w3.keccak(signed_txn.rawTransaction))
        return tx_hash
    except Exception as ex:
        print(f'Some problems with create_nft: {ex}')
        return None



def unique_hash_generator(size=20, chars=ascii_uppercase + ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size))


@api_view(['GET'])
def getNFTS(request):
    if request.method == 'GET':
        nfts = NFT.objects.all().order_by('id')
        serializer_class = NFTSerializer(nfts, many=True)
        return Response(serializer_class.data)


@api_view(['GET'])
def getTotalSupply(request):
    if request.method == 'GET':
        totalSupply = CONTRACT.functions.totalSupply().call()
        data = {"total_supply": f"{w3.fromWei(totalSupply, 'ether')}"}
        return Response(data)


@api_view(['POST'])
def mintNFT(request):
    if request.method == 'POST':
        req_dat = request.data
        unique_hash = unique_hash_generator()
        data = {}

        try:
            tx_hash = create_nft(
                req_dat['owner'], unique_hash, req_dat['media_url'])
            if tx_hash is None:
                return Response('Problems with create_nft...')
            data['unique_hash'] = unique_hash
            data['tx_hash'] = tx_hash
            data['media_url'] = req_dat['media_url']
            data['owner'] = req_dat['owner']
        except Exception as ex:
            print(f'Some problems with mintNFT: {ex}')
            return Response(ex)

        serializer = NFTSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data)
        else:
            return Response(serializer.errors)
