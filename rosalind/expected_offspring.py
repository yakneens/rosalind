import re
import collections
from numpy import *



myFilename = "/Users/siakhnin/Downloads/rosalind_iev (1).txt"

f = open(myFilename, 'r')
input_str = f.read()

'''
input_str = """1 0 0 1 0 1"""
'''

num_offspring = [int(x.strip()) for x in input_str.split(" ")]

'''Probability of dominant phenotype in offspring of the following genotype combination parents - 
AA-AA,AA-Aa,AA-aa,Aa-Aa,Aa-aa,aa-aa '''
prob_dominant = [1, 1, 1, 0.75, 0.5, 0]


print sum(map(lambda x,y: x*y, num_offspring, prob_dominant)) * 2