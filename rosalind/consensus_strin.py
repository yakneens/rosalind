import re
import collections
from numpy import *



myFilename = input("Eneter filename:")

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""
'''

inputlist = inputstr.split(">")
input_matrix = list()

for i in inputlist:
    
    x = re.match('Rosalind_[0-9]*',i)
    
    if x:
        dna_str = i[x.end():].replace('\n','').strip()
        input_matrix.append(list(dna_str))


new_matrix = array(input_matrix)

nuc_lookup = {'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3}
rev_nuc_lookup = {0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T'}

profile_matrix = zeros((4, new_matrix.shape[1]),int)


i = 0
for row in new_matrix.T:
    char_counter = collections.Counter(row)
    for x in char_counter:
        profile_matrix[nuc_lookup[x],i] = char_counter[x]
    
    i += 1

cons_str = ''

for val in profile_matrix.argmax(axis=0):
    cons_str += rev_nuc_lookup[val]


print(cons_str)    

print('A: ' + ' '.join(map(str, profile_matrix[0])))
print('C: ' + ' '.join(map(str, profile_matrix[1])))
print('G: ' + ' '.join(map(str, profile_matrix[2])))
print('T: ' + ' '.join(map(str, profile_matrix[3])))
