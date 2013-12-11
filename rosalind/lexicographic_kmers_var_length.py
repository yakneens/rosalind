import itertools as it
import operator as op

myFilename = "/Users/siakhnin/Downloads/rosalind_lexv (4).txt"

f = open(myFilename, 'r')
inputstr = f.read()
'''
inputstr = """D N A
3"""
'''
input_list = inputstr.split("\n")

alpha=input_list[0].split(" ")
alpha_dict = {}
for i,a in enumerate(alpha):
    alpha_dict[a] = str(hex(i+1))[2:]
    
#alpha_dict = {'T':'1','A':'2','G':'3','C':'4'}
str_len = int(input_list[1].strip())
my_strings = []
for i in range(str_len):
    j = i + 1
    my_strings.extend([x for x in it.product(alpha,repeat=j)])
    

def strToNum(my_str):
    return int("".join([alpha_dict[x] for x in my_str]))

def strToNumVarLength(my_str):    
    num_list = [alpha_dict[x] for x in my_str]
    l = len(num_list)
    num_list.extend('0'*(str_len - l))
    return int("".join(num_list),16)
my_records = []
for tup in my_strings:
    my_str = "".join(tup)
    my_records.append((my_str, strToNumVarLength(my_str)))
my_sorted_records = sorted(my_records, key=op.itemgetter(1)) 

f = open('lexicographic_kmers.out', 'w')
f.write("\n".join([x[0] for x in my_sorted_records]))
print "\n".join([x[0] for x in my_sorted_records])