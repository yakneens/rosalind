import re

'''
myFilename = "/Users/siakhnin/Downloads/dataset_101_6 (1).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''

inputstr = """smnpbnnaaaaa$a
ana"""
inputstr = """TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
     CCT CAC GAG CAG ATC"""

 
input_list = inputstr.split("\n")
my_bwt = input_list[0].strip()

my_patterns = input_list[1].strip().split(" ")

my_match = re.search("\$",my_bwt)
if my_match:
    string_end = ("$", my_match.start())

input_len = len(my_bwt)

last_col = zip(my_bwt, range(input_len))
first_col = sorted(last_col)

#This is the LastToFirst mapping
first_index = dict(zip(first_col, range(input_len)))

last_to_first = dict(zip(last_col, first_col))

def getOriginalString():
    cur_val = last_to_first[string_end]
    my_string = list(cur_val[0])
    while cur_val != string_end:
        cur_val = last_to_first[cur_val]
        my_string.append(cur_val[0])
    return "".join(my_string)

def countMatches(my_pattern):

    #Range for search
    top = 0
    bottom = input_len - 1
    
    for c in my_pattern[::-1]:
        #First occurrence of c in search range
        first_match = re.search(c,my_bwt[top:bottom+1])
        
        if first_match:
            
            top_index = first_match.start()
            
            #Last occurrence of c in search range
            last_match = re.search(r"" + c + "[^"+c+"]*$", my_bwt[top:bottom+1])
            
            if last_match:
                bottom_index = last_match.start()
                
                last_top = top
                
                #Compute new search range based on looking up last column indexes in the
                #first column
                top =  first_index[(c,last_top + top_index)]
                bottom = first_index[(c,last_top + bottom_index)]
        #There is a character mismatch
        else:
            return 0
                
    #Number of matches = size of search range after all characters exhausted            
    return bottom - top + 1
    
for my_pattern in my_patterns:
    print countMatches(my_pattern),