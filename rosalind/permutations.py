
import itertools as it


myFilename = "/Users/siakhnin/Downloads/rosalind_perm.txt"

f = open(myFilename, 'r')
input_str = int(f.read())

'''
input_str = int("""3""")
'''

perms = it.permutations(range(input_str))
a = [list(map(lambda y: y + 1,x)) for x in perms]
y = map(str, a)
print len(a)
for i in a:
    print " ".join(map(str,i))

