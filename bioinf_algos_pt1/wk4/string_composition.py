import numpy as np
import operator
import itertools as it


myFilename = "/Users/siakhnin/Downloads/dataset_51_3 (1).txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """5
     CAATCCAAC"""
''' 
inputlist = [x.strip() for x in inputstr.split("\n")]
k = int(inputlist[0].strip())
dna_string = inputlist[1].strip()
print dna_string

def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            

def stringComposition(dna_string, k):
    return sorted(allKmersOf(dna_string, k))

f = open('string_composition.out', 'w')
f.write("\n".join(sorted(allKmersOf(dna_string,k))))
#print "\n".join(sorted(allKmersOf(dna_string,k)))
#print "\n".join(stringComposition(dna_string,k))