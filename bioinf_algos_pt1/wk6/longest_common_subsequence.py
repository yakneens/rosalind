import numpy as np
import sys

sys.setrecursionlimit(10000)
'''
myFilename = "/Users/siakhnin/Downloads/dataset_74_5 (2).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """AACCTTGG
     ACACTGTGA"""

input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)

str2 = input_list[1].strip()
str2_len = len(str2)
def computeAlignment(str1 ,str2):
    s = np.zeros((str1_len+1,str2_len+1))
    backtrack = np.zeros((str1_len+1, str2_len+1))
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                s[i,j] = max(s[i-1,j-1] + 1,s[i-1,j], s[i,j-1])
            else:
                s[i,j] = max(s[i-1,j], s[i,j-1])
            
            if s[i,j] == s[i-1,j-1] + 1 and str1[i-1] == str2[j-1]:
                backtrack[i,j] = 3    
            elif s[i,j] == s[i,j-1]:
                backtrack[i,j] = 2
            elif s[i,j] == s[i-1,j]:
                backtrack[i,j] = 1
            
            
    return s, backtrack

s, backtrack = computeAlignment(str1, str2)
#print str1_len, str2_len
print str1
print str2
print s
print backtrack
#print s
#print backtrack
output = []
def outputLCS(backtrack, str1, i, j):
    if i == 0 or j == 0:
        return
    if backtrack[i,j] == 1:
        outputLCS(backtrack, str1, i-1, j)
    elif backtrack[i,j] == 2:
        outputLCS(backtrack, str1, i, j-1)
    else:
        outputLCS(backtrack, str1, i-1, j-1)
        output.append(str1[i-1])
        
outputLCS(backtrack, str1, str1_len, str2_len)

print "".join(output) 