import sys

myFilename = "/Users/siakhnin/Downloads/dataset_71_8.txt"

f = open(myFilename, 'r')
inputstr = f.read()

'''
inputstr= """40
     50,25,20,10,5,1"""
'''     
input_list = inputstr.split("\n")

total = int(input_list[0].strip())
denominations = [int(x.strip()) for x in input_list[1].split(",")]
min_num_coins = []

min_num_coins = (total+1) * [None]
min_num_coins[0] = 0

for m in range(1,total+1):
    min_num_coins[m] = sys.maxint
    for i in range(0,len(denominations)):
        if m >= denominations[i]:
            if min_num_coins[m - denominations[i]] + 1 < min_num_coins[m]:
                min_num_coins[m] = min_num_coins[m - denominations[i]] + 1
                
print min_num_coins[-1]

