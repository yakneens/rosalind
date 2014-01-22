import numpy as np
import re

myFilename = "/Users/siakhnin/Downloads/dataset_87_2 (3).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = "(-3 +4 +1 +5 -2)"
'''

matches = re.findall('[\+\-][0-9]*',inputstr)
  
x = np.array([int(m) for m in matches])
x_map = {abs(z):i for i,z in enumerate(x)}

sort_dist = 0
y = np.array(x)

def reverseAndNegate(my_list, offset):
    list_len = len(my_list)
    for i in range(list_len/2):
        temp = my_list[i]
        my_list[i] = -my_list[-i-1]
        x_map[abs(my_list[i])] = i + offset
        my_list[-i-1] = -temp
        x_map[abs(my_list[-i-1])] = offset + len(my_list)-i-1
    
    if list_len % 2 != 0:
        my_list[list_len / 2] *= -1
    
    return my_list
f = open('greedy_sort.out', 'w')

for i,k in enumerate(y):
    if abs(k) != i + 1:
        new_ind = x_map[i+1]
        reverseAndNegate(y[i:new_ind+1], i)
        sort_dist += 1
        f.write("(" + " ".join(["%+d" % j for j in y]) + ")\n") 
    
    if y[i] < 0:
        y[i] *= -1
        sort_dist += 1
        f.write("(" + " ".join(["%+d" % j for j in y]) + ")\n") 
    