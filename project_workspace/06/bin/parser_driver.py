#!/usr/bin/python2.6

from assembler import Assembler
from sys import argv

#only care about the first argument.
if(None == argv[1]):
    print("No input file specified.")
    exit(255)

file = argv[1]
assembler = Assembler(file)

assembler.two_pass_assembly()
