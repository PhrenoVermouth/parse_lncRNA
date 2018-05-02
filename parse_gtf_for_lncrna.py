#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:59:17 2018

@author: gyang
"""
import os,sys,re,getopt

usage = '''
Usage: python parse_gtf_for_lncrna.py <Required> [Options]   

  -i   Input coordinate file.
  -f   Threhold for minimum FPKM. 
  -n   Threhold for minimum exon number.
  -l   Threhold for total exon length in one transcript, eg:200.
  -o   Name of output file.

Ex: python parse_gtf_for_lncrna.py -i transcripts.gtf -f 0.1 -n 2 -l 200 -o new.gtf     
'''
if (len(sys.argv) < 11 or re.match("^-", sys.argv[1]) is None): sys.exit(usage)


options,args = getopt.getopt(sys.argv[1:],"hi:f:n:o:l:",["help"])   
for name,value in options:
    if name in ("-h","--help"):
        usage()
    elif name in ("-i"):
        fi = value
    elif name in ("-o"):
        fo = value
    elif name in ("-f"):
        fpkm_min = float(value)
    elif name in ("-n"):
        num_min = float(value)
    elif name in ("-l"):
        len_min = float(value)


fo = open(fo,'w')
with open(fi,'r') as fi:
    line = fi.readline().strip()
    temp = [line]
    exon = []
    while True: 
        line = fi.readline().strip() 
        if len(line) == 0:
            break             
        list = line.split()
        #### Within or next transcript?
        if line.split()[2] == 'exon':
            exon.append(abs(float(line.split()[4]) - float(line.split()[5])))
            temp.append(line)
            start = line.find('FPKM "') + 6
            end = line.find('"; frac')
            fpkm = float(line[start:end])
        else: # if next transcript is read
            if len(exon) >= num_min and fpkm >= fpkm_min and sum(exon) >= len_min:
                for i in temp:
                    fo.write('\n')
                    fo.write(i)
            temp = [line]
            exon = []
fo.close()            
   

                
                
                
                
                
            
        
        
        
        
        
        
    


        
