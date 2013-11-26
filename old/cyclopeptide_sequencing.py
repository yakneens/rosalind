from collections import Counter


#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_22_4 (1).txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """ 0 113 128 186 241 299 314 427"""
inputstr = """0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093"""
'''
experimental_spectrum = [int(x.strip()) for x in inputstr.strip().split(" ")]

amino_acid_weights = {'A':71,'D':115,'V':99,'G':57,'E':129,'I':113,'M':131,'T':101,'N':114,'K':128,'S':87,'R':156,'F':147,'L':113,'P':97,'H':137,'Q':128,'Y':163,'C':103,'W':186}

peptides = [[]]

def expandPeptideList(peptide_list):
    candidate_peptides = []
    for pep in peptide_list:
        for amino_acid in amino_acid_weights.keys():
            new_pep = list(pep)
            new_pep.append(amino_acid_weights[amino_acid])
            candidate_peptides.append(new_pep)
    return candidate_peptides

def generateAllSubPeptides(peptide):
    peplen = len(peptide)
    my_list = []
    for i in range(0,peplen):
        for j in range(1,peplen):
            my_list.append(peptide[0:j])
           
        
        first_part_list = list(peptide[1:])
        first_part_list.append(peptide[0])
        peptide = first_part_list
    
    my_list.append([])
    my_list.append(peptide)
    return my_list

def generateAllLinearSubPeptides(peptide):
    peplen = len(peptide)
    my_list = []
    for i in range(0,peplen):
        for j in range(i+1,peplen+1):
            my_list.append(peptide[i:j])
    
    my_list.append([])
           
    return my_list
    
def generateSpectrum(peptide, isCircular):
    spectrum = []
    subpeptide_list = []
    
    if isCircular:
        subpeptide_list = generateAllSubPeptides(peptide)
    else:
        subpeptide_list = generateAllLinearSubPeptides(peptide)
        
    for p in subpeptide_list:
        spectrum.append(sum([c for c in p]))
        
    return spectrum

def isConsistent(peptide_spectrum, experimental_spectrum):
    peptide_spectrum_counter = Counter(peptide_spectrum)
    experimental_spectrum_counter = Counter(experimental_spectrum)
    
    for p in peptide_spectrum_counter.keys():
        if peptide_spectrum_counter[p] > experimental_spectrum_counter[p]:
            return False
    
    return True

matches = set()

while len(peptides) > 0:
    candidate_peptides = expandPeptideList(peptides)
    filtered_peptides = list(candidate_peptides)
    for peptide in candidate_peptides:
        generated_spectrum = generateSpectrum(peptide, False)
        generated_circular_spectrum = generateSpectrum(peptide, True)
        if Counter(generated_circular_spectrum) == Counter(experimental_spectrum):
            matches.add('-'.join([str(x) for x in peptide]))
            filtered_peptides.remove(peptide)
        elif not isConsistent(generated_spectrum, experimental_spectrum):
            filtered_peptides.remove(peptide)
    
    peptides =  filtered_peptides
    
print(' '.join(matches))
