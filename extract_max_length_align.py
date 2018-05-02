#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:07:21 2018

@author: gyang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  21 21:58:29 2018

@author: gyang
"""

import os,sys,re,getopt
import pandas as pd

usage = '''
Usage: python extract_max_length_align.py <Required> [Options]   

Extract the longest transcript for blastn result. Default column index based on format 6.

  -i   Input coordinate file.
  -g   Index of groupby column.(Default:2) 
  -l   Index of alignment length.(Default:4)
  -o   Name of output file.

Ex: python extract_max_length_align.py -i cpc_cnci_gencode.nt.self -o cpc_cnci_gencode.nt.longest    
'''
if (len(sys.argv) < 3 or re.match("^-", sys.argv[1]) is None): sys.exit(usage)
options,args = getopt.getopt(sys.argv[1:],"hi:g:l:o:",["help"]) 
###Take care of the index! minus one!
group = 1
length = 3
 
for name,value in options:
    if name in ("-h","--help"):
        usage()
    elif name in ("-i"):
        fi = value
    elif name in ("-o"):
        fo = value
    elif name in ("-g"):
        group = int(value) -1
    elif name in ("-l"):
        length = int(value) -1
print("length",length)
print("group",group)

#fi = pd.read_table("cpc_cnci_gencode.nt.self",header = None,sep = "\t")
fi = pd.read_table(fi,header = None,sep = "\t")
temp = fi.groupby(group).apply(lambda t: t[t.iloc[:,length] == t.iloc[:,length].max()])
temp.to_csv(fo,index=False,sep='\t',header=False)