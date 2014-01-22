
myFilename = "/Users/siakhnin/Downloads/rosalind_tree (7).txt"

f = open(myFilename, 'r')
inputstr = f.read()
'''
inputstr = """10
1 2
2 8
4 10
5 9
6 10
7 9"""
'''

input_list = [x.strip() for x in inputstr.split("\n")]
adj_dict = {}
num_nodes = int(input_list[0].strip())
component_mapping = {}

# parse input into a dictionary that stores the adjacency list
for my_str in input_list[1:]:
    if len(my_str) > 0:
        rec = my_str.split(" ")
        key = int(rec[0].strip())
        vertex1 = int(rec[0].strip())
        vertex2 = int(rec[1].strip())
        adj_dict[vertex1] = vertex2
        
num_edges = len(adj_dict.keys())
print num_nodes - len(input_list[1:])       

#ALL THE STUFF BELOW IS NOT NEEDED
component_number = 1
bak = dict(adj_dict)
v1,v2 = adj_dict.popitem()
component_mapping[v1] = component_number

while len(adj_dict) > 0:
    
    if adj_dict.get(v2) != None:
        v1 = v2
        v2 = adj_dict[v1]
        adj_dict.pop(v1)
        component_mapping[v1] = component_number
        component_mapping[v2] = component_number
    else:    
        v1,v2 = adj_dict.popitem()
        
        if v2 not in component_mapping.keys():
            component_number += 1
            component_mapping[v1] = component_number
            component_mapping[v2] = component_number
        else:
            component_mapping[v1] = component_mapping[v2]    

num_seen_nodes = len(component_mapping.keys())

# This takes care of nodes that have no connections and are thus not in the adjacency list  
if num_seen_nodes < num_nodes:
    component_number += (num_nodes - num_seen_nodes)  
