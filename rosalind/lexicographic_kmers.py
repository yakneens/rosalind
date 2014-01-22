import itertools as it
import operator as op

myFilename = "/Users/siakhnin/Downloads/rosalind_lexf.txt"

f = open(myFilename, 'r')
inputstr = f.read()
'''
inputstr = """T A G C
2"""
'''
input_list = inputstr.split("\n")

alpha=input_list[0].split(" ")
alpha_dict = {}
for i,a in enumerate(alpha):
    alpha_dict[a] = str(i+1)
    
#alpha_dict = {'T':'1','A':'2','G':'3','C':'4'}
str_len = int(input_list[1].strip())

def strToNum(my_str):
    return int("".join([alpha_dict[x] for x in my_str]))
    
my_strings =  [x for x in it.product(alpha,repeat=str_len)]
my_records = []
for tup in my_strings:
    my_str = "".join(tup)
    my_records.append((my_str, strToNum(my_str)))
my_sorted_records = sorted(my_records, key=op.itemgetter(1)) 

print "\n".join([x[0] for x in my_sorted_records])