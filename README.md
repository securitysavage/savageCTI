## Prerequisites

1. Python 3+
2. ```gunzip```
3. The Shodan CLI module, initialized with your API key. Install guide [here](https://help.shodan.io/command-line-interface/0-installation) and CLI documentation [here](https://cli.shodan.io/).
4. The Greynoise CLI module, initialized with your API key. Install guide [here](https://developer.greynoise.io/docs/libraries-sample-code) and documentation [here](https://greynoise.readthedocs.io/en/latest/)

## Instructions for Shodan Scripts

1. Place your IP list (one address per line) in your savageCTI directory.
2. Run ```python3 shodan-ip-download.py iplist.txt filename.json.gz``` and wait for the API to process the list.
3. Run ```gunzip filename.json.gz``` to decompress the generated archive.
4. Run ```python3 shodan-parse.py -o outputname.txt -v filename.json``` to produce the list ```outputname.txt``` in the format ```IP:PORT:ORG:HOSTNAMES``` (see output example file).

## Docker Setup!

1. Edit the Dockerfile and add your Shodan/Greynoise API keys to it.
2. Run ```docker build -t <YOUR TAG HERE> .``` and Docker will set up your container.
3. Create a local directory, for example ```mkdir /home/<YOUR USERNAME>/sharedir``` for sharing files such as IP lists with savageCTI.
4. Use ```docker run -v /home/<YOUR USERNAME>/sharedir:/storage -it <YOUR TAG HERE> /bin/bash``` to access a root shell in your new container. Verify successful installation with ```shodan version``` and ```greynoise version```.

## Notes

You must sign up for a Shodan/Greynoise account to get an API key.
To use external files such as IP lists with the container, place them in the local share directory you established with your ```docker run``` command.

Twitter: [@securitysavage](https://twitter.com/securitysavage)