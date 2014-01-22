import re
import cProfile
'''
myFilename = "/Users/siakhnin/Downloads/dataset_103_4.txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''


inputstr = """panamabananas
ana"""
inputstr = """AATCGGGTTCAATCGGGGT
     ATCG
     GGGT"""


input_list = inputstr.split("\n")

my_original_string = input_list[0].strip() + "$"
print my_original_string

def getBWT(input_string):
    first_and_last = [(i, c, input_string[i-1]) for i,c in enumerate(input_string)]
    tran = sorted(first_and_last, key=lambda(x): ''.join((input_string[x[0]:],input_string[:len(input_string)-x[0]-1])))
    return ''.join([x[2] for x in tran])

my_bwt = getBWT(my_original_string)
print my_bwt


my_patterns = [x.strip() for x in input_list[1:]]

my_match = re.search("\$",my_bwt)
if my_match:
    string_end = ("$", my_match.start())

input_len = len(my_bwt)

last_col = zip(my_bwt, range(input_len))
first_col = sorted(last_col)
first_to_ind = dict(zip(first_col, range(input_len)))

last_to_first = dict(zip(last_col, first_col))

my_alphabet = ['A','C','G','T', '$']

first_col_str = "".join([l[0] for l in first_col])
print first_col_str

first_occurrence = {}
for letter in my_alphabet:
    first_occurrence[letter] = re.search(letter, first_col_str).start()

def getOccurrenceCounts(my_bwt_str, C):
    counts = {let:[0] for let in my_alphabet}
    cur_vals = {let:0 for let in my_alphabet}
    for i,c in enumerate(my_bwt_str):
        for l in counts:
            if c == l:
                cur_vals[l] += 1            
                if (i + 1) % C == 0:
                    counts[l].append(cur_vals[l])
            else:
                if (i + 1) % C == 0:
                    counts[l].append(cur_vals[l])
    return counts

C = 5
counts = getOccurrenceCounts(my_bwt, C)

def getCount(let, pos, counts, C, my_bwt):
    row_ind = int(pos / C)
    
    cur_count = counts[let][row_ind]
    my_ind = row_ind * C
    while my_ind < pos:
        if my_bwt[my_ind] == let:
            cur_count += 1
        
        my_ind += 1
        
    return cur_count

def getPartialSuffixArray(original_string, k):
    my_suffix_array = {}
    new = sorted((input_len - i - 1 for i in range(input_len)), key=lambda(x): original_string[x:])

    for i,v in enumerate(new):
        if v % k == 0:
            my_suffix_array[i] = v
    
    return my_suffix_array
    
k = 1
partial_suff_array = getPartialSuffixArray(my_original_string, k)

def getMatchIndex(match_pos):
    offset = 0
    cur_pos = match_pos
    while not partial_suff_array.get(cur_pos):
        offset += 1
        cur_pos = first_to_ind[(my_bwt[cur_pos], cur_pos)]
        #last_val = 

    return cur_pos + offset    

answers = []

def countMatches(my_pattern):

    #Range for search
    top = 0
    bottom = input_len - 1
    
    for c in my_pattern[::-1]:
        #First occurrence of c in search range
        first_match = re.search(c,my_bwt[top:bottom+1])
        
        if first_match:
            first_c = first_occurrence[c]
            top = first_c + getCount(c, top, counts, C, my_bwt)
            bottom = first_c + getCount(c, bottom+1, counts, C, my_bwt) - 1
            
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
        
                
    for r in range(top, bottom + 1):
        match_index = getMatchIndex(r)
        answers.append(partial_suff_array.get(match_index))
        
    #Number of matches = size of search range after all characters exhausted            
    return bottom - top + 1

for my_pattern in my_patterns:
    countMatches(my_pattern)
    
print " ".join([str(a) for a in answers])