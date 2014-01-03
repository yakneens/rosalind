import numpy as np
import sys
import re

sys.setrecursionlimit(10000)

myFilename = "/Users/siakhnin/Downloads/dataset_78_8 (13).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """PRTEINS
     PRTWPSEIN"""
inputstr = """ADDFFFSWDFVDFSWDHF
DFFFSFVQIFQDFSHE"""
inputstr = """KDFFFSWDFVDFSWDRRHEDEAPIAVSDIHDYSALFFEVVHDVLQYIQENWLWCGLLFMHTQCWNHKCCFFTTEVEN
KDFFFSFVQIVFVAFDFQDFSRRHEDEAPITVSDIHRYSSLFFEVVHDVLQYIQENWPWCGASCIFMHTQCWNHKMCFVTTEVEN"""
inputstr = """KFLWGRWPFFPPARMFDFIMDICGSFPRSLFQKAGTVKMVGRRRTIYLCIKPCLPLHRPPQYKMHPKHMCQIRQPTSGNKL
KECFMDLWGNWPFFPPARMFDTMDICFPFPGSLFQAVKMVGRAFRDARTIYLCIKPCLPCHRPPQCKMHPKHMCQIRQRFTSVNKL"""
inputstr = """DDDWWWDDD
WWW"""
inputstr = """GRRR
GRAFRDAR"""
inputstr = """FVSALYQFEPSLKCMYLH
MYIFIMDFVSALYQFEPSLKC"""
inputstr = """FVSA
MYIFIMD"""
inputstr = """QPYHSETSVDYPVGSEATTDNCNCLPTIWVTVFPMAIVMYLVPMFSMCWLKHAVGLDHLMMRWPWHNSFHDMMTNKNCWL
QPYHYPTKTTSVDYPVGSEAGTDNYNCLPTHTFQHFWVTVFEYVMYLMFSMDEVGQFKTWLKHIIAAGPVGLMMRWPMTNKSWWL"""
inputstr = """PTI
PTHTFQHF"""
'''

# Parse the two input strings
input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)
str2 = input_list[1].strip()
str2_len = len(str2)

# Set up the BLOSUM62 scoring matrix
aa_ind_map = {"A":0,"C":1,"D":2,"E":3,"F":4,"G":5,"H":6,"I":7,"K":8,"L":9,"M":10,"N":11,"P":12,"Q":13,"R":14,"S":15,"T":16,"V":17,"W":18,"Y":19}
a = """4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7"""
b = a.split("\n")
z = np.zeros((20,20))
for i,k in enumerate(b):
    c = re.split(r"\s*", k.strip())
    for j,l in enumerate(c):
        z[i,j] = int(l.strip())

# Indel penalty
sigma = -11
epsilon = -1

# Look up cost of letters c1 and c2 based on the scoring matrix
def getCost(c1, c2):
    return z[aa_ind_map[c1], aa_ind_map[c2]]

def computeAlignment(str1 ,str2):
    
    m = np.zeros((str1_len+1,str2_len+1))
    l = np.zeros((str1_len+1,str2_len+1))
    u = np.zeros((str1_len+1,str2_len+1))
    
    
    #Init first row and column with indel costs
    m[1:,0] = np.arange(str1_len).T * epsilon + sigma
    m[0,1:] = np.arange(str2_len) * epsilon + sigma
    
    l[1:,0] = np.arange(str1_len).T * epsilon + sigma
    l[0,:] = -np.inf
    
    u[0,1:] = np.arange(str2_len) * epsilon + sigma
    u[:,0] = -np.inf
    
    backtrack = np.zeros((str1_len+1, str2_len+1))
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            
            #lower level score
            l[i,j] = max(l[i-1,j] + epsilon,m[i-1,j] + sigma)
            
            #upper level score
            u[i,j] = max(u[i,j-1] + epsilon,m[i,j-1] + sigma)
            
            #Cost of a diagonal move that consumes 1 character from each string
            diag = m[i-1,j-1] + getCost(str1[i-1], str2[j-1])
            
            #Pick max cost between diagonal, downward or rightward moves
            m[i,j] = max(diag, l[i,j], u[i,j])
            
            #Remember which move we chose
            backtrack[i,j] = np.argmax([[l[i,j], u[i,j], diag]])    
            
    return m, l, u, backtrack

m, l, u, backtrack = computeAlignment(str1, str2)

print l
print m
print u
print str1,str2
print backtrack

# This is the score of the alignment
print int(m[str1_len,str2_len])

out1 = []
out2 = []

#Recursive function to print the alignment
def outputGA(backtrack, str1, str2, i, j):
    
    # Base case
    if i == 0 and j == 0:
        return
    if i == 0:
        outputGA(backtrack, str1, str2, i, j-1)
        out1.append("-")
        out2.append(str2[j-1])
    elif j == 0:
        outputGA(backtrack, str1, str2, i-1, j)
        out1.append(str1[i-1])
        out2.append("-")
    elif backtrack[i,j] == 2:
        outputGA(backtrack, str1, str2, i-1, j-1)
        out1.append(str1[i-1])
        out2.append(str2[j-1])
    elif backtrack[i,j] == 0:
        outputGA(backtrack, str1, str2, i-1, j)
        out2.append("-")
        out1.append(str1[i-1])
    elif backtrack[i,j] == 1:
        outputGA(backtrack, str1, str2, i, j-1)
        out1.append("-")
        out2.append(str2[j-1])

        
outputGA(backtrack, str1, str2, str1_len, str2_len)

print "".join(out1)
print "".join(out2)
