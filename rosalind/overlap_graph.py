import re

myFilename = "/Users/siakhnin/Downloads/rosalind_grph (7).txt"
f = open(myFilename, 'r')
input_str = f.read()
'''

input_str = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""
'''
inputlist = input_str.split(">")
input_matrix = list()
dna_reads = {}

for i in inputlist:
    
    x = re.match('Rosalind_[0-9]{4}',i)
    
    if x:
        dna_str = i[x.end():].replace('\n','').strip()
        dna_name = i[:x.end()]
        dna_reads[dna_name] = dna_str
        

k = 3

def listBasedGraph():
    
    suff_dict = {}
    
    for key in dna_reads.keys():
        suff = tuple(dna_reads[key][-k:])
        suff_dict.setdefault(suff, []).append(key)
    
    answers = []
    for key in dna_reads.keys():
        pref = tuple(dna_reads[key][:k])
        if pref in suff_dict and key not in suff_dict[pref] :
            for val in suff_dict[pref]:
                answers.append((val, key))
    
    
        
    return answers

def listBasedGraph2():
    
    answers = []
    
    for key in dna_reads.keys():
        suff = tuple(dna_reads[key][-k:])
        
        for key2 in dna_reads.keys():
            pref = tuple(dna_reads[key2][:k])
            if pref == suff and dna_reads[key] != dna_reads[key2] :
                    answers.append((key, key2))
    
    
        
    return answers
final = sorted(listBasedGraph(), key=lambda x:x[0])
final2 = sorted(listBasedGraph2(), key=lambda x:x[0])


#print ("\n".join([dna_reads[x[0]] + " "+  dna_reads[x[1]] for x in final]))
print ("\n".join([x[0] + " "+  x[1] for x in final2]))
