from collections import Counter
from operator import itemgetter
import itertools as it
'''
#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_26_7.txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''



inputstr = """16
84
672 669 1075 761 690 464 579 344 841 1142 1291 633 1204 438 474 882 399 853 879 301 637 766 303 1275 985 216 595 113 781 668 1191 1086 1249 458 87 273 601 1248 486 1176 729 511 417 975 546 224 1261 1116 682 596 71 214 938 87 295 1275 1138 966 1174 367 568 725 759 1233 816 1305 1263 896 658 129 1215 300 396 924 325 287 0 1067 171 945 1089 466 704 1154 434 881 1158 1305 995 898 99 580 1199 276 382 158 612 1029 509 693 851 603 928 186 767 888 1037 805 270 57 963 295 521 204 1092 680 360 876 377 783 208 147 794 1146 387 1225 483 980 1148 480 137 1061 581 246 188 417 750 101 694 1018 481 904 333 945 1067 1059 57 213 1362 1002 424 114 163 1149 1062 220 782 557"""
inputstr = """20
     60
     57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493"""


inputlist = [x.strip() for x in inputstr.split("\n")]
num_amino_acids =  int(inputlist[0].strip())
num_leaders = int(inputlist[1].strip())
experimental_spectrum = [int(x.strip()) for x in inputlist[2].strip().split(" ")]

amino_acid_weights = {'A':71,'D':115,'V':99,'G':57,'E':129,'I':113,'M':131,'T':101,'N':114,'K':128,'S':87,'R':156,'F':147,'L':113,'P':97,'H':137,'Q':128,'Y':163,'C':103,'W':186}

peptides = [[]]

def getConvolutionOfSpectrum(spectrum):
    convolution = []
    [convolution.append(x[0] - x[1]) for x in it.ifilter(lambda x: x[0] > x[1], it.product(spectrum,repeat=2))]
    return convolution

def getSpectrumBasedAlphabet(spectrum, num_acids):
    #Compute convolution
    convolution = getConvolutionOfSpectrum(spectrum)
    
    #Only keep masses between 57 and 200 units of weight
    filtered_convolution = filter(lambda x: x >= 57 and x <= 200, convolution)
    
    #Collect mass counts
    massCounter = Counter(filtered_convolution)
    
    #Convert to a list of tuples
    mass_list = [(k, v) for k, v in massCounter.iteritems()]
    
    #Sort by number of ocurrences
    mass_list = sorted(mass_list, key=itemgetter(1), reverse=True)
    
    current_index = 0
    spectrum_based_alphabet = []
    
    num_masses = len(massCounter) 
    bound = min(num_acids,num_masses)
    
    #Add the first n masses
    for i in range(0,bound):
        spectrum_based_alphabet.append(mass_list[i][0])
    
        
    if num_masses > num_acids:
        #The N-th mass
        nth_mass_count = mass_list[num_acids-1][1]
        i = num_acids
        
        #Add all the ties for N-th most common mass
        while i < num_masses:
            next_mass_count = mass_list[i][1]
            
            if next_mass_count == nth_mass_count:
                spectrum_based_alphabet.append(mass_list[i][0])
                i+=1
            else:
                break   
        
    
    return spectrum_based_alphabet


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

def expandLeaderBoard(leaderboard):
    candidate_leaderboard = []
    
    for pep in leaderboard:
        for w in distinct_amino_acid_weights:
            new_pep = list(pep)
            new_pep.append(w)
            candidate_leaderboard.append(new_pep)
    return candidate_leaderboard
 
def calculateMass(peptide):
    return sum(peptide)

def calculateParentMass(experimental_spectrum):
    return max(experimental_spectrum)

def calculateScore(peptide, experimental_spectrum):
    
    peptide_spectrum = generateSpectrum(peptide,True)
    sorted_peptide_spectrum = sorted(peptide_spectrum)
    sorted_experimental_spectrum = sorted(experimental_spectrum)
    
    score = 0
    
    i = 0
    j = 0
    
    peplen = len(sorted_peptide_spectrum)
    speclen = len(sorted_experimental_spectrum)
    
    while True:
        if i == peplen or j == speclen:
            break
        
        if sorted_peptide_spectrum[i] == sorted_experimental_spectrum[j]:
            score+=1
            i+=1
            j+=1
        elif sorted_peptide_spectrum[i] > sorted_experimental_spectrum[j]:
            j+=1
        else:
            i+=1
            
    
    return score

def cutLeaderboard(leaderboard, experimental_spectrum, num_leaders):
    filtered_leaderboard = []
    chosen_leaders = 0
    peptide_scores = []
    leaderboard_size = len(leaderboard)
    
    if leaderboard_size > 0:
    
        #Tuples of (peptide,score) created
        for peptide in leaderboard:
            
            #If score has been previously computed look it up, if not compute and store in dictionary
            peptide_score = peptide_score_dict.get(tuple(peptide))
            if peptide_score == None:
                peptide_score = calculateScore(peptide, experimental_spectrum)
                peptide_score_dict[tuple(peptide)] = peptide_score
                
            peptide_scores.append((peptide,peptide_score))
        
        #Sort the tuples in descending order according to score
        sorted_scores = sorted(peptide_scores, key=itemgetter(1), reverse=True)
        
        #Make sure we don't go out of bound on the leaderboard
        bound = min(num_leaders,leaderboard_size)
        
        #Add the first n scores
        for i in range(0,bound):
            filtered_leaderboard.append(sorted_scores[i][0])
        
            
        if leaderboard_size > num_leaders:
            #The N-th score
            nth_score = sorted_scores[num_leaders-1][1]
            i = num_leaders
            
            #Add all the ties for N-th score
            while i < leaderboard_size:
                next_score = sorted_scores[i][1]
                
                if next_score == nth_score:
                    filtered_leaderboard.append(sorted_scores[i][0])
                    i+=1
                else:
                    break
        
    return filtered_leaderboard

peptide_score_dict = {}

#The weights are determined using a spectrum convolution
distinct_amino_acid_weights = getSpectrumBasedAlphabet(experimental_spectrum, num_amino_acids)

leaderboard = [[]]
leader_peptide = []
while len(leaderboard) > 0:
    candidate_leaderboard = expandLeaderBoard(leaderboard)
    filtered_leaderboard = list(candidate_leaderboard)
    for peptide in candidate_leaderboard:
        peptide_mass = calculateMass(peptide)
        parent_mass = calculateParentMass(experimental_spectrum)
        
        if peptide == [99,71,137,57,72,57]:
            print "here"
        
        if peptide_mass == parent_mass:
            #If score has been previously computed look it up, if not compute and store in dictionary
            peptide_score = peptide_score_dict.get(tuple(peptide))
            if peptide_score == None:
                peptide_score = calculateScore(peptide, experimental_spectrum)
                peptide_score_dict[tuple(peptide)] = peptide_score
            
            #If score has been previously computed look it up, if not compute and store in dictionary
            leader_score = peptide_score_dict.get(tuple(leader_peptide))
            if leader_score == None:
                leader_score = calculateScore(leader_peptide, experimental_spectrum)
                peptide_score_dict[tuple(leader_peptide)] = leader_score
                
            if peptide_score > leader_score:
                leader_peptide = peptide
        elif peptide_mass > parent_mass:
            filtered_leaderboard.remove(peptide)
    leaderboard = cutLeaderboard(filtered_leaderboard, experimental_spectrum, num_leaders)
print ('-'.join([str(x) for x in leader_peptide]))
print(leader_score)
