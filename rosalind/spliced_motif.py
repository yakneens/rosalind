import re

myFilename = "/Users/siakhnin/Downloads/rosalind_sseq (1).txt"
f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr=""">Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA"""
'''

inputlist = inputstr.split(">")
inputs = []
for i in inputlist:
    
    x = re.match('Rosalind_[0-9]*',i)
    
    if x:
        inputs.append(i[x.end():].replace('\n','').strip())

s = inputs[0]
t = inputs[1]
ans = []
i = 0
for c in t:
    flag = True
    while flag:
        if i < len(s):
            if s[i] == c:
                ans.append(i+1)
                i += 1
                flag = False
            else:
                i += 1
        else:
            break
            
if len(ans) == len(t):
    print " ".join([str(x) for x in ans])