
import itertools as it


myFilename = "/Users/siakhnin/Downloads/rosalind_sign (3).txt"

f = open(myFilename, 'r')
input_str = int(f.read())

'''
input_str = int("""3""")
'''
f = open('signed_permutations.out', 'w')

x = range(1, input_str + 1)

ones = list(it.product([1,-1], repeat=input_str))
num_ones = len(ones)

perms = it.permutations(x, input_str)
a = [list(x) for x in perms]
y = map(str, a)
print len(a) * len(ones)
f.write(str(len(a) * len(ones)) + "\n")

for i in a:
    for j in ones:
        f.write(" ".join([str(x*y) for x,y in zip(i, j)]) + "\n")
                #print " ".join(map(str,i))
        #f.write(" ".join(map(str,i)) + "\n")
