myFilename = "/Users/siakhnin/Downloads/rosalind_lgis.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr = """5
5 1 4 2 3"""
'''

input_list = inputstr.split('\n')

len_seq = int(input_list[0])
seq = [int(x.strip()) for x in input_list[1].split(" ")]

active_list = []
active_list_decr = []

prev_els_decr = len_seq * [None]
prev_els = len_seq * [None]


active_list.append(0)
largest_length = 1
prev_els[0] = 0

active_list_decr.append(0)
largest_length_decr = 1
prev_els_decr[0] = 0

for i in range(1, len(seq)):
    #j = findActiveList(i)
    
    j = len(active_list_decr) - 1
    while seq[active_list_decr[j]] <= seq[i] and j >= 0:
        j -= 1
    
    prev_els_decr[i] = active_list_decr[j]
        
    if j < 0:
        active_list_decr[0] = i
    elif j == len(active_list_decr) - 1:
        active_list_decr.append(i)
        largest_length_decr +=1
    else:
        active_list_decr[j+1] = i
    
    
    j = len(active_list) - 1
    while seq[active_list[j]] >= seq[i] and j >= 0:
        j -= 1
    
    prev_els[i] = active_list[j]
        
    if j < 0:
        active_list[0] = i
    elif j == len(active_list) - 1:
        active_list.append(i)
        largest_length +=1
    else:
        active_list[j+1] = i
    
        
        

results = []
results.append(seq[active_list[largest_length-1]])
ind = active_list[largest_length - 1]
for i in range(largest_length-1, 0, -1):
    ind = prev_els[ind]
    results.append(seq[ind])


results_decr = []
results_decr.append(seq[active_list_decr[largest_length_decr-1]])
ind = active_list_decr[largest_length_decr - 1]
for i in range(largest_length_decr-1, 0, -1):
    ind = prev_els_decr[ind]
    results_decr.append(seq[ind])    

print " ".join([str(x) for x in results[::-1]]) 
print " ".join([str(x) for x in results_decr[::-1]])    
            