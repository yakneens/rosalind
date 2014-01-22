import re
import cProfile
'''
myFilename = "/Users/siakhnin/Downloads/dataset_101_6 (1).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''

inputstr = """smnpbnnaaaaa$a
ana"""
inputstr = """TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
     CCT CAC GAG CAG ATC"""
inputstr = """TC$AATTTCGCGGGGGTAAG
ATCG"""

input_list = inputstr.split("\n")
my_bwt = input_list[0].strip()

my_patterns = input_list[1].strip().split(" ")

my_match = re.search("\$",my_bwt)
if my_match:
    string_end = ("$", my_match.start())

input_len = len(my_bwt)

last_col = zip(my_bwt, range(input_len))
first_col = sorted(last_col)


my_alphabet = ['A','C','G','T', '$']

first_col_str = "".join([l[0] for l in first_col])

first_occurrence = {}
for letter in my_alphabet:
    first_occurrence[letter] = re.search(letter, first_col_str).start()

#print first_occurrence

counts = {let:[0] for let in my_alphabet}
for i,c in enumerate(my_bwt):
    for l in counts:
        if c == l:
            counts[l].append(counts[l][i] + 1)
        else:
            counts[l].append(counts[l][i])
#print counts

def countMatches(my_pattern):

    #Range for search
    top = 0
    bottom = input_len - 1
    
    for c in my_pattern[::-1]:
        #First occurrence of c in search range
        first_match = re.search(c,my_bwt[top:bottom+1])
        
        if first_match:
            first_c = first_occurrence[c]
            top = first_c + counts[c][top]
            bottom = first_c + counts[c][bottom+1] - 1
            
            '''top_index = first_match.start()
            
            #Last occurrence of c in search range
            last_match = re.search(r"" + c + "[^"+c+"]*$", my_bwt[top:bottom+1])
            
            if last_match:
                bottom_index = last_match.start()
                
                last_top = top
                
                #Compute new search range based on looking up last column indexes in the
                #first column
                top =  first_index[(c,last_top + top_index)]
                bottom = first_index[(c,last_top + bottom_index)]'''
        #There is a character mismatch
        else:
            return 0
                
    #Number of matches = size of search range after all characters exhausted            
    return bottom - top + 1

for my_pattern in my_patterns:
    print countMatches(my_pattern),