import re
import collections
import numpy as np
from operator import mul




myFilename = "/Users/siakhnin/Downloads/dataset_39_3.txt"


f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
     5
     A C G T
     0.2 0.4 0.3 0.1
     0.2 0.3 0.3 0.2
     0.3 0.1 0.5 0.1
     0.2 0.5 0.2 0.1
     0.3 0.1 0.4 0.2
"""
inputstr = """GGTATGCGCACTTCCGAAGAAGGATGCTCAATCATACAAGACACATTCCATCGAGGTAGTTTGACTGGCGAAGTCCCGACTCGCTCACAACTAGTATCCTGTGAAGTCCAGCGTTGAACGACGTGTTGGCTTTAAGCGCCCTGCTTTTCACCAGTTTCTCTCCTAAGTTCGTTCCAGGTCCAAACTGTGGCACTGCAAAT
7
A C G T
0.357 0.357 0.179 0.107
0.393 0.179 0.143 0.286
0.179 0.179 0.321 0.321
0.214 0.179 0.321 0.286
0.286 0.25 0.25 0.214
0.286 0.25 0.179 0.286
0.393 0.143 0.214 0.25"""
'''

inputlist = [x.strip() for x in inputstr.split("\n") if len(x) > 0]
dna_str = inputlist[0]
k = int(inputlist[1].strip())
nuc_to_col_mapping = dict([(v,i) for i,v in enumerate(inputlist[2].split(" "))])

vals = [i.split(" ") for i in inputlist[3:]]
vals = [float(f) for i in vals for f in i]
profile_matrix = np.array(vals)
profile_matrix = np.reshape(profile_matrix,(k,4))

# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]

# Return tuple (my_dna_str, prob) where prob is the probability of generating my_dna_str under profile
def profileProbabilityOf(my_dna_str,profile):
    return (my_dna_str,reduce(mul,[profile[c[0]][nuc_to_col_mapping[c[1]]] for c in enumerate(my_dna_str)],1))

# Return the kmer corresponding to the max probability of being generated under profile
def bestKmer(dna_str, k):
    return max([profileProbabilityOf(my_str, profile_matrix) for my_str in allKmersOf(dna_str,k)], key=lambda x: x[1])[0]
    
print bestKmer(dna_str, k)
