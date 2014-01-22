
myFilename = "/Users/siakhnin/Downloads/dataset_96_6 (5).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()
f = open('suffix_tree_from_suffix_array.out', 'w') 
'''
inputstr = """GTAGT$
     5, 2, 3, 0, 4, 1
     0, 0, 0, 2, 0, 1"""
inputstr = """panamabananas$
13, 5, 3, 1, 7, 9, 11, 6, 4, 2, 8, 10, 0, 12
0, 0, 1, 1, 3, 3, 1, 0, 0, 0, 2, 2, 0, 0""" 
 '''    
input_list = inputstr.split("\n")

my_string = input_list[0].strip()
suffix_array = [int(x) for x in input_list[1].strip().split(", ")]
lcp_array = [int(x) for x in input_list[2].strip().split(", ")]
print my_string, suffix_array, lcp_array
result_list = []

for i, val in enumerate(lcp_array):
    if val == 0:
        result_list.append(my_string[suffix_array[i]:])
        print "Current suffix is: " + my_string[suffix_array[i]:]
    else:
        print "Current suffix is: " + my_string[suffix_array[i]:]
        lastval = result_list.pop(-1)
        
        if lastval[-1] == '$':
            split_val = lastval[:val]
            result_list.append(lastval[val:])
            result_list.append(my_string[suffix_array[i] + val:])
            result_list.append(split_val)
        else:
            cur_overlap = val
            tmp_list = [lastval]
            while cur_overlap > 0:
                if cur_overlap > len(lastval):
                    cur_overlap -= len(lastval)
                    lastval = result_list.pop(-1)
                    tmp_list.append(lastval)
                elif cur_overlap == len(lastval):
                    result_list.append(my_string[suffix_array[i] + val:])
                    result_list.extend(tmp_list[::-1])
                    break
                else:
                    tmp_list.pop(-1)
                    result_list.append(lastval[cur_overlap:])
                    result_list.append(my_string[suffix_array[i] + val:])
                    result_list.append(lastval[:cur_overlap])
                    result_list.extend(tmp_list[::-1])
                    break
            
#print result_list
#print "\n".join(result_list)         
f.write("\n".join(result_list))