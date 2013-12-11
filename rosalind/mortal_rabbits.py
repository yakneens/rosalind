import re


myFilename = "/Users/siakhnin/Downloads/rosalind_fibd (4).txt"

f = open(myFilename, 'r')
inputstr = f.read()


'''
inputstr = """12 3"""
'''
input_list = inputstr.split(" ")

num_gen = int(input_list[0].strip())
life_span = int(input_list[1].strip())

#F(n) = F(n-1) + F(n-2) - F(n-m-2)
rabbit_count = list()*num_gen
rabbit_count.append(1)
rabbit_count.append(1)

for i in range(2, num_gen):
    rabbit_count.append(rabbit_count[i-1] + rabbit_count[i - 2])
    
    if(i - life_span + 1 - 2) > 0:
        rabbit_count[i] -= rabbit_count[i-life_span+1-2]
    elif (i - life_span + 1) > 0:
        rabbit_count[i] -= 1
        
print rabbit_count.pop()        