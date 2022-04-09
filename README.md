# NFT API
## Description:

*This is my test assignment for the company!*

A Django back-end service that interacts with an ERC-721 standard contract in the Ethereum blockchain and allows operations with an NFT token using the REST API.

## Technology stack:
- Language: `Python 3.10.0`
- Web framework: `Django 4.0.3 & DRF 3.13.11`
- Database: `SQLite3` 
- Blockchain framework: `Web3.py`
- Blockchain: `Ethereum (Rinkeby Testnet)`

## Docker and Docker-Compose:

If you want to run my project in docker container, you will need to install it first, all information about it you can find on ***https://hub.docker.com***

After that clone repository and go to the directory project:

    git clone https://github.com/miht-sem/nft-api.git

    cd nft-api

Then use this command in termial to build it in container:

    docker-compose build

And this to run app on `localhost:8000` in your web browser:
    
    docker-compose up 


### Existing virtualenv:

First, if your project is already in an existing python virtualenv clone the repository and go to the directory project:

    git clone https://github.com/miht-sem/nft-api.git

    cd nft-api

Second, install django by running

    pip install django
      
### No virtualenv:

First clone the repository from Github and switch to the new directory:

    git clone https://github.com/miht-sem/nft-api.git

    cd nft-api


I recommend to use `virtualenv` for development:

- Start by installing `virtualenv` if you don't have it

        pip install virtualenv


- Create a virtual environment

        virtualenv venv


- Enable the virtual environment

        source venv/bin/activate



## Getting Started:

Install project dependencies:

    pip install -r requirements/local.txt
    
Then you need to open the `.env` file and replace all the variable values with your own. 

After that simply apply the migrations:

    python manage.py migrate --run-syncdb
    

You can now run the development server:

    python manage.py runserver

## What you can do:

    /tokens/create 

- Request method: POST

This API  create a new unique token in the blockchain and record the request parameters in the database.

The request accept:
- media_url - url with some media
- owner - Ethereum-the address of the future owner of the token

```
/tokens/list
```
- Request method: GET

This API output a list of all objects of the Token

```
/tokens/total_supply
```
- Request method: GET

This API access the contract in the blockchain and provide information in the response about the current Total supply of the token - the total number of tokens in the network. The response form is arbitrary, in JSON format.

## NFT Token Smart Contract for Integration:
- Network: `Ethereum Rinkeby Testnet`
- Blockchain Explorer of the network: ***https://rinkeby.etherscan.io/***
- Smart contract page: ***https://rinkeby.etherscan.io/address/0x92e098def0ca9577bd50ca61b90b9a46ec1f2040***