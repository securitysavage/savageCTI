#!/usr/bin/env/python3
#
# Adapted from https://gist.github.com/jivoi/3905537780a38d53c8e6add152d0d61a, a fork of 
#
# https://gist.github.com/achillean/f4bce0971b132f35d104a728d8d797f1
#
# This script uses the Shodan API to generate json data from a list of IPs.

from shodan import Shodan
from shodan.helpers import open_file, write_banner
from shodan.cli.helpers import get_api_key
from sys import argv, exit

# Input validation
if len(argv) != 3:
    print('Usage: {} <IP filename> <output.json.gz>'.format(argv[0]))
    print('Example: {} grizzly-ips.txt shodan-grizzly.json.gz'.format(argv[0]))
    exit(1)

input_filename = argv[1]
output_filename = argv[2]

# Must run shodan init from CLI before running this script
key = get_api_key()

# Create API connection
api = Shodan(key)

# Create output file
fout = open_file(output_filename, 'w')

# Open the file containing the list of IPs
with open(input_filename, 'r') as fin:
    # Loop over all IPs in file
    for line in fin:
        ip = line.strip() # Remove whitespace/newlines

        # Wrap API calls to skip IPs with no data
        try:
            print('Processing: {}'.format(ip))
            info = api.host(ip)

            # All banner stored in 'data' property
            for banner in info['data']:
                write_banner(fout, banner)
        except:
            pass # No data
