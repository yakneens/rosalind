import re
import collections
import numpy as np
from operator import mul
import operator
import random


myFilename = "/Users/siakhnin/Downloads/dataset_41_4 (8).txt"


f = open(myFilename, 'r')
inputstr = f.read()

'''


inputstr =  """8 5
     CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
     AATCCACCAGCTCCACGTGCAATGTTGGCCTA"""
'''
inputlist = [x.strip() for x in inputstr.split("\n") if len(x) > 0]
param = inputlist[0].split(" ")
k = int(param[0].strip())
t = int(param[1].strip())

dna_strings = inputlist[1:]

nuc_to_col_mapping = {"A":0, "C":1, "G":2, "T":3}
col_to_nuc_mapping = {0:"A", 1:"C", 2:"G", 3:"T"}

ne = operator.ne

def getHammingDistance(str1,str2):
    return sum(map(ne,str1, str2))

# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            
# Return tuple (my_dna_str, prob) where prob is the probability of generating my_dna_str under profile
def profileProbabilityOf(my_dna_str,profile):
    return (my_dna_str,reduce(mul,[profile[c[0]][nuc_to_col_mapping[c[1]]] for c in enumerate(my_dna_str)],1))
            
def bestKmer(dna_str, profile, k):
    return max([profileProbabilityOf(my_str, profile) for my_str in allKmersOf(dna_str,k)], key=lambda x: x[1])[0]

def allBestKmers(dna_strings,profile,k):
    return [bestKmer(dna_string,profile,k) for dna_string in dna_strings]

def generateInitialMotifList():
    return [dna_string[0:k] for dna_string in dna_strings]

def generateRandomMotifList():
    my_motif_list = []
    for dna_string in dna_strings:
        my_index = random.randint(0,len(dna_string) - k-1)
        my_motif_list.append(dna_string[my_index:my_index+k])
    
    return my_motif_list

def createProfile(dna_strings, withPseudoCounts):
    profile = np.zeros((len(dna_strings[0]),4))
    x = np.array([list(dna_str) for dna_str in dna_strings])
    
    total_samples = len(dna_strings)
    
    if withPseudoCounts:
        total_samples += 4
    
    counters = [collections.Counter(x[:,i]) for i in range(len(dna_strings[0]))]
    for i,c in enumerate(counters):
        for ch in 'ACGT':
            current_count = float(c[ch])
            if withPseudoCounts:
                current_count += 1
            profile[i][nuc_to_col_mapping[ch]] = current_count / total_samples
        
    return profile

def buildConsensusString(motifs):
    current_profile = createProfile(motifs, withPseudoCounts=True)
    cons_str = ""
    for val in current_profile.argmax(axis=1):
        cons_str += col_to_nuc_mapping[val]
    
    return cons_str

def getMotifScore(motifs):
    consensus_string = buildConsensusString(motifs)
    motif_score = 0
    for motif in motifs:
        motif_score += getHammingDistance(motif, consensus_string)
    return motif_score
motif_scores = {}

def randomizedMotifSearch(dna_str,k,t,num_iters):
    global_best_motifs = generateRandomMotifList()
    global_best_motif_score = getMotifScore(global_best_motifs)
    
    for i in range(num_iters):
    
        best_motifs = generateRandomMotifList()
        best_motif_score = getMotifScore(best_motifs)
        
        my_motifs = best_motifs
        
        while True:
            current_profile = createProfile(my_motifs, withPseudoCounts=True)
            
            my_motifs = allBestKmers(dna_strings,current_profile,k)
            
            my_motif_score =  getMotifScore(my_motifs)
            
            if my_motif_score < best_motif_score:
                best_motifs = my_motifs
                best_motif_score = my_motif_score
            else:
                break;
        
        if best_motif_score < global_best_motif_score:
            global_best_motifs = best_motifs
            global_best_motif_score = best_motif_score
    
    return global_best_motifs
    
print("\n".join(randomizedMotifSearch(dna_strings,k,t,1000)))