import copy
import cProfile

myFilename = "/Users/siakhnin/Downloads/dataset_57_2 (1).txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """0 -> 3
     1 -> 0
     2 -> 1,6
     3 -> 2
     4 -> 2
     5 -> 4
     6 -> 5,8
     7 -> 9
     8 -> 7
     9 -> 6"""
'''
input_list = [x.strip() for x in inputstr.split("\n")]
adj_dict = {}
unexplored_nodes = []

# parse input into a dictionary that stores the adjacency list
for my_str in input_list:
    if len(my_str) > 0:
        rec = my_str.split("->")
        key = int(rec[0].strip())
        
        if unexplored_nodes == []:
            unexplored_nodes.append(key)
            
        adj_dict[int(rec[0].strip())] = [int(x.strip()) for x in rec[1].split(",")]

#given a graph and a start node creates and returns a cycle via a random walk 
def createCycle(graph, unexplored_nodes):
    
    my_cycle = []
    cur_node = unexplored_nodes.pop()
    
    #Add first node
    my_cycle.append(cur_node)
    
    #This will be the start node for the next cycle if it is needed
    next_start_node = ""
    
    while True:
        #Unexplored edges of the current node
        neighbours = graph.get(cur_node)
        
        if neighbours != None:
            #Explore this edge by consuming it
            cur_neighbour = neighbours.pop()
            
            #Add the edge to the cycle
            my_cycle.append(cur_neighbour)
            
            #All edges of the current node have been explored so consume the current node
            if len(neighbours) == 0:
                graph.pop(cur_node)
            else:
                #If this node has mode unexplored edges it becomes the candidate for being a
                #start node for the next cycle
                unexplored_nodes.append(cur_node)
            
            #The neighbour becomes the current node for the next iteration        
            cur_node = cur_neighbour
            
        else:
            #IF this node has no neighbours, can't go any further.
            if len(graph) > 0 and graph.get(cur_node):
                graph.pop(cur_node)
            break
    
    # Return both the created cycle and the start node for the next cycle
    return my_cycle, unexplored_nodes

#Merges two cycles created in separate runs of createCycle() together
def mergeCycles(cycle1, cycle2):
    index_of = cycle1.index(cycle2[0])
    new_cycle = cycle1[:index_of] + cycle2 + cycle1[index_of+1:]
    return new_cycle


def eulerCycle(graph, unexplored_nodes):
    
    #Create the first cycle
    my_cycle, unexplored_nodes = createCycle(graph, unexplored_nodes)
    
    #The graph is consumed as it is explored so having unexplored edges
    #can be detected by testing if the graph is empty
    has_unexplored_edges = len(graph) > 0
    
    while has_unexplored_edges:
        
        #Create the next cycle
        new_cycle, unexplored_nodes = createCycle(graph, unexplored_nodes)
        
        #Merge the new cycle into my_cycle
        my_cycle = mergeCycles(my_cycle, new_cycle)
        
        has_unexplored_edges = len(graph) > 0
    
    #The final euler cycle is returned
    return my_cycle

def doIt():
    cycle_list = eulerCycle(adj_dict,unexplored_nodes)
    print "->".join([str(x) for x in cycle_list])
    
cProfile.run('doIt()')