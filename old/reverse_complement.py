import re
import sys
import operator

#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/rosalind_1b.txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr =  """AAAACCCGGT"""
'''
def getDNAReverseComplement(dna_str):
    complements = {'A':'T','C':'G','G':'C','T':'A'}
    outstr = ""
    
    for c in inputstr:
        outstr += complements[c]
    
    return outstr[::-1]

print(getDNAReverseComplement(inputstr))