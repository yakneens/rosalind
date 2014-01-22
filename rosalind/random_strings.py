import numpy as np
from collections import Counter

myFilename = "/Users/siakhnin/Downloads/rosalind_prob.txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783"""
'''
input_list = inputstr.split('\n')

pattern=input_list[0]
arr_list = [float(item) for item in input_list[1].split(" ")]

gc_vals = np.array(arr_list)
at_vals = 1 - gc_vals


prob_gc = np.log10(gc_vals / 2)
prob_at = np.log10(at_vals / 2)

my_counter = Counter(pattern)

outcomes = (my_counter['A'] + my_counter['T']) * prob_at + (my_counter['G'] + my_counter['C']) * prob_gc

print " ".join([str(outcome) for outcome in outcomes])