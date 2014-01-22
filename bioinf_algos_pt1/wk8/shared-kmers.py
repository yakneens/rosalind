import cProfile

myFilename = "/Users/siakhnin/Downloads/dataset_90_2.txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
'''
inputstr = """3
     AAACTCATC
     TTTCAAATC"""
'''     
input_list = inputstr.split("\n")
k = int(input_list[0].strip())
str1 = input_list[1].strip()
str2 = input_list[2].strip()
 
def getDNAReverseComplement(dna_str):
    complements = {'A':'T','C':'G','G':'C','T':'A'}
    outstr = ""
    
    for c in dna_str:
        outstr += complements[c]
    
    return outstr[::-1]

# Yield all kmers of string my_str
def allKmersOf(my_str, k):
    if len(my_str) >= k:
        for i in range(0,len(my_str) - k + 1):
            yield my_str[i:i+k]
            
def initKmerCounts(my_str, k, count_dict, with_rev_comp):
    for i in range(0, len(my_str) - k + 1):
        current_kmer = my_str[i:i+k];
        count_dict.setdefault(current_kmer, []).append(i)
        if with_rev_comp:
            rev_comp = getDNAReverseComplement(current_kmer)
            count_dict.setdefault(rev_comp, []).append(i)

        
str1_dict = {}
str2_dict = {}
initKmerCounts(str1,k,str1_dict, False)
initKmerCounts(str2,k,str2_dict, True)
def doIt():
    for my_key in str1_dict:
        val = str1_dict[my_key]
        
        if my_key in str2_dict:
            other_val = str2_dict[my_key]
            for v1 in val:
                for v2 in other_val:
                    print "("+ str(v1) + ", " + str(v2) + ")"
                           
cProfile.run('doIt()')          