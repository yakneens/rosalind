import numpy as np
import operator
import itertools as it


myFilename = "/Users/siakhnin/Downloads/dataset_36_7.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """3 1
     ATTTGGC
     TGCCTTA
     CGGTATC
     GAAAATT"""
''' 
inputlist = [x.strip() for x in inputstr.split("\n")]
params = [x.strip() for x in inputlist[0].split(" ")]
k = int(params[0])
d = int(params[1])
dna_strings = inputlist[1:]

ne = operator.ne

def getHammingDistance(str1,str2):
    return sum(map(ne,str1, str2))

def allKmersOf(str, k):
    if len(str) >= k:
        for i in range(0,len(str) - k + 1):
            yield str[i:i+k]
            
            
        
def getMinDistance(str1,str2):
    bigger = ""
    smaller = ""
    
    
    if len(str1) >= len(str2):
        bigger = str1
        smaller = str2
    else:
        bigger = str2
        smaller = str1
    
    min_distance = len(smaller)
    
    for kmer in allKmersOf(bigger, len(smaller)):    
        cur_distance = getHammingDistance(smaller, kmer)
        
        if cur_distance < min_distance:
            min_distance = cur_distance  
        
    return min_distance

def allDKmersOf(kmer,d): 
    dkmers = set()
    #took this awesome code from stackoverflow
    for x in it.combinations(range(len(kmer)), d):
        this_word = [[char] for char in kmer]
        for loc in x:
            this_word[loc] = [l for l in 'ACTG']
        for poss in it.product(*this_word):
            dkmers.add("".join(item[0] for item in poss))
    
    return dkmers

def isMotif(kmer,dna_strings,d):
    for my_str in dna_strings:
        if getMinDistance(kmer, my_str) > d:
            return False
        
    return True

def motifEnumeration():
    my_kmers = set()
    for my_str in dna_strings:
        for kmer in allKmersOf(my_str,k):
            dkmers = allDKmersOf(kmer, d)
            for dkmer in dkmers:
                if isMotif(dkmer,dna_strings,d):
                    my_kmers.add(dkmer)
    print("\n".join([kmer for kmer in my_kmers]))  
                 
motifEnumeration()