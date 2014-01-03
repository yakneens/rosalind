import numpy as np


myFilename = "/Users/siakhnin/Downloads/dataset_77_3.txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """PLEASANTLY
     MEANLY"""
inputstr = """TGCATAT
     ATCCGAT"""
'''

input_list = inputstr.split("\n")     
str1 = input_list[0].strip()
str1_len = len(str1)

str2 = input_list[1].strip()
str2_len = len(str2)

def computeAlignment(str1 ,str2):
    s = np.zeros((str1_len+1,str2_len+1))
    
    s[:,0] = np.arange(str1_len+1)
    s[0,:] = np.arange(str2_len+1)
    
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                s[i,j] = min(s[i-1,j-1],s[i-1,j]+1, s[i,j-1]+1)
            else:
                s[i,j] = min(s[i-1,j-1] + 1, s[i-1,j]+1, s[i,j-1]+1)
                        
    return s

s = computeAlignment(str1, str2)
#print str1_len, str2_len
#print str1
#print str2
#print s
print int(s[str1_len,str2_len])
