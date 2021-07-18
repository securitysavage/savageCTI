## Prerequisites

1. Linux fundamentals
1. Python 3+
2. ```gunzip```
3. The Shodan CLI module, initialized with your API key. Install guide [here](https://help.shodan.io/command-line-interface/0-installation) and CLI documentation [here](https://cli.shodan.io/).
4. The Greynoise CLI module, initialized with your API key. Install guide [here](https://developer.greynoise.io/docs/libraries-sample-code) and CLI documentation [here](https://greynoise.readthedocs.io/en/latest/).

## Instructions for Shodan Scripts

1. Run ```$ python3 shodan-ip-download.py /path/to/foo.txt bar.json.gz``` and wait for the API to process the list.
3. Run ```$ gunzip bar.json.gz``` to decompress the generated archive.
4. Run ```$ python3 shodan-parse.py -o foobar.txt -v bar.json``` to produce list ```foobar.txt``` of format ```IP:PORT:ORG:HOSTNAMES``` (see output example file).

## Docker Setup (optional)

1. Edit the Dockerfile and add your Shodan/Greynoise API keys to it.
2. Run ```$ docker build -t <YOUR TAG HERE> .``` and Docker will provision your container.
3. Create a local directory, for example ```$ mkdir /home/<YOUR USERNAME>/sharedir``` for sharing files such as IP lists with savageCTI.
4. Use ```$ docker run -v /home/<YOUR USERNAME>/sharedir:/storage -it <YOUR TAG HERE> /bin/bash``` to access a root shell in your new container. Verify successful installation from your container prompt with ```# shodan version``` and ```# greynoise version```. The Shodan scripts from this repo are pulled via ```wget``` to the container's ```/scripts``` directory.

Usage: ```[root@container:/storage]# python3 /scripts/shodan-ip-download.py foo.txt bar.json.gz``` with ```foo.txt``` being an IP list from your local machine, such as a SIEM export.

## Notes

You must sign up for a Shodan/Greynoise account to get an API key.

Twitter: [@securitysavage](https://twitter.com/securitysavage)