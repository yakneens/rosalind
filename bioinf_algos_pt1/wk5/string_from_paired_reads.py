import copy
import cProfile


myFilename = "/Users/siakhnin/Downloads/dataset_58_14 (4).txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """2
     GAGA|TTGA
     TCGT|GATG
     CGTG|ATGT
     TGGT|TGAG
     GTGA|TGTT
     GTGG|GTGA
     TGAG|GTTG
     GGTC|GAGA
     GTCG|AGAT"""
'''

input_list = [x.strip() for x in inputstr.split("\n")]
k = int(input_list[0])

adj_dict = {}
paired_reads_list = []

for line in input_list[1:]:
    if len(line) > 0:
        vals = line.split("|")
        paired_reads_list.append(vals)

global unexplored_nodes
unexplored_nodes = []

def generateGraph(dna_reads):
    graph = {}
    for kmer_pair in dna_reads:
        prefix_list = []
        [prefix_list.append(x[:-1]) for x in kmer_pair]
        suffix_list = []
        [suffix_list.append(x[1:]) for x in kmer_pair]
        
        graph.setdefault(tuple(prefix_list),[]).append(tuple(suffix_list))

    return graph

graph = generateGraph(paired_reads_list)


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

graph = completeCycle(graph)

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
    dna_string = reads[0][0]
    dna_string2 = reads[0][1]
    for read in reads[1:]:
        dna_string += read[0][-1]
        dna_string2 += read[1][-1]
    
    return dna_string + dna_string2[-1 * (k + len(reads[0][0]) + 1):]
def doIt():
    cycle_list = eulerCycle(graph,unexplored_nodes)[:-1]
    
    f = open('string_from_reads.out', 'w')
    my_dna_string = reconstructFromReads(cycle_list)
    
    f.write(my_dna_string)
    print my_dna_string
    
    
    
cProfile.run('doIt()')