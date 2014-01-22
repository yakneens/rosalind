from Bio import SeqIO
from collections import Counter

seq_list = []

for seq_record in SeqIO.parse('/Users/siakhnin/Downloads/rosalind_tran.txt', 'fasta'):
    seq_list.append(seq_record.seq)
    
t_v_dict = {('A', 'T'):'v', 
            ('A', 'C'):'v', 
            ('A', 'G'):'t', 
            ('T', 'A'):'v', 
            ('T', 'C'):'t', 
            ('T', 'G'):'v', 
            ('C', 'A'):'v', 
            ('C', 'T'):'t', 
            ('C', 'G'):'v', 
            ('G', 'A'):'t', 
            ('G', 'T'):'v', 
            ('G', 'C'):'v'}    
outcomes = []    
for a,b in zip(seq_list[0],seq_list[1]):
    outcomes.append((a,b))
    
my_counts = Counter(outcomes)    
t_count = 0.0
v_count = 0.0

for k in my_counts.keys():
    val = t_v_dict.get(k)
    if val != None:
        if val == 't':
            t_count += my_counts[k]   
        elif val == 'v':
            v_count += my_counts[k]
            
print (t_count / v_count) 