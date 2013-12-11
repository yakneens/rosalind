import copy
import cProfile
import itertools as it
'''
myFilename = "/Users/siakhnin/Downloads/dataset_57_10 (2).txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """40"""

k = int(inputstr.strip())

kmer_list = ["".join(y) for y in it.product('01',repeat=k)]

global unexplored_nodes
unexplored_nodes = []

def generateGraph(kmer_list):
    graph = {}
    for kmer in kmer_list:
        if unexplored_nodes == []:
            unexplored_nodes.append(kmer[:-1])
        
        graph.setdefault((kmer[:-1]),[]).append(kmer[1:])

    return graph

my_graph = generateGraph(kmer_list)    


#Finds two semi-balanced nodes in the graph and connects them to allow an Euler cycle to be created.
def completeCycle(graph):
    edge_counts = {}
    out_edge = None
    in_edge = None
    
    for key in graph:
        vals = graph[key]
        
        if edge_counts.get(key) == None:
            edge_counts[key] = [0,0]
        
        edge_counts[key][0] = len(vals)
        for val in vals:
            if edge_counts.get(val) == None:
                edge_counts[val] = [0,1]
            elif edge_counts.get(val)[1] == "":
                edge_counts[val][1] = 1
            else:
                edge_counts[val][1] +=1
                
    for v in edge_counts:
        out_count = edge_counts[v][0]
        in_count = edge_counts[v][1]
        
        if out_count > in_count:
            out_edge = v 
        elif in_count > out_count:
            in_edge = v
            
    if graph.get(in_edge) == None:
        graph[in_edge] = [out_edge]
    else:
        graph[in_edge].append(out_edge)
    global unexplored_nodes 
    unexplored_nodes = [out_edge]        
    return graph

#given a graph and a start node creates and returns a cycle via a random walk 
def createCycle(graph, unexplored_nodes):
    
    my_cycle = []
    cur_node = unexplored_nodes.pop()
    
    #Add first node
    my_cycle.append(cur_node)
    
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

def reconstructFromReads(reads):
    dna_string = reads[0]
    for read in reads[1:-1*(k-1)]:
        dna_string += read[-1]
    
    return dna_string

def validateOutput(dna_string, k):
    kmers = []
    new_string = dna_string + dna_string[0:k-1]
    for i in range(len(new_string) - k + 1):
        kmers.append(new_string[i:i+k])

    print kmers == kmer_list
    
    return    
def doIt():
    #graph = completeCycle(my_graph)
    cycle_list = eulerCycle(my_graph,unexplored_nodes)
    f = open('unistring.out', 'w')
    my_uc_string = reconstructFromReads(cycle_list)
    validateOutput(my_uc_string,k)
    f.write(my_uc_string)
    print my_uc_string
    
    
#doIt()   
cProfile.run('doIt()')