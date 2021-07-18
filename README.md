## Prerequisites

1. Python 3+
2. ```gunzip```
2. The Shodan CLI module, initialized with your API key. Install guide [here](https://help.shodan.io/command-line-interface/0-installation) and CLI documentation [here](https://cli.shodan.io/).

## Instructions for Shodan Scripts

1. Place your IP list (one per line) in your savageCTI directory.
2. Run ```python3 shodan-ip-download.py iplist.txt filename.json.gz``` and wait for the API to process the list.
3. Run ```gunzip filename.json.gz``` to decompress the generated archive.
4. Run ```python3 shodan-parse.py -o outputname.txt -v filename.json``` to produce the list ```outputname.txt``` in the format IP:PORT:ORG:HOSTNAMES (see example files).

## Docker Setup

1. Place the Dockerfile in an empty folder and add your Shodan/Greynoise API keys to it.
2. Run ```docker volume create savagecti-data```.
3. Run ```docker build -t <YOUR TAG HERE> .``` and Docker will set up your environment.
3. When it completes, use ```docker run -it <YOUR TAG HERE> /bin/bash``` to access a root shell in your new container. Verify successful installation with ```shodan version``` and ```greynoise version```.
4. 

## Notes

You must sign up for a Shodan/Greynoise account to get an API key.

Twitter: [@securitysavage](https://twitter.com/securitysavage)