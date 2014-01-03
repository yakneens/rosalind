import numpy as np
import sys
import re
import cProfile

sys.setrecursionlimit(10000)

myFilename = "/Users/siakhnin/Downloads/dataset_79_14 (9).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """PLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLYPLEASANTLY
     MEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLYMEANLY"""
inputstr = """Y
YV"""
inputstr = """PLEASANTLY
MEANLY"""
'''
# Parse the two input strings
input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)
str2 = input_list[1].strip()
str2_len = len(str2)
print str1
print str2
# Set up the BLOSUM scoring matrix
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
sigma = -5

edge_list = []

# Look up cost of letters c1 and c2 based on the scoring matrix
def getCost(c1, c2):
    return z[aa_ind_map[c1], aa_ind_map[c2]]



# Return scores at column ind of the alignment, these represent the length of the alignment path up to that point
def computeScoresAt(ind, str1 ,str2):
    
    str1_len = len(str1)
    str2_len = len(str2)
    
    #s has two columns, the column currently being computed and the previous column
    s = np.zeros((str1_len+1,2))
    
    #Backtrack keeps track of which direction we are coming into the current node from
    backtrack = np.zeros((str1_len+1))
    
    #Init first column with indel costs
    s[:,0] = np.arange(str1_len+1).T * sigma
    
    backtrack[0] = 2
    
    #Inner loop iterates over rows and outer over columns
    for j in range(1, ind + 1):
        #Init the first row with the indel cost for that point in the string 
        s[0,1] = j * sigma
        
        for i in range(1, str1_len+1):
            
            #Cost of a diagonal move that consumes 1 character from each string
            diag = s[i-1,0] + z[aa_ind_map[str1[i-1]], aa_ind_map[str2[j-1]]]
            
            #Pick max cost between diagonal, downward or rightward moves
            s[i,1] = max(diag,s[i-1,1] + sigma, s[i,0] + sigma)
            
            #print "Vals",diag,s[i-1,1] + sigma, s[i,0] + sigma
            #Backtrack remembers the decision we made - 0 for diagonal move, 1 for vertical move, 2 for horizontal move  
            x = 0
            if s[i-1,1] + sigma > diag and s[i-1,1] + sigma > s[i,0] + sigma:
                x = 1
            elif s[i,0] + sigma > diag and s[i,0] + sigma > s[i-1,1] + sigma:
                x = 2
            
            backtrack[i] =  x
            
            
        # Once all rows are processed, copy column 1 into column 0 to prepare for the next iteration.   
        s[:,0] = s[:,1]  
        
    #We return only the first column (which contains the final result) and the backtrack vector    
    return s[:,0], backtrack


    
def computeMiddleNodeAndEdge(top, bottom, left, right):
    sub1 = str1[top:bottom]
    sub2 = str2[left:right]
    
    sub1_len = len(sub1)
    sub2_len = len(sub2)
     
    # Middle of the second string (i.e. middle column of alignment matrix)
    middle = int(sub2_len / 2)
    
    #Compute alignment up to the middle
    s, b = computeScoresAt(middle, sub1, sub2)
    
    #Compute alignment of the reverse strings up to the middle, 
    #the answers are in reverse to the first alignment as we are aligning from the back 
    s2, b2 = computeScoresAt(sub2_len - middle, sub1[::-1],sub2[::-1])
    
    # This computes Length(i) for all i in the middle column
    # the second vector needs to be reversed to match up the values appropriately
    tot =  s + s2[::-1]
    
    #The row with maximal length path
    max_length_row = np.argmax(tot)
    
    #This is the middle node
    middle_node = (max_length_row, middle)
    
    #The node from which we came to the middle node during the reverse alignment
    #This defines the middle edge.
    back_val = b2[-(max_length_row+1)]
    '''next_node = (0,0)
    if back_val == 0:
        next_node = (max_length_row + 1, middle + 1)
    elif back_val == 2:
        next_node = (max_length_row, middle+1)
    else:
        next_node = (max_length_row + 1, middle)
    
    print sub1
    print sub2
    print s
    print s2'''
    
    return max_length_row, back_val

        
def linearSpaceAlignment(top, bottom, left, right):
    middle = int((left + right) / 2)
    
    if top == bottom:
        if left != right:
            print "here2",left,right
            for i in range(left, right):
                print (top,i), 2
                edge_list.append((top,i,2))
            return
    if left == right:
        if top != bottom:
            print "here",top,bottom
            for i in range(top, bottom):
                edge_list.append((i,middle,1))
        return sigma * (bottom - top)
    
        
    midNode,midEdge = computeMiddleNodeAndEdge(top, bottom, left, right)
    
    midNode = top + midNode
    
    linearSpaceAlignment(top, midNode, left, middle)
    
    print (midNode,middle), midEdge
    edge_list.append((midNode,middle,midEdge))
    
    if midEdge == 2 or midEdge == 0:
        middle = middle + 1
    if midEdge == 1 or midEdge == 0:
        midNode = midNode + 1
    
    linearSpaceAlignment(midNode, bottom, middle, right)
      
#print edge_list

def generateAlignment(edge_list, str1, str2):
    
    out1 = []
    out2 = []
    total_score = 0
    
    i = 0
    j = 0
    for ind,e in enumerate(edge_list):
        if e[2] == 0:
            out1.append(str1[i])
            out2.append(str2[j])
            total_score += getCost(str1[i], str2[j])
            i+=1
            j+=1
            
        elif e[2] == 1:
            out1.append(str1[i])
            out2.append("-")
            total_score += sigma
            i+=1
        elif e[2] == 2:
            out1.append("-")
            out2.append(str2[j])
            total_score += sigma
            j+=1
    return out1, out2, int(total_score) 



def doIt():
    linearSpaceAlignment(0,str1_len,0,str2_len)
    
    out1, out2, total_score = generateAlignment(edge_list, str1, str2)  

    print total_score  
    print "".join(out1)
    print "".join(out2)

cProfile.run('doIt()')
'''    
def computeAlignment2(str1 ,str2):
    
    s = np.zeros((str1_len+1,str2_len+1))
    
    #Init first row and column with indel costs
    s[:,0] = np.arange(str1_len+1).T * sigma
    s[0,:] = np.arange(str2_len+1) * sigma
    
    backtrack = np.zeros((str1_len+1, str2_len+1))
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            
            #Cost of a diagonal move that consumes 1 character from each string
            diag = s[i-1,j-1] + getCost(str1[i-1], str2[j-1])
            
            #Pick max cost between diagonal, downward or rightward moves
            s[i,j] = max(diag,s[i-1,j] + sigma, s[i,j-1] + sigma)
            
            #Remember which move we chose
            backtrack[i,j] = np.argmax([[diag, s[i-1,j] + sigma, s[i,j-1] + sigma]])    
            
    return s, backtrack

s3,backtrack = computeAlignment2(str1, str2)
s4,backtrack2 = computeAlignment2(str1[::-1], str2[::-1])
print s3
print s4
'''