'''
myFilename = "/Users/siakhnin/Downloads/dataset_52_7 (1).txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ATGCG
     GCATG
     CATGC
     AGGCA
     GGCAT"""

dna_reads = sorted([x.strip() for x in inputstr.split("\n")])
num_reads = len(dna_reads)
read_length = len(dna_reads[0])

def listBasedGraph():
    suff_dict = {tuple(read[1:]):i for i,read in enumerate(dna_reads)}
    answer = {}
    for i,read in enumerate(dna_reads):
        pref = tuple(read[:-1])
        if pref in suff_dict:
            answer.setdefault(dna_reads[suff_dict[pref]], []).append(read)
    
    ans_list = []
    for key in answer:
        if key != "":
            ans_list.append(key + " -> " + ", ".join(answer[key]))
        
    return ans_list
final = listBasedGraph()
f = open('overlap_graph.out', 'w')
f.write("\n".join(sorted(final)))
