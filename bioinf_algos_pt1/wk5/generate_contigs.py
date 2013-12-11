import copy
import cProfile


myFilename = "/Users/siakhnin/Downloads/dataset_59_5.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ATG
     ATG
     TGT
     TGG
     CAT
     GGA
     GAT
     AGA"""
''' 
dna_reads = [x.strip() for x in inputstr.split("\n")]
adj_dict = {}
global unexplored_nodes
unexplored_nodes = []

def generateGraph(dna_reads):
    graph = {}
    for kmer in dna_reads:
        graph.setdefault((kmer[:-1]),[]).append(kmer[1:])

    return graph




#Finds two semi-balanced nodes in the graph and connects them to allow an Euler cycle to be created.
def buildStartnodesList(graph):
    edge_counts = {}
    start_nodes = []
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
        
        if in_count == 0 or out_count > 1 or in_count > 1:
            start_nodes.append(v)
            
    return start_nodes, edge_counts


def buildContigs(graph, start_nodes, edge_counts):
    
    my_contigs = []
    
    
    for start_node in start_nodes:
        current_contig = []
        current_contig.append(start_node)
    
        neighbours = graph.get(start_node)
        
        for n in neighbours:
            current_contig = []
            current_contig.append(start_node)
            cur_node = n
            while True:
                current_contig.append(cur_node)
                
                current_counts = edge_counts[cur_node]
                
                if current_counts[0] == 0 or current_counts[0] > 1 or current_counts[1] > 1:
                    break
                else:
                    #graph.pop(cur_node)
                    #edge_counts.pop(cur_node)
                        cur_node = graph[cur_node][0]
                
            
            my_contigs.append(current_contig)
    
    # Return both the created cycle and the start node for the next cycle
    return my_contigs

def reconstructFromReads(reads):
    dna_string = reads[0]
    for read in reads[1:]:
        dna_string += read[-1]
    
    return dna_string


def doIt():
    graph = generateGraph(dna_reads)
    start_nodes, edge_counts = buildStartnodesList(graph)
    contig_list = sorted([reconstructFromReads(x) for x in buildContigs(graph, start_nodes, edge_counts)])
    
    print "\n".join(contig_list)
    
    
    
cProfile.run('doIt()')