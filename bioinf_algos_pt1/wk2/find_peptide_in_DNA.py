import re


myFilename = "/Users/siakhnin/Downloads/dataset_18_6.txt"

f = open(myFilename, "r")

inputstr = f.read()

'''
inputstr = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA\nMA"
'''
inputlist = [x.strip() for x in inputstr.split("\n")]
inputstr = inputlist[0]
num_codons = len(inputstr) / 3

pep = inputlist[1]
peptide_length = len(pep)

def getDNAReverseComplement(dna_str):
    complements = {'A':'T','C':'G','G':'C','T':'A'}
    outstr = ""
    
    for c in dna_str:
        outstr += complements[c]
    
    return outstr[::-1]

def getRNAReverseComplement(rna_str):
    complements = {'A':'U','C':'G','G':'C','U':'A'}
    outstr = ""
    
    for c in rna_str:
        outstr += complements[c]
    
    return outstr[::-1]

def DNAToRNA(dna_str):
    return dna_str.replace('T','U')

def RNAToDNA(rna_str):
    return rna_str.replace('U','T')

r_to_p_str = '''UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G '''
    
    
x = dict(re.findall('([A,U,C,G]{3}) ([A-Z]{1}   |Stop)', r_to_p_str.replace('\n','   ') + '  '))

def buildPeptideFromRNA(rna_str):

    prot_str = ''
    
    for c in re.findall('([A,U,C,G]{3})', rna_str):
        if (x[c] != 'Stop'):
            prot_str = prot_str + x[c].strip()
    
    return prot_str    
    
def generateCandidateStrings(inputstr):
    candidate_strings = []
    
    input_rna = DNAToRNA(inputstr)
    
    candidate_strings.extend(re.findall('(?=([A,U,C,G]{' + str(3*peptide_length) + '}))', input_rna))
    
    return candidate_strings

def getPeptideMatches(candidate_matches):
    peptide_matches = []
    for c in candidate_matches:
        if buildPeptideFromRNA(c) == pep or buildPeptideFromRNA(getRNAReverseComplement(c)) == pep:
            peptide_matches.append(RNAToDNA(c))
    return peptide_matches
    
matches = getPeptideMatches(generateCandidateStrings(inputstr))

print(' '.join(matches)), 