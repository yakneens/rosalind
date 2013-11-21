
#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_20_3 (3).txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """LEQN"""
inputstr = """IAQMLFYCKVATN"""
'''
strlen = len(inputstr)
theoretical_spectrum = []
amino_acid_weights = {'A':71,'D':115,'V':99,'G':57,'E':129,'I':113,'M':131,'T':101,'N':114,'K':128,'S':87,'R':156,'F':147,'L':113,'P':97,'H':137,'Q':128,'Y':163,'C':103,'W':186}

def generateAllSubPeptides():
    global inputstr
    
    for i in range(0,strlen):
        for j in range(1,strlen):
            yield(inputstr[0:j])
        inputstr = inputstr[1:] + inputstr[0]
    
def generateTheoreticalSpectrum():
    for p in generateAllSubPeptides():
        #print(p)
        theoretical_spectrum.append((p,sum([amino_acid_weights[c] for c in p])))
        
    theoretical_spectrum.append(([],0))    
    theoretical_spectrum.append((inputstr,sum([amino_acid_weights[c] for c in inputstr])))
        
generateTheoreticalSpectrum()

for seq, weight in sorted(theoretical_spectrum, key=lambda tup: tup[1]):
    print(weight),


