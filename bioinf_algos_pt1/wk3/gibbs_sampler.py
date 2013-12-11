import re
import collections
import numpy as np
from operator import mul
import operator
import random
import cProfile

myFilename = "/Users/siakhnin/Downloads/dataset_43_4 (2).txt"


f = open(myFilename, 'r')
inputstr = f.read()

'''

inputstr =  """8 5 100
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
n = int(param[2].strip())

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
def profileProbabilityOf2(my_dna_str,profile):
    return (my_dna_str, np.prod(profile[np.arange(len(my_dna_str)), np.array([nuc_to_col_mapping[c] for c in my_dna_str])]))


def profileProbabilityOf(my_dna_str,profile):
    tot = 1
    for c in enumerate(my_dna_str):
        tot *= profile[c[0]][nuc_to_col_mapping[c[1]]]
    
    return (my_dna_str, tot)

def generateRandomMotifList(dna_strings):
    my_motif_list = []
    for dna_string in dna_strings:
        my_index = random.randint(0,len(dna_string) - k-1)
        my_motif_list.append(dna_string[my_index:my_index+k])
    
    return my_motif_list

def generateRandomMotifDict(dna_strings):
    my_motif_dict = {}
    for i,dna_string in enumerate(dna_strings):
        my_index = random.randint(0,len(dna_string) - k-1)
        my_motif_dict[i] = dna_string[my_index:my_index+k]
    
    return my_motif_dict

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

def getGibbsMotif(dna_str, profile):
    kmer_prob_dict = {}
    prob_sum = 0
    for i, kmer in enumerate(allKmersOf(dna_str,k)):
        kmer_prob = profileProbabilityOf(kmer, profile)
        kmer_prob_dict[(i,kmer)] = (i, prob_sum, prob_sum + kmer_prob[1])
        prob_sum += kmer_prob[1]
    
   
    rnum = random.random()
    sampled = rnum*prob_sum
    
    for (i,kmer) in kmer_prob_dict:
        ind,lower,upper = kmer_prob_dict[(i,kmer)]
        
        if sampled >= lower and sampled < upper:
            return kmer

    print "Uhoh" 
    
def gibbsSample(dna_str,k,t,num_iters, num_runs):
    global_best_motifs = generateRandomMotifDict(dna_str)
    
    global_best_motif_score = getMotifScore(global_best_motifs.values())
    
    for i in range(num_runs):
        print i   
        cur_motifs = generateRandomMotifDict(dna_str)
        
        best_motifs = dict(cur_motifs)
        best_motif_score = getMotifScore(best_motifs.values())
        
        for j in range(num_iters):
            ind = random.randint(0, t - 1)
            
            cur_motifs.pop(ind)
            #cur_list = list(dna_str[0:ind])
            #cur_list.extend(dna_str[ind+1:])
            motifs_for_profile = [cur_motifs[x] for x in sorted(cur_motifs)]
            cur_profile = createProfile(motifs_for_profile, withPseudoCounts=True)
        
            new_motif = getGibbsMotif(dna_str[ind], cur_profile)
            cur_motifs[ind] = new_motif
            
            cur_motif_score =  getMotifScore(cur_motifs.values())
            
            if cur_motif_score < best_motif_score:
                best_motifs = dict(cur_motifs)
                best_motif_score = cur_motif_score
                
        if best_motif_score < global_best_motif_score:
            global_best_motifs = dict(best_motifs)
            global_best_motif_score = best_motif_score
    
    return global_best_motifs

def doIt():
    result = gibbsSample(dna_strings,k,t,n,20)
    print("\n".join([result[x] for x in sorted(result)]))
    print(getMotifScore(result.values()))
cProfile.run('doIt()')
#doIt()