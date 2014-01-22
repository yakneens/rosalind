
import math


myFilename = "/Users/siakhnin/Downloads/rosalind_pper.txt"

f = open(myFilename, 'r')
input_str = f.read()
'''

input_str = """21 7"""
'''

input_list = input_str.split(" ")
p = int(input_list[0].strip())
k = int(input_list[1].strip())

print (math.factorial(p) / math.factorial(p - k)) % 1000000

