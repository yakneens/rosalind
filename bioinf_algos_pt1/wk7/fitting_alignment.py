import numpy as np
import sys
import re

sys.setrecursionlimit(10000)


myFilename = "/Users/siakhnin/Downloads/dataset_77_5 (1).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """GTAGGCTTAAGGTTA
     TAGATA"""
'''

# Parse the two input strings
input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)
str2 = input_list[1].strip()
str2_len = len(str2)

# Set up the PAM250 scoring matrix
aa_ind_map = {"A":0,"C":1,"G":2,"T":3}
a = """1 -1 -1 -1
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 1"""
b = a.split("\n")
z = np.zeros((20,20))
for i,k in enumerate(b):
    c = re.split(r"\s*", k.strip())
    for j,l in enumerate(c):
        z[i,j] = int(l.strip())

# Indel penalty
sigma = -1

# Look up cost of letters c1 and c2 based on the scoring matrix
def getCost(c1, c2):
    return z[aa_ind_map[c1], aa_ind_map[c2]]

def computeAlignment(str1 ,str2):
    
    s = np.zeros((str1_len+1,str2_len+1))
    
    backtrack = np.zeros((str1_len+1, str2_len+1))
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            
            #Cost of a diagonal move that consumes 1 character from each string
            diag = s[i-1,j-1] + getCost(str1[i-1], str2[j-1])
            
            #Pick max cost between diagonal, downward or rightward moves
            s[i,j] = max(diag,s[i-1,j] + sigma, s[i,j-1] + sigma, 0)
            
            #Remember which move we chose
            backtrack[i,j] = np.argmax([[diag, s[i-1,j] + sigma, s[i,j-1] + sigma, 0]])    
            
    return s, backtrack

s, backtrack = computeAlignment(str1, str2)

#print s

# The best fitting alignment corresponds to the maximum score in the last column of matrix s that occurs after row str2_len 
# i.e. consumes all of str2 and at least len(str2) of str1
print str(int(max(s[str2_len:,-1])))
max_s1 = str2_len + np.argmax(s[str2_len:,-1])
max_s2 = str2_len
#print max_s1, max_s2


#print s
#print backtrack


out1 = []
out2 = []

#Recursive function to print the alignment
def outputGA(backtrack, str1, str2, i, j):
    
    # Base case
    if j == 0:
        return
    elif backtrack[i,j] == 1:
        outputGA(backtrack, str1, str2, i-1, j)
        out2.append("-")
        out1.append(str1[i-1])
    elif backtrack[i,j] == 2:
        outputGA(backtrack, str1, str2, i, j-1)
        out1.append("-")
        out2.append(str2[j-1])
    elif backtrack[i,j] == 3:
        out1.append(str1[i-1])
        out2.append(str2[j-1])
        return
    else:
        outputGA(backtrack, str1, str2, i-1, j-1)
        out1.append(str1[i-1])
        out2.append(str2[j-1])
        
outputGA(backtrack, str1, str2, max_s1, max_s2)

print "".join(out1)
print "".join(out2)
