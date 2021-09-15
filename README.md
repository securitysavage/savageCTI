## Prerequisites

1. Linux fundamentals
2. Docker
3. Python 3+
4. ```gunzip```

## Instructions for Shodan Scripts

1. Run ```$ python3 shodan-ip-download.py /path/to/foo.txt bar.json.gz``` and wait for the Shodan to process the list.
2. Run ```$ gunzip bar.json.gz``` to decompress the generated archive.
3. Run ```$ python3 shodan-parse.py -o foobar.txt -v bar.json``` to produce list ```foobar.txt``` of format ```IP:PORT:ORG:HOSTNAMES``` (see output example file).

## Docker Setup (optional)

1. Edit the Dockerfile and add your Shodan/Greynoise API keys to it.
2. Run ```$ docker build -t <YOUR TAG HERE> .``` and Docker will provision your container.
3. Create a local directory, for example ```$ mkdir /home/<YOUR USERNAME>/sharedir``` for sharing files with the savageCTI container.
4. Use ```$ docker run -v /home/<YOUR USERNAME>/sharedir:/storage -it <YOUR TAG HERE> /bin/bash``` to access a root shell in your new container. Verify successful installation from your container prompt with ```# shodan version``` and ```# greynoise version```. The Shodan scripts from this repo are pulled via ```wget``` to the container's ```/scripts``` directory.

## Notes

Shodan CLI module install guide [here](https://help.shodan.io/command-line-interface/0-installation) and CLI documentation [here](https://cli.shodan.io/).

Greynoise CLI module install guide [here](https://developer.greynoise.io/docs/libraries-sample-code) and CLI documentation [here](https://greynoise.readthedocs.io/en/latest/).

EmailRep CLI module install guide [here](https://pypi.org/project/emailrep/) and CLI documentation [here](https://docs.emailrep.io/).

You must sign up for a Shodan/Greynoise account to get an API key. EmailRep's key must be requested with a "known safe" email address.

CentOS Dockerfile included for variety.

Tested on Ubuntu 18.04, CentOS 8, MacOS Catalina, Windows 10.

Twitter: [@securitysavage](https://twitter.com/securitysavage)
