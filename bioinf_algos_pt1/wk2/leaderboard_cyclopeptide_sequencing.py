from collections import Counter
from operator import itemgetter

#myFilename = input("Eneter filename:")
myFilename = "/Users/siakhnin/Downloads/dataset_24_4.txt"
f = open(myFilename, 'r')
inputstr = f.read().strip()

'''


inputstr = """10
     0 71 113 129 147 200 218 260 313 331 347 389 460"""
inputstr = """26
0 71 97 101 103 113 113 113 113 114 114 115 128 128 128 128 129 131 131 131 156 156 184 186 186 200 214 227 227 228 230 231 241 242 242 243 244 244 256 257 262 269 270 287 298 299 301 328 331 340 340 343 345 345 356 358 359 370 370 372 375 383 385 397 400 401 429 430 442 453 454 454 459 462 468 471 472 473 474 485 486 487 498 499 501 512 514 514 542 561 567 570 573 575 581 583 585 590 599 600 600 601 602 610 615 615 616 627 627 630 658 695 696 698 698 698 701 703 704 713 723 728 728 728 728 730 730 731 741 744 747 758 761 769 799 810 817 827 829 831 832 841 841 844 844 851 854 854 857 859 862 872 882 884 886 889 928 928 944 945 947 955 955 958 959 960 966 967 972 972 982 985 990 996 997 1000 1000 1003 1041 1056 1059 1062 1068 1068 1068 1073 1075 1075 1084 1087 1089 1095 1097 1103 1113 1114 1128 1128 1131 1152 1172 1172 1181 1182 1184 1189 1190 1190 1196 1197 1199 1200 1202 1210 1212 1227 1231 1242 1259 1259 1283 1295 1298 1303 1303 1303 1303 1304 1311 1312 1317 1318 1325 1325 1328 1330 1338 1340 1345 1355 1356 1388 1396 1416 1426 1426 1427 1431 1432 1432 1434 1440 1442 1443 1445 1451 1453 1453 1454 1458 1459 1459 1469 1489 1497 1529 1530 1540 1545 1547 1555 1557 1560 1560 1567 1568 1573 1574 1581 1582 1582 1582 1582 1587 1590 1602 1626 1626 1643 1654 1658 1673 1675 1683 1685 1686 1688 1689 1695 1695 1695 1696 1701 1703 1704 1713 1713 1733 1754 1757 1757 1771 1772 1782 1788 1790 1796 1798 1801 1810 1810 1812 1817 1817 1817 1823 1826 1829 1844 1882 1885 1885 1888 1889 1895 1900 1903 1913 1913 1918 1919 1925 1926 1927 1930 1930 1938 1940 1941 1957 1957 1996 1999 2001 2003 2013 2023 2026 2028 2031 2031 2034 2041 2041 2044 2044 2053 2054 2056 2058 2068 2075 2086 2116 2124 2127 2138 2141 2144 2154 2155 2155 2157 2157 2157 2157 2162 2172 2181 2182 2184 2187 2187 2187 2189 2190 2227 2255 2258 2258 2269 2270 2270 2275 2283 2284 2285 2285 2286 2295 2300 2302 2304 2310 2312 2315 2318 2324 2343 2371 2371 2373 2384 2386 2387 2398 2399 2400 2411 2412 2413 2414 2417 2423 2426 2431 2431 2432 2443 2455 2456 2484 2485 2488 2500 2502 2510 2513 2515 2515 2526 2527 2529 2540 2540 2542 2545 2545 2554 2557 2584 2586 2587 2598 2615 2616 2623 2628 2629 2641 2641 2642 2643 2643 2644 2654 2655 2657 2658 2658 2671 2685 2699 2699 2701 2729 2729 2754 2754 2754 2756 2757 2757 2757 2757 2770 2771 2771 2772 2772 2772 2772 2782 2784 2788 2814 2885"""
'''

inputlist = [x.strip() for x in inputstr.split("\n")]
num_leaders = int(inputlist[0].strip())
experimental_spectrum = [int(x.strip()) for x in inputlist[1].strip().split(" ")]
print(num_leaders)
print(experimental_spectrum)

amino_acid_weights = {'A':71,'D':115,'V':99,'G':57,'E':129,'I':113,'M':131,'T':101,'N':114,'K':128,'S':87,'R':156,'F':147,'L':113,'P':97,'H':137,'Q':128,'Y':163,'C':103,'W':186}
distinct_amino_acid_weights = [71,115,99,57,129,113,131,101,114,87,156,147,97,137,128,163,103,186]
peptides = [[]]

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

distinct_amino_acid_weights = [71,115,99,57,129,113,131,101,114,87,156,147,97,137,128,163,103,186]

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

#print("Score ",calculateScore([0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484],[0,113,114,128,129,227,242,242,257,355,356,370,371,484]))

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

leaderboard = [[]]
leader_peptide = []
while len(leaderboard) > 0:
    candidate_leaderboard = expandLeaderBoard(leaderboard)
    filtered_leaderboard = list(candidate_leaderboard)
    for peptide in candidate_leaderboard:
        peptide_mass = calculateMass(peptide)
        parent_mass = calculateParentMass(experimental_spectrum)
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
