import re
import sys
import operator

#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/rosalind_1c.txt"
f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr =  """ ATAT
     GATATATGCATATACTT"""
'''

inputlist = [x.strip() for x in inputstr.split("\n")]
pattern = inputlist[0]
genome = inputlist[1]

z = re.finditer('(?=(' + pattern + '))',genome)

my_str = ''
for w in z:
    
    my_str += str(w.start()) + " "
print(my_str)