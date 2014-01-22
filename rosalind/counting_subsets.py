
myFilename = "/Users/siakhnin/Downloads/rosalind_sset.txt"

f = open(myFilename, 'r')
inputstr = f.read()
'''

inputstr = """3"""
'''
card = int(inputstr.strip())

base = 2

ans = 1

for i in range(card):
    ans = (ans * base) % 1000000
    
print ans