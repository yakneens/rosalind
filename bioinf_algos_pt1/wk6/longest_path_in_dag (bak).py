import numpy as np
import re
from collections import OrderedDict
'''    
myFilename = "/Users/siakhnin/Downloads/dataset_74_7.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr = """ 3
     4
     3->1:7
     3->2:4
     1->4:1
     0->4:3
     2->0:2"""
 
input_list = inputstr.strip().split("\n")
source = int(input_list[0].strip())
sink = int(input_list[1].strip())


my_graph = np.zeros((sink+1,sink+1))
path_mat = np.zeros((sink+1, sink+1))

for i in input_list[2:]:
    my_edge = [int(x.strip()) for x in re.split(r"->|:", i)]
    my_graph[my_edge[0], my_edge[1]] = my_edge[2]

my_graph_copy = np.array(my_graph)
my_graph_permutation = np.zeros((sink+1,sink+1))
s = set()
s.add(source)
perm = OrderedDict()
while len(s) > 0:
    el = s.pop()
    perm[el] = None
    for i in range(0, sink+1):
        my_graph_copy[el,i] = 0
        if max(my_graph_copy[:,i]) == 0 and i not in perm:
            s.add(i)
print perm
for i,j in enumerate(perm.keys()):
    my_graph_permutation[:,i] = my_graph[:,j]

print "My graph - \n", my_graph
print "Permuted graph \n", my_graph_permutation
    
path_mat = np.array(my_graph_permutation)    
    
for i in range(0,sink+1):
    for j in range (0, sink + 1):
        if path_mat[j,i] > 0:
            max_pred = max(path_mat[:,j])
            path_mat[j,i] = max(path_mat[:,j]) + path_mat[j,i]
print my_graph
print path_mat    

j = np.argmax(path_mat[:,-1])
print int(path_mat[j,-1])
result = [perm.keys()[-1]]
while j != source:
    result.append(perm.keys()[j])
    j = np.argmax(path_mat[:,j])
    
result.append(source)

print "->".join([str(x) for x in result[::-1]])    
    