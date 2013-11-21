import re

myFilename = "/Users/siakhnin/Downloads/dataset_18_3.txt"

f = open(myFilename, "r")
inputstr = f.read()

'''
inputstr = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
'''

def buildPeptideFromRNA(rna_str):

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
    
    #print(x)
    
    #
    prot_str = ''
    
    #print(re.split('([A|U|C|G]{3})', input_str))
    
    for c in re.findall('([A,U,C,G]{3})', rna_str):
        #print(x[c])
        if (x[c] != 'Stop'):
            prot_str = prot_str + x[c].strip()
    
    return prot_str    
    
peptide_str = buildPeptideFromRNA(inputstr)
print(peptide_str)    