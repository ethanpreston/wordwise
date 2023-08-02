#!/usr/bin/env python3

import argparse
from definitions import *
from synonyms import *

# Set up parser for the command line interface
parser = argparse.ArgumentParser(description="Dictionary and Thesaurus all from your Command Line!")
parser.add_argument('-d', '--define', default="", help='Specify the word you would like to define')
parser.add_argument('-s', '--synonyms', default="", help='Specify the word you would like to find synonyms for')
parser.add_argument('-a', '--all', default=False, action="store_true")
args = parser.parse_args()

if args.define:
    define_word(args.define)
elif args.synonyms:
    get_synonyms(args.synonyms, args.all)
else:
    print("Please provide a valid command to the application")
