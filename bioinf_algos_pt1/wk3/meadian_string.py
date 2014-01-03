import numpy as np
import operator
import itertools as it


myFilename = "/Users/siakhnin/Downloads/dataset_38_7.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ 3
     AAATTGACGCAT
     GACGACCACGTT
     CGTCAGCGCCTG
     GCTGAGCACCGG
     AGTACGGGACAG"""
inputstr = """6
TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT
CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA
TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT
TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA
ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG
TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA
TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC
GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA
CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG
CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"""
''' 
inputlist = [x.strip() for x in inputstr.split("\n")]
k = int(inputlist[0].strip())
dna_strings = inputlist[1:]

ne = operator.ne

def getHammingDistance(str1,str2):
    return sum(map(ne,str1, str2))

def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            
            
        
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

def bruteMedianString():
    allKmers = allDKmersOf('A'*k, k)
    min_score = int(len(dna_strings[0]) / 4) * k
    best_kmer = ""
    for kmer in allKmers:
        distance = sum([getMinDistance(kmer,dna_str) for dna_str in dna_strings])
        
        if distance < min_score:
            min_score = distance
            best_kmer = kmer
            
    print best_kmer
    
bruteMedianString()

