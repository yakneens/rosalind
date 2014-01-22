import numpy as np
import re

myFilename = "/Users/siakhnin/Downloads/dataset_88_1 (1).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = "(-3 +4 +1 +5 -2)"
inputstr = "(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)"
'''

matches = re.findall('[\+\-][0-9]*',inputstr)

input_list = [0]
[input_list.append(int(m)) for m in matches]
input_list.append(len(matches)+1) 
x = np.array(input_list)
breakpoint_count = 0

for i in range(0, len(input_list)-1):
    cur = input_list[i]
    next_val = input_list[i+1]
    if cur >= 0 and not next_val - 1 == cur:
        breakpoint_count += 1
    elif cur < 0 and not next_val - 1 == cur:
        breakpoint_count += 1
   
    
print breakpoint_count