import numpy as np

myFilename = "/Users/siakhnin/Downloads/dataset_72_9.txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """4
     4
     1 0 2 4 3
     4 6 5 2 1
     4 4 5 2 1
     5 6 8 5 3
     -
     3 2 4 0
     3 2 4 2
     0 7 3 3
     3 3 0 2
     1 3 2 2"""
'''     
input_list = inputstr.split("\n")
n = int(input_list[0].strip())
m = int(input_list[1].strip())
down = []
right = []
cur_arr = down
for my_str in input_list[2:]:
    if my_str.strip() == "-":
        cur_arr = right
    else:
        cur_arr.append([int(x.strip()) for x in my_str.strip().split(" ")])

down = np.array(down)
right = np.array(right)
s = np.zeros((n+1,m+1))

for i in range(1,n+1):
    s[i,0] = s[i-1,0] + down[i-1,0]

for j in range(1,m+1):
    s[0,j] = s[0, j-1] + right[0,j-1]
    
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i,j] = max(s[i-1,j] + down[i-1,j], s[i, j-1] + right[i,j-1])

print s[n,m]
  

 
