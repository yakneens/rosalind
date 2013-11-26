import re


myFilename = input("Eneter filename:")

f = open(myFilename, 'r')
x = f.readline().strip()
y = f.readline().strip()

z = re.finditer('(?=(' + y + '))',x)

my_str = ''
for w in z:
    
    my_str += str(w.start() + 1) + " "
print(my_str)