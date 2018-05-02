#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:08:11 2018

@author: gyang
"""
import os,sys,re,getopt

def usage():
    usage = '''
    Usage: python bed12_to_gtf.py <Required> [Options]   

    Transfer bed12 file to gtf file. 

      -b   Input bed12 file.
      -o   Name of output gtf file.

    Ex: python bed12_to_gtf.py -b test.bed12 -o test.gtf     
'''
    sys.exit(usage)

def main():
    if (len(sys.argv) < 5  or re.match("^-", sys.argv[1]) is None): 
        usage()
    options,args = getopt.getopt(sys.argv[1:],"hi:b:o:",["help"])   
    for name,value in options:
        if name in ("-h","--help"):
            usage()
        elif name in ("-b"):
            bed = value
        elif name in ("-o"):
            fo = value
    parse_bed_file(bed,fo)
#bed12:
#chr1	3073252	3074322	ENSMUST00000193812.1	0	+	3074322	3074322	0	1	1070,	0,
#gtf:
#chr1	HAVANA	exon	3073253	3074322	.	+	.	gene_id "ENSMUSG00000102693.1"; transcript_id "ENSMUST00000193812.1"; gene_type "TEC"; gene_name "RP23-271O17.1"; transcript_type "TEC"; transcript_name "RP23-271O17.1-001"; exon_number 1; exon_id "ENSMUSE00001343744.1"; level 2; transcript_support_level "NA"; tag "basic"; havana_gene "OTTMUSG00000049935.1"; havana_transcript "OTTMUST00000127109.1";
   
def parse_bed_file(bed,fo):
    with open(bed,'r') as bed:
        with open(fo,'w') as gtf: 
            while True:
                bed_tran = bed.readline().strip()
                if len(bed_tran) == 0:
                    break
                bed_tran = bed_tran.split('\t')
                bed_chr = bed_tran[0]
                bed_start = int(bed_tran[1])
                #bed_end = int(bed_tran[2])
                bed_id = bed_tran[3]
                #bed_score = bed_tran[4]
                bed_strand = bed_tran[5]
                bed_count = int(bed_tran[9])
                bed_exon_start = [ int(i) for i in bed_tran[11].split(',')[:-1]]
                bed_exon_size = [ int(i) for i in bed_tran[11].split(',')[:-1]]
                
                for i in range(bed_count):
                    gtf.write(bed_chr + "\tgyang\texon\t" + str(bed_exon_start[i] + bed_start + 1 ) + "\t" + 
                             str(bed_exon_start[i] + bed_start + bed_exon_size[i]) + '\t.\t' + str(bed_strand) + 
                             '\t.\ttranscript_id "' +  bed_id + '";\n')

                
if __name__ == "__main__":
    main()               

