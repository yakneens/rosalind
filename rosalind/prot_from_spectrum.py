from collections import Counter
'''

#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_22_4 (1).txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''
inputstr = """3524.8542
3710.9335
3841.974
3970.0326
4057.0646"""

experimental_spectrum = [float(x.strip()) for x in inputstr.strip().split("\n")]

amino_acid_weights = {'A': '71.03711',
 'C': '103.00919',
 'D': '115.02694',
 'E': '129.04259',
 'F': '147.06841',
 'G': '57.02146',
 'H': '137.05891',
 'I': '113.08406',
 'K': '128.09496',
 'L': '113.08406',
 'M': '131.04049',
 'N': '114.04293',
 'P': '97.05276',
 'Q': '128.05858',
 'R': '156.10111',
 'S': '87.03203',
 'T': '101.04768',
 'V': '99.06841',
 'W': '186.07931',
 'Y': '163.06333'}

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
        spectrum.append(sum([float(c) for c in p]))
        
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
