import re

myFilename = "/Users/siakhnin/Downloads/dataset_99_10.txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = """TTCCTAACG$A"""
'''
my_match = re.search("\$",inputstr)
if my_match:
    string_end = ("$", my_match.start())

input_len = len(inputstr)

last_col = zip(inputstr, range(input_len))
first_col = sorted(last_col)

last_to_first = dict(zip(last_col, first_col))

cur_val = last_to_first[string_end]
my_string = list(cur_val[0])

while cur_val != string_end:
    cur_val = last_to_first[cur_val]
    my_string.append(cur_val[0])

print "".join(my_string)