#!/usr/bin/python

from parser import Parser
from sys import argv

#only care about the first argument.
if(None == argv[1]):
    print("No input file specified.")
    exit(255)

file = argv[1]

parser = Parser(file)
parser.test()

