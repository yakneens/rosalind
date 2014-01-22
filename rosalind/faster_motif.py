from Bio import SeqIO



seq_record = SeqIO.read('/Users/siakhnin/Downloads/rosalind_kmp.txt', 'fasta')
inputstr = seq_record.seq
'''

inputstr = """CAGCATGGTATCACAGCAGAG"""
'''


strlen = len(inputstr)
b = (strlen + 1)*[None]
i = 0
j = -1
b[i] = j

while i < strlen:
    while j >= 0 and inputstr[i] != inputstr[j]:
        j = b[j]
    i+=1
    j+=1
    b[i]=j
    
    
print " ".join([str(x) for x in b[1:]])