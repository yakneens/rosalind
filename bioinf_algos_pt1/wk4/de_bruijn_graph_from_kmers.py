
myFilename = "/Users/siakhnin/Downloads/dataset_54_7.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """GAGG
     GGGG
     GGGA
     CAGG
     AGGG
     GGAG"""
'''
dna_reads = [x.strip() for x in inputstr.split("\n")]
k = int(len(dna_reads[0]))

def generateGraph(dna_reads):
    graph = {}
    for kmer in dna_reads:
        graph.setdefault((kmer[:-1]),[]).append(kmer[1:])

    return graph

graph = generateGraph(dna_reads)

def prepareForOutput(graph):
    ans_list = []
    for key in graph:
        if key != "":
            ans_list.append(key + " -> " + ",".join(sorted(graph[key])))
    return sorted(ans_list)


f = open('de_bruijn_graph_from_kmers.out', 'w')
f.write("\n".join(prepareForOutput(graph)))
