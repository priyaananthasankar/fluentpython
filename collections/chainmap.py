import argparse
import os
from collections import ChainMap

##
# Useful to mix and reconcile a bunch of dictionaries/maps in priority
##

def main():
    defaults = {"username": "admin", "password": "test"}
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--username')
    parser.add_argument('-p','--password')

    args = parser.parse_args()

    # Dictionary comprehension
    command_line_args = {key:value for key,value 
                          in vars(args).items() if value}

    #  chain maps in order. Command line, environment variables and defaults
    chain =  ChainMap(command_line_args,os.environ, defaults)
    print(chain['username'])

if __name__ == "__main__":
    main()
    os.environ['username'] = 'test'
    main()
    