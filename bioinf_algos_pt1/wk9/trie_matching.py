from node import Trie

myFilename = "/Users/siakhnin/Downloads/dataset_93_6.txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = """AATCGGGTTCAATCGGGGT
     ATCG
     GGGT"""
'''     
input_list = [my_str.strip() for my_str in inputstr.split("\n")]
my_pattern = input_list[0]

my_trie = Trie('')
my_trie.initFromStrings(input_list[1:])

match_hits = {}

def matchPrefixToTrie(my_text, my_trie, start_index):
    cur_node = my_trie
    
    my_match = []
    for (i,c) in enumerate(my_text):
        my_child = cur_node.getChild(c)
        if my_child:
            cur_node = my_child
            my_match.append(c)
        else:
            break
        
        if not cur_node.hasChildren():
            matched_string = my_text[:i+1]
            match_hits.setdefault(matched_string,[]).append(start_index)
            break
        
for i in range(0, len(my_pattern)):
    my_sub = my_pattern[i:]
    matchPrefixToTrie(my_sub, my_trie, i)
    
for my_str in input_list[1:]:
    print " ".join([str(my_match) for my_match in match_hits[my_str]])
    
    
        

