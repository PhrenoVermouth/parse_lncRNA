#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 09:08:11 2018

@author: gyang
"""
import os,sys,re,getopt

usage = '''
Usage: python fill_header_for_fasta.py <Required> [Options]   

Fill full header for fasta files. 

  -b   Input bed file.
  -f   Input fasta file.
  -o   Name of output fasta file.

Ex: python fill_header_for_fasta.py -f test.fa -i test.bed12 -o test.fa     
'''

if (len(sys.argv) < 7  or re.match("^-", sys.argv[1]) is None): sys.exit(usage)


options,args = getopt.getopt(sys.argv[1:],"hi:f:b:o:",["help"])   
for name,value in options:
    if name in ("-h","--help"):
        usage()
    elif name in ("-b"):
        bed = value
    elif name in ("-f"):
        fa = value
    elif name in ("-o"):
        fo = value

fo = open(fo,'w')

with open(fa,'r') as fa:
    with open(bed,'r') as bed: 
        while True:
            header_old = fa.readline().strip()
            seq = fa.readline().strip()
            header_new = bed.readline().strip()
            if len(header_old) == 0 :
                break
            fo.write('>')           
            fo.write(header_new)
            fo.write('\n')
            fo.write(seq)
            fo.write('\n')
fo.close()            
