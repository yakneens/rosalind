import operator

myFilename = input("Eneter filename:")

f = open(myFilename, 'r')
inputstr = f.read()


inputs = [x.strip() for x in inputstr.split('\n')]

ne = operator.ne
print(sum(map(ne,inputs[0], inputs[1])))

