import math as m


myFilename = "/Users/siakhnin/Downloads/rosalind_lia (2).txt"

f = open(myFilename, 'r')
inputstr = f.read()


'''
inputstr = """2 1"""
'''

input_list = inputstr.split(" ")

#Num generations
k = int(input_list[0].strip())

#Num organisms
n = int(input_list[1].strip())

offspring_at_k = 2**k

prob_of_het = 0.5**2

cum_prob = 0
for i in range(0,n):
    n_choose_i = m.factorial(offspring_at_k)/(m.factorial(i)*m.factorial(offspring_at_k-i))
    cum_prob += n_choose_i * (prob_of_het**i) * ((1-prob_of_het)**(offspring_at_k-i))

#generational_prob = 1 - cum_prob

#probability of at least n offspring with aA in first generation
print 1 - cum_prob