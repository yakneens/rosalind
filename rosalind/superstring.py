from Bio import SeqIO
from collections import Counter
import re
import copy
import cProfile

read_list = []

for seq_record in SeqIO.parse('/Users/siakhnin/Downloads/rosalind_super.txt', 'fasta'):
    read_list.append(str(seq_record.seq))
    

# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]


def buildGraph(dna_reads):
    adj_dict = {}
    print len(dna_reads)
    for read in dna_reads:
        for kmer in allKmersOf(read, (len(read) / 2)):         
            adj_dict.setdefault(kmer[:-1], []).append(kmer[1:])
    
    return adj_dict



adj_dict = buildGraph(read_list)

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
    print "Unbalanced edges ", len([val for val in edge_counts.values() if val[0] != val[1]])            
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
    for read in reads[1:]:
        dna_string += read[-1]
    
    return dna_string
def doIt():
    graph = completeCycle(adj_dict)
    cycle_list = eulerCycle(graph,unexplored_nodes)[:-1]
    print reconstructFromReads(cycle_list)
    
    
    
cProfile.run('doIt()')

'''
def chopInHalf(my_str):
    str_len = len(my_str)
    return my_str[:(str_len / 2)], my_str[(str_len/2):]

edges = {}

for i,read in enumerate(read_list):
    v1, v2 = chopInHalf(read)
    edges.setdefault(v1,[]).append(i)
    edges.setdefault(v2,[]).append(i)

def setAlignment(i, my_read, match):
    
    pref = my_read[:match.end()]
    suff = my_read[match.start():]
    for j in i:
        another_read = read_list[j]
        if another_read[-1 * len(pref):] == pref:
            print 'pref_match %s', another_read, pref, another_read + my_read[len(pref):]
        elif another_read[:len(suff)] == suff:
            print 'suff match %s', another_read, suff, my_read + another_read[len(suff):]
        
    return 

for key in edges.keys():
    for i,read in enumerate(read_list):
        if i not in edges[key]:
            m = re.search(key, read)
        
            if m:
                setAlignment(edges[key], read, m)
        
print edges'''