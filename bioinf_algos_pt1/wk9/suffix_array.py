'''

myFilename = "/Users/siakhnin/Downloads/dataset_96_3 (2).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''

inputstr = """AACGATAGCGGTAGA$"""
inputstr = """panamabananas$"""
input_len = len(inputstr)

f = open('suffix_array.out', 'w') 
new = sorted((input_len - i - 1 for i in range(input_len)), key=lambda(x): inputstr[x:])
print new
f.write(", ".join([str(x) for x in new]))

