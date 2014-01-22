import re
import urllib
from Bio import SeqIO

myFilename = "/Users/siakhnin/Downloads/rosalind_mprt (2).txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
"""
'''
input_list = inputstr.strip().split("\n")

motif =  "N{P}[ST]{P}"

def motifToRegExp(motif):
    my_regex = re.sub(r'{(?P<aa>[A-Z])}',r'[^\g<aa>]', motif)
    return '(?=' + my_regex + ")"
    
my_regex = motifToRegExp(motif)

for item in input_list:
    if len(item) > 0:
        my_handle = urllib.urlopen('http://www.uniprot.org/uniprot/' + item + '.fasta')
        seq_record = SeqIO.read(my_handle, 'fasta')
        my_seq = str(seq_record.seq)
        if re.search(my_regex,my_seq):
            print item
            print " ".join([str(my_match.start() + 1) for my_match in re.finditer(my_regex, my_seq)])
                
        my_handle.close()