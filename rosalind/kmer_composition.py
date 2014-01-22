from Bio import SeqIO
from collections import Counter
import itertools as it

seq_list = []

seq_record = SeqIO.read('/Users/siakhnin/Downloads/rosalind_kmer (1).txt', 'fasta')
dna_str = str(seq_record.seq)


# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            
kmers_list = [kmer for kmer in allKmersOf(dna_str,4)]

kmer_counts = Counter(kmers_list)

kmer_list = []
kmer_dict = {}
vals = it.product('ACGT', repeat=4)

for i, val in enumerate(vals):
    kmer_list.append(0)
    kmer_dict[''.join(val)] = i
    
for key in kmer_counts.keys():
    kmer_list[kmer_dict[key]] = kmer_counts[key]
    
print " ".join([str(kmer) for kmer in kmer_list])