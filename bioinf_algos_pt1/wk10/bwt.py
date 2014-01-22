'''
myFilename = "/Users/siakhnin/Downloads/dataset_97_4 (1).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """GCGTGCCTGGTCA$"""
inputstr = """panamabananas$"""

input_len = len(inputstr)

first_and_last = [(i, c, inputstr[i-1]) for i,c in enumerate(inputstr)]
tran = sorted(first_and_last, key=lambda(x): ''.join((inputstr[x[0]:],inputstr[:input_len-x[0]-1])))
print ''.join([x[2] for x in tran])