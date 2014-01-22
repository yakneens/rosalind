import operator
import itertools as it
import re

myFilename = "/Users/siakhnin/Downloads/rosalind_lcsm (3).txt"

f = open(myFilename, 'r')
input_str = f.read()

'''
input_str =  """3 1
     ATTTGGC
     TGCCTTA
     CGGTATC
     GAAAATT"""
input_str = """
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
'''    
inputlist = input_str.split(">")
input_matrix = list()
dna_strings = []

for i in inputlist:
    
    x = re.match('Rosalind_[0-9]*',i)
    
    if x:
        dna_str = i[x.end():].replace('\n','').strip()
        dna_name = i[:x.end()]
        dna_strings.append(dna_str)


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

def isMotif(kmer,dna_strings):
    for my_str in dna_strings:
        if not kmer in my_str:
            return False
        
    return True

def motifEnumeration(dna_strings, k):
    my_kmers = set()
    
    for kmer in allKmersOf(dna_strings[0],k):
        if isMotif(kmer,dna_strings):
            my_kmers.add(kmer)
            return my_kmers
    
    return my_kmers
                 
def findLargestMotif():
    for i in range(len(dna_strings[0]))[::-1]:
        print i
        my_kmers = motifEnumeration(dna_strings, i)
        
        if len(my_kmers) > 0:
            return my_kmers
        
        
my_kmers = findLargestMotif()        
#my_kmers = motifEnumeration(dna_strings, k,d)

print(my_kmers.pop())  