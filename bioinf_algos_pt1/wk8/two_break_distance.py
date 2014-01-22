import re

myFilename = "/Users/siakhnin/Downloads/dataset_89_1 (3).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """(+1 +2 +3 +4 +5 +6)
     (+1 -3 -6 -5)(+2 -4)"""
'''

input_list = inputstr.split("\n")

# Adds edges in both directions to a dictionary
def parseEdges(my_input):
    sub_graphs = my_input.split(")(")
    my_dict = {}
    for my_graph in sub_graphs:     
        matches = re.findall('[\+\-][0-9]*', my_graph)
        
        for i,m in enumerate(matches):
            from_node = 0
            to_node = 0
            if i == 0:
                from_node = int(matches[-1])
                to_node = int(matches[i])           
            else:
                from_node = int(matches[i-1])
                to_node = int(matches[i])
                
            my_dict[from_node] = -to_node
            my_dict[-to_node] = from_node
        #print my_list
    return my_dict

p = parseEdges(input_list[0])
q = parseEdges(input_list[1])

#Number of synteny blocks
num_blocks = len(p)

#Initialize the counter of cycles
cycle_count = 0

#Get the first edge (and pop its reverse)
a_edge = p.popitem()
p.pop(a_edge[1])

#Remember where the cycle started
cycle_start = a_edge[0]

#a and b are used to swap p and q on each iteration
a = p
b = q

while len(p) > 0 or len(q) > 0:
    #This is the next edge
    b_edge = (a_edge[1], b.pop(a_edge[1]))
    b.pop(b_edge[1])
    
    #If we are back at the cycle start
    if b_edge[1] == cycle_start:
        
        cycle_count+= 1
        
        #If there are more edges, get the next one (beginning of a new cycle)
        if len(b) > 0:
            a_edge = b.popitem()
            b.pop(a_edge[1])
            cycle_start = a_edge[0]
    else:
        a_edge = b_edge

    #Swap a and b
    if b == p:
        b = q
        a = p
    else:
        b = p
        a = q
  # 2-break distance = number of blocks - number of cycles  
print (num_blocks/2) - cycle_count  
              
    
    
