import re
import sys

myFilename = input("Eneter filename:")

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """>Rosalind_6404 
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"""

'''
inputlist = inputstr.split(">")

inputdict = dict()

for i in inputlist:
    
    x = re.match('Rosalind_[0-9]{4}',i)
    
    if x:
        inputdict[i[x.start():x.end()]] = i[x.end():].replace('\n','')
#print(inputdict)

maxCount = 0
maxKey = ""


for i,v in enumerate(inputdict):
    x = 100 * (inputdict[v].count('C') + inputdict[v].count('G')) / len(inputdict[v])
    
    if x > maxCount:
        maxCount = x
        maxKey = v

print('' + maxKey + "\n" + str(maxCount))