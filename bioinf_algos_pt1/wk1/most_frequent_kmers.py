import re
import sys
import operator

#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/rosalind_1a.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ACGTTGCATGTCGCATGATGCATGAGAGCT
     4"""
'''

inputlist = [x.strip() for x in inputstr.split("\n")]
inputstr = inputlist[0]
k = int(inputlist[1])
inputdict = dict()
maxcount = 0

for i,c in enumerate(inputstr):
    current_kmer = inputstr[i:i+k];
    if inputdict.has_key(current_kmer) :
        inputdict[current_kmer] = inputdict[current_kmer] + 1
    else:
        inputdict[current_kmer] = 1
        
    if inputdict[current_kmer] > maxcount:
        maxcount = inputdict[current_kmer]
outstr = "" 
for key in inputdict.keys():
    if inputdict[key] == maxcount:
        outstr = outstr + key + " "
                
print(outstr)