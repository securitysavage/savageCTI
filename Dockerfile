FROM debian
ENV PATH="/root/.local/bin:${PATH}"
RUN apt update && apt install python3 python3-pip wget -y
RUN pip3 install greynoise --upgrade
RUN pip3 install -U --user shodan
RUN greynoise setup -k <YOUR API KEY HERE>
RUN shodan init <YOUR API KEY HERE>
RUN mkdir /storage && mkdir /scripts
RUN cd /scripts && wget https://raw.githubusercontent.com/securitysavage/savageCTI/main/shodan-ip-download.py && wget https://raw.githubusercontent.com/securitysavage/savageCTI/main/shodan-parse.py