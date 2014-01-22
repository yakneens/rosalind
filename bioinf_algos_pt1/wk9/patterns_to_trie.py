from node import Trie

myFilename = "/Users/siakhnin/Downloads/dataset_93_3 (2).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = """GGTA
     CG
     GGC"""
'''     
input_list = [my_str.strip() for my_str in inputstr.split("\n")]

my_trie = Trie('')
my_trie.initFromStrings(input_list)
        

