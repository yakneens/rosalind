import numpy as np
import sys
import re

sys.setrecursionlimit(10000)


myFilename = "/Users/siakhnin/Downloads/dataset_80_5 (2).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''

inputstr = """ATATCCG
     TCCGA
     ATGTACTG"""
'''

# Parse the input strings
input_list = [x.strip() for x in inputstr.split("\n")]     


# Look up cost of letters c1 and c2 based on the scoring matrix
def getCost(vals):
    if np.all(vals == vals[0]):
        return 1
    else:
        return 0


def computeAlignment(input_strings):
    lengths = []
    for my_str in input_strings:
        lengths.append(len(my_str) + 1)
    len_tup = tuple(lengths)
    
    s = np.zeros(len_tup)
    backtrack = np.zeros(len_tup)
    backtrack[1:,0,0] = 2
    backtrack[0,1:,0] = 3
    backtrack[0,0,1:] = 4
    backtrack[1:,1:,0] = 5
    backtrack[1:,0,1:] = 6
    backtrack[0,1:,1:] = 7
    
    for i in range(1, len_tup[0]):
        for j in range(1, len_tup[1]):
            for k in range(1, len_tup[2]):
                #Cost of a diagonal move that consumes 1 character from each string
                diag = s[i-1,j-1,k-1] + getCost(np.array([input_strings[0][i-1], input_strings[1][j-1], input_strings[2][k-1]]))
                
                
                
                
                vals = [diag, s[i-1,j,k], s[i,j-1,k], s[i,j,k-1], s[i-1,j-1,k], s[i-1,j,k-1], s[i,j-1,k-1]]
                
                #Pick max cost between diagonal, downward or rightward moves
                s[i,j,k] = max(vals)
                
                #Remember which move we chose
                backtrack[i,j,k] = np.argmax([vals]) + 1    
            
    return s, backtrack

s, backtrack = computeAlignment(input_list)

'''print s
print "backtrack"
print backtrack'''


out1 = []
out2 = []
out3 = []

lengths = []
for my_str in input_list:
    lengths.append(len(my_str))
len_tup = tuple(lengths)
    
#Recursive function to print the alignment
def outputGA(backtrack, input_list, i, j, k):
    
    # Base case
    if i == 0 and j == 0 and k == 0:
        return
    if backtrack[i,j,k] == 2:
        outputGA(backtrack, input_list, i-1, j,k)
        out1.append(input_list[0][i-1])
        out2.append("-")
        out3.append("-")        
    elif backtrack[i,j,k] == 3:
        outputGA(backtrack, input_list, i, j-1,k)
        out1.append("-")
        out2.append(input_list[1][j-1])
        out3.append("-")
    elif backtrack[i,j,k] == 4:
        outputGA(backtrack, input_list, i, j,k-1)
        out1.append("-")
        out2.append("-")
        out3.append(input_list[2][k-1])
    elif backtrack[i,j,k] == 5:
        outputGA(backtrack, input_list, i-1, j-1,k)
        out1.append(input_list[0][i-1])
        out2.append(input_list[1][j-1])
        out3.append("-")
    elif backtrack[i,j,k] == 6:
        outputGA(backtrack, input_list, i-1, j,k-1)
        out1.append(input_list[0][i-1])
        out2.append("-")
        out3.append(input_list[2][k-1])        
    elif backtrack[i,j,k] == 7:
        outputGA(backtrack, input_list, i, j-1,k-1)
        out1.append("-")
        out2.append(input_list[1][j-1])
        out2.append(input_list[2][k-1])        
    elif backtrack[i,j,k] == 1:
        outputGA(backtrack, input_list, i-1, j-1,k-1)
        out1.append(input_list[0][i-1])
        out2.append(input_list[1][j-1])
        out3.append(input_list[2][k-1])
        
outputGA(backtrack, input_list, lengths[0], lengths[1], lengths[2])

print int(s[lengths[0], lengths[1], lengths[2]])
print "".join(out1)
print "".join(out2)
print "".join(out3)