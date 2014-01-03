import numpy as np
import re
from collections import OrderedDict
   
myFilename = "/Users/siakhnin/Downloads/dataset_74_7 (5).txt"

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


inputstr = """0
3
0->2:1
2->3:1
1->2:10""" 
 ''' 
 
input_list = inputstr.strip().split("\n")
source = int(input_list[0].strip())
sink = int(input_list[1].strip())
print "\n".join(sorted(input_list[2:]))

my_graph = np.zeros((sink+1,sink+1))
path_mat = np.zeros((sink+1, sink+1))

# Parse input into adjacency matrix
for i in input_list[2:]:
    my_edge = [int(x.strip()) for x in re.split(r"->|:", i)]
    my_graph[my_edge[0], my_edge[1]] = my_edge[2]

print "\n".join(sorted(input_list[2:]))

# This will be destroyed by the topological sort
my_graph_copy = np.array(my_graph)

# Set of nodes with no incoming edges that are safe to add to sort
s = set()
s.add(source)

# Permutation of nodes corresponding to a topological sort fo the DAG
perm = OrderedDict()

'''
new_graph = np.zeros((sink+1, sink+1))

def top_dfs(my_graph, cur):
    if cur == sink:
        perm[cur] = None
        return
    
    neighbours = my_graph[cur,:]
    
    if np.all(my_graph[:,cur] == 0) and cur not in perm:
        perm[cur] = None
        
    for i,n in enumerate(neighbours):
        if n > 0:
            new_graph[cur,i] = my_graph[cur,i]
            my_graph[cur,i] = 0
            top_dfs(my_graph, i)

top_dfs(my_graph_copy, source)
print new_graph
'''
while len(s) > 0:
    #Since el has no incoming edges it is safe to put into perm
    el = s.pop()
    perm[el] = None
    
    #Explore all outgoing edges of el
    for i in range(0, sink+1):
        #Remove edge i
        my_graph_copy[el,i] = 0
        
        #If node i has no incoming edges and is not yet in perm add it to s
        if max(my_graph_copy[:,i]) == 0 and i not in perm:
            s.add(i)

print perm
print "My graph - \n", my_graph

#This array will compute the longest path in topological sort order    
path_mat = np.array(my_graph)    

# j tracks nodes (rows of path_math) in topological order, i tracks edges emanating from j in order    
for i in range(0,sink+1):
    for j in perm.keys():
        if path_mat[j,i] > 0:
            #Edge going from j to i has length path_mat[j,i] plus the longest edge leading into j
            #print path_mat[:,j]
            max_pred = max(path_mat[:,j])
            print np.argmax(path_mat[:,j])
            path_mat[j,i] = max_pred + path_mat[j,i]

print "Path matrix - \n", path_mat
    
perm_list = perm.keys()
j = np.argmax(path_mat[:,perm_list[-1]])

# Visit nodes in reverse order, the path is specified by the index of the node with greatest length edge
print int(path_mat[j,sink])
result = [sink]
while j != source:
    result.append(j)
    j = np.argmax(path_mat[:,j])
    
result.append(source)

print "->".join([str(x) for x in result[::-1]])    
    