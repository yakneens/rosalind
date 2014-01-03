import numpy as np
import sys
import re

sys.setrecursionlimit(10000)


myFilename = "/Users/siakhnin/Downloads/dataset_77_7.txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """PAWHEAE
     HEAGAWGHEE"""
'''

# Parse the two input strings
input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)
str2 = input_list[1].strip()
str2_len = len(str2)


# Indel penalty
sigma = -2

# Look up cost of letters c1 and c2 based on the scoring matrix
def getCost(c1, c2):
    if c1 == c2:
        return 1
    else:
        return -2

def computeAlignment(str1 ,str2):
    
    s = np.zeros((str1_len+1,str2_len+1))
    
    backtrack = np.zeros((str1_len+1, str2_len+1))
    
    #Init first row with indel costs
    s[0,:] = np.arange(str2_len+1) * sigma
    
    #First column is all zeros to allow consuming an arbitrary prefix of str1 for 0 cost
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            
            #Cost of a diagonal move that consumes 1 character from each string
            diag = s[i-1,j-1] + getCost(str1[i-1], str2[j-1])
            
            #Pick max cost between diagonal, downward or rightward moves
            s[i,j] = max(diag,s[i-1,j] + sigma, s[i,j-1] + sigma)
            
            #Remember which move we chose
            backtrack[i,j] = np.argmax([[diag, s[i-1,j] + sigma, s[i,j-1] + sigma]])    
            
    return s, backtrack

s, backtrack = computeAlignment(str1, str2)


# The best fitting alignment corresponds to the maximum score in the last row of matrix s
print str(int(max(s[-1,:])))
max_s1 = str1_len
# Detect max_s2 from the back of the array so that a maximal length overlap is detected
max_s2 = str2_len - np.argmax(s[-1,::-1])

#print max_s1, max_s2
#print str1
#print str2
#print s
#print backtrack


out1 = []
out2 = []

#Recursive function to print the alignment
def outputGA(backtrack, str1, str2, i, j):
    
    # Base case
    if j == 0:
        return
    elif backtrack[i,j] == 0:
        outputGA(backtrack, str1, str2, i-1, j-1)
        out1.append(str1[i-1])
        out2.append(str2[j-1])
    elif backtrack[i,j] == 1:
        outputGA(backtrack, str1, str2, i-1, j)
        out2.append("-")
        out1.append(str1[i-1])
    elif backtrack[i,j] == 2:
        outputGA(backtrack, str1, str2, i, j-1)
        out1.append("-")
        out2.append(str2[j-1])

        
outputGA(backtrack, str1, str2, max_s1, max_s2)

print "".join(out1)
print "".join(out2)
