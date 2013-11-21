import itertools as it


#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_26_4.txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()


'''
inputstr =  """ 0 137 186 323"""
'''
spectrum = [int(x.strip()) for x in inputstr.strip().split(" ")]

convolution = []
[convolution.append(x[0] - x[1]) for x in it.ifilter(lambda x: x[0] > x[1], it.product(spectrum,repeat=2))]
print(' '.join([str(x) for x in convolution]))