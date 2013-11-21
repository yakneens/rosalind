from networkx import *
import re

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

inputlist = input_str.split(">")
input_matrix = list()

for i in inputlist:
    
    x = re.match('Rosalind_[0-9]',i)
    
    if x:
        dna_str = i[x.end():].replace('\n','').strip()
        input_matrix.append(list(dna_str))

print(inputlist)
