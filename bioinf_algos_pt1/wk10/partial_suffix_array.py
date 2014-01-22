

myFilename = "/Users/siakhnin/Downloads/dataset_102_3 (1).txt"

f = open(myFilename, 'r')
inputstr = f.read().strip()

'''

inputstr = """PANAMABANANAS$
     5"""
inputstr = """GAGTATATAACCTGCATTACTGGAGCGCTCCCTTTTAAGAATCTAGTATCGGCACGCACGAACTCCCCATCGTTCTATTGTTACAGAGTACGCAGCCTGCCGCTGAAAGGACTAAATTAAACATAACTCATTTGGTCGGCTTTAAATTTACCCGGCCGCCAATGTCGTTGGCTGATCCAATAACTCACATGTGCCGCTCACTTTCCTAGACAATGTGACAGTGGACTGTGTTGGAGTCTAGTGGAAACGACCGTCGGAAATAGACCCTCCAAGGGATCTCCGAGCCTGCATTTTGCTACAGGTTGCTGGCTCGGCGTAGTGCTCTTTAGGGGTGAGTACTCAACTTAAACTGCATAACCTCATTATGTCTTTCTCCCGTAGTCTGACCGATAGGTGCATCTCCCCAAATCGTTAAGCCGCGTCTCCGAGGACGGCCCACGTCGCTCCATTTAGGGCATGCGGGCACCACAAATGCTAATACGTTTAACCGATCGCTCTCGGTGCTGCACTTCCCGGGACATGACACCTGCTATGCGGGACCGACTCATTGCACCATCGCGAGGGGCCCATGAGCGGTTTTATCAAACATCCTTGGTGATAGCTCCGTCTTCCCAGGAAATTCCTGAGGCGCAGGCTTGGGCACCGCCTACACGGGAGGATCCGGGGGTAGCGGTTAACCTAGACTTAAAATGTCCAACCTAAAACATTAAATCCCGCAGAAATACAAGACCTATGTCTTACCATAAACCATGCGGTCTAGACAGAAATGCACATATTACTCAACACTGATTCAATCACTGGAGTGCAAAAATGATGAGCGAGACTGATAGGCTGGGTACTTGTCAAGTATTATAACGGGTTGCTTAATACCCTCAGGGCTAGCTCCTGTCATGGACCACCTGTGTACCGTTCTCTAAAGTAGTCTATCTCTCTTCAGCTTTATGTCTGTTCGGCCTTAAAATGTACAAGCGGTGGGTCCGAGCTTATGCGGTCGCGGACTTCCACCATGCGAACGAGTGGCCTTGACGGGGAAGATCAAGGCGAGTACAATCGGCGGAGCGCGTGGGGCTGCCTACAGGTCACCACTGTAAATTACGTTGTCGATATGAACTCTCCGTGACCTTGTGTTTGGCACTTGTCAGTCGCTTCCTTGTACTAACTGAGCACAACTTGCTACAACCTTCCAATCAGAGACTGAAAGTTGTCACTTGGGTGTGGACATGGTGTAAGACTGGGTTCCCCTTCGTAGACAAGGTCCGCCCATGTATGGTCCCTAAATTGTATAAGGAAACGTTCGTGCAATTCATCCATTATGCGAGTTCTTCCCCCGGGGGGGCTGGGTTCTAGGGAAGTCAAACCACCCAGGCGTTGCTGATCAGCGATTGTCATTTTTCTAAAATGACTATTATCGCGCTCTCTCGATGTTTCCGGGTGCCCCATGTAATCGCGTCGACCCATCGGCCCTGGCAAAACAAAGGCGTTGGAATGTTCCGTCACACAATGGCTTAAAGAAACATCACTCGGAACACTGACCTCATCGGCGGGCCCCAACCGCACCCGCCAGGGTCACTTGTGGCCAATGCGGGACGACGACTTCTCCCTGAATAGAAACAATCCATAGGGACTCAGGCAATCCACACTATTTAAGTGATCTGCAAGCCTCAATCGAGAGTCAATTATTTGCGCCCATTCACAACCACGCCTGGAAATTCTTATAGTGCACACCCGGAGGGCACGTCGTGCTCAACGTACCATAATGGCGAGATTCCGTGGTTGCTAACCCATCGATAGCCAGGAAGATCAAGGCACCTCCCGCGCTACACTTTGATATCTAGACATCCGTCCACAGGGTATACAATTAAACGGGTTACTTTGCCGCGGTCAGCAAGCTCGGATCCCTTGCTTTAGACCTTTTTAATGATCAGACGTAACCTACTGAGTTATGAATACTGGGGTTCACTCTCTATGTGGACCTGGGATACCCATTGATTGAACGAGGACAAATGTCGCCAACAATAAAATCATGGGAATACAGGCCCCCGTTTAGTGGTGCTGGAAAGAGTCGGCACATTGCCCAAATTCTGAGAGGCGGACCACCTCCTCTTTTTCAGTCCGACGTTATAAAGATTTACGGCTTTAGGAGTATGCCATAGGTCCATGATCAATCCACAAGAGTAGATTAATAAAAATCTTTACTGGCTACCGAGAGTTAAACAGTGACAGTTCGTTTTTACTGCCGTAGGGCTATGTGTTAAATCCCGACGTATCATGATGCACACTTCCAACCCTAAGCACGATTCCATGTTGGGCCAATACGAACTGGCATAGTTTACACGACGTTTCTCCTTTCGGTATTAGACGAGAAACACTACCAACCTGTCAGAGCGACCGGGCCTTGACCGCGAGCTGGCAGCCATCAGGATTACCGTGACGTATTCACATGTACCCCGGTGGGTCGTTAATGCAAACCGTTAGCCCGGACGACTGCAATGTCCAGGACGTGAGAACTGCGGCAGCTGAATACATGAGGCGCCCCGGACGCCGTGAGCAATGCATGTTATTGCGGCTCAGTGCCACAGATGTTGAGGTTCCACTGTGCCATTCTCTGCGTCCAATGCAATATCTATACGGAAAGAGTAGGACGTGTCCGTCTCTGTACGAGTACGAGCGCATTCAGAATTCGTCCGACAATTATGAAAGCGGTGGCGGTCACAAATTAGATGCTCTAGCCATAAGAGCTGATATGTAATAGTTCTCCGCCGTCTTCGAGGTTCAGGAATTGCCAGGAAAGGAAAAACAAATCTAGTGCCCCGAAGTGTGTCTTAATCATGATGGCAATATTACCGGGTTTCAGCACAGTTAGGGATAATGTATGAAATCTGGCAGACCTCAGTAATACTTAAACGATTGAGGGAATGAACTGATAATTATTATTCTCCTATCATCCAGAGCTCATCAGAAAGCAGGACAAATTATGCCTAACGCACTTTTACCAGTACGTCCTCGGCAGTATTAAAAACCACGAGTCCAGTAACTCCTGAAAGGGAAGAATGTTCTCCGCTGTCCATAGTAGAAAGCCGTGTACAATTCAGGACTACTTTGATAATATTTAGGAATTTCTATCAACATGGCAAAACCATTGCTGGGCGCGAACGTACGAATTTGCATTATACCTTCTCCCGTAACGCGAGTTTTTCTCGATTCGGATCCGGGAAATCCGCTGTTTGGGGACAGTTGTAAAAATCGAGCAATGTGTCCGTTTATCAGTCTTCGGATAGTGGCCACGTTGCCGACGTGCCGGGCTAGGAGTATCTGGTGCGTCTGTTTCCGATGGGCTCAGTCCCAGCCAAACTGCCTCTACCTCCTTCACTACCTGTCTTTCGACTTTGACCCAAAATATGCAGATTTTCTGCTCTTCCTCGGTTGAGGCGCCTAAGGTACATTAGTGAGTGGGGAGGCATCTTCTGCCTTGTGTGGGGGGGAAATGCTCTACTAATATAGCGACACCATTGGCGAAATTTGCTGCGACTCAGGTATCCTGTGCGGCCCTTCCTATGATAGATAGTCTATATTTGTGCCCAGCCTTATCTTTGCGGCTACCGCGCTAGCAAGAGCGTATGGTCCGAAATTAGCGCCCTCAACCGGTTCGCTCATAATGACAGAGTCATCCTACCCAGTGTATGTATCGCCATTTTGCCTTTGCATCCTGTGACAGGGGGCTTAGAGCTTAACCCTAATGCCCCGCTACTGCTCCGGGGAAAATCTACGAATTGCGAGCAAAACAAGAATTGTCGATAGCCACTTCGTCCATTCCACGAGAAGCCTCAGCTGGCTTGTCCCCCCGTTTTTATCTTCACCTTTTCCAATACTCATTCGGGCAACCCACAGATTGGGTTCGCTGATCAGGTTGCTGATTCTTTTATACTTGCGCCCAGAGCACTGCCGCGAGGTGTTCGCCGCCTTAGTCATGTGGCCGCGTTATCATATCACCGCGCACGCGAGGATGGAAACTCGATAAGAGGGTACGATAACTATTGCTCCCGTAGCTCTGCAAGAGAGCCCTCGGGCGGGTGTCCGAATCCGTTCAGCGAAATTCCGTGCCCCTTCCATGCTGACTAGTGCTTAGGTGTACCGAGGTACCTAATTCAGGCGTGCCAACTGCTCTGTCAAGCGTCATCATGGTTTGGCTCCGACGGAATTCTAGGGCCAGCTTACGTGGCCCAACCGCAAACCAGCGATCAGAACGCTTAAGTAACAAACGTTGGCAGCGTCTGGGACTCGTAAGAGGTAAAAGCTGTGTACGGCAGAGGGGGCGGTGTGTATTTATATATCGCCACGATCGGCACATACTCGAGGTTGAGACAATCTCCTTAGTTCCCGGGCACCATCGCAATAGGCGCAAGTTCGAAACAGGTATACGCTCCGGGTGATAACCCCAGCCGGAACTAGCGTGTAATAAGCGGATTTCCCGTGGCCACCTATGTCATAGCGGGGTGACACGTCGTGTATGACCTCCTCGTTGCTCTGATGTAAAGCCCACGCTATGCATTTAGCACCCCGGTAAGAGAAGACTGTAAGGTAAAGAGGAGGATAACTGCACCCCCAACAAATCTCTCCGCTAAGGTAGGAGTGCTGAGTACACCCCACAACTCGAAAAAAACTGACCCACACTGCAATATGCACATACAGCGAGTTTGTTAGGGAAAAATCCGGTCTCGACCAGCAGATACTTGCGCATGCTTTGAATTAAATAACATTCATTGGCCGCACATTTGAATTTTACCAGAACGAGCGCTAGACGTAATTTGCCTTCCTTCGACTCATTTCCCGGAAGCCTGAACCACGTGGTGCCTCCGGTACCTCGACCGCAACATCTGACAGTCTGTTGTGTCCATCACACTAGTACCGATGGCTTGGTCTCCCACGGTGGCAAAATGCTGATTTACATGGTACTTTGATACGCGATGCGGAACATCGTCTTGTTGTTACCGAATCCTCTTAGGAACCTTCGGGGAAACTTCTGGTCCTTAGGCCTGCTCATTCAGTTTTAGCGAGAACTGTGATGCGTAACTCCACCACTAGTTTATAATGGCGACGCGTTCCGCATACGACTAAGCTTGTATCCGGAAGTGGCATTCTCGGGTCCGTAGGGGGCTAGTTTGGCTAGTCCTATCCAGGAGACTAGAAACGTGTTGTGCTATTCTTCCGGCTGAAGCGGGCGTATAATTATACTCAGCTCTCCGGCTCCAGACAAACAGACCGGTGCTTCGGCCAGACTTGGGGCTCTCATCATACACCATTGCTGCCCAAGGGCATAACTCGCATCGAGTCCGTACCTTTCTCCGTCCGCGACCTAGCTGGACGTAGCTCTTGCACCGAACCGTCCTATAGAATGTGTAGGTATTCACTAGTTAATCACCCATTATGAAGGACAGTACGGTGGAATGCAAACTTCGCGTCTGCGCCATCAGAACTTATGTAGTGACTGCAAGCGGCTTTACTGCGGCGACGTCTTATGGCCCGGCCGAACCAAGGGAAACTAATTCATCTGGCGGAACGATATAGAGAGACCCCGTGGCCTAATAATAGCCGTGCCTTAGTGTGGCTTGAATCGGACACTGACTTCCGGATGTCGGCGTAGTGCAATCATATAATTGAACAGAAAACTGGAATTTTAGTCCAATAAATCGACTTGCTCTGGACTAGCAGTAGGCTTAGCACTCACATTATGGCGCTAGTTTGTTTTAAACTGTGTAGAGTGGTTCTAGCCATTCTTGGCTGTGGGCGTGTTTTCGCAGGCCGGAGTTGCGGAGACGTCGCCCCAGTGTAATCAGGATTGGTCGCTGGTTTTCGTCTGCGGTATGTCCAACATCAACGTTCAAGGGCGTGAGTGACGGGATTGCACCGCCGAACTCCAAACACGTCGTTGACCGCGTGGCAATCCTGGTTTAGACAATCCACTCCCAGTGCCATACCATCACTGCGGGAATTCGGCTAATGCCTAGACCGCAATTCGCAACGCTCGCAGTTAGATGTTAGGTCGGCTCCTACTATCCGAGATGTCCATGCGGCCGAATTCGTTTTGGGGGCCCTCTTCGAACATGATAGTATCAATGCGGACCTCCGGAGCGTATAGTCATAAAGGTTGCGCATTGTATCGAGTCAGTAAGGAGACGATGGCGCTCGAGGCGTCACTCAAGTAGCATAGTATTATAGACGTATGACTTCGAAATCTTGGGAAGAGGGCAGGGCGTAGTTTTTCGTGCGTCTGGGGGCGGCACTGAACACCGGCTACAGGCATATCTACCATGGAGCCTTGCCCTGTTCGATTTCTTGTGTTCCCCTGGAGAGCGTGTAATATAAGCCGACTCCCTTGCACCAACAACAAACATGTTTCGACTGCCCCCCCCCAAAAGTGCTCAAACACTGGGGGACTTCCGCCGCGCCGTTATTACAATAAGCTATTATGTATTTTTCTTTGCCCCTGTCGAAAGATAGTTGCCGTGGCCGCTCGGGCCGATCGTGCACTGGCGCACCCACTACAGCAGCTGTATGCTTGGTGTGACCATTTCCTGCGTAAATACCGCTGGGGACGCCCTATCGCACAGCCCGATACGCCGCTGGCATCCTATGAATCCGCGGTTCCAATCTTACTCAGATGCGACTCCTCGACGCTATGATAACATGAGCCTCCTCCCTCGTACCACTTGCCGTACTGTAACTGTCACCCAATGAAGTGCTTCCGCACATACATGCACCCGCAAGCTCCTATTTTCGTTAACCCTCCTTAGCCTTAGAATTACGCACAACAGCCTATAAGGTGGTACTAGCGGTTACGAGCCACCTTGTCGAATCAAAGGAGCCCTATCGCTCCGTGGGCAGGACGGCAAACAGACAAGCTGAATAGCCATAGGTCGAGCTCACCCACCTGTCGGAGATTGGCCTGTGCTAGATTCGACAGTGACTAGTACGCGCGCGCGATTACAGTACCGTGCTCTGTTAAGAAAAGTGGCCTCTGGTCCTCTGAACTAAAGTTGGGGTTACCCTAATTAATTCCGTGTAAGCTTCTCTATAATCCTAGTATGTCGGATTCTCAGACCTATTGCTCGAGGACGATCAGCTGAGCGAATCGTACCCGGGGGCACGCTTGTTATGCCCGAGGGATTTGTCACCAGTGGTAGAGCTCGTGGGCCTTATGTAGGCGTATTTCGGAAGGGCCTAGAGGTCTAGAAGCGGACTACAAGTGCACGATCGTCTAGCTAATACCAACACGTTAGCCTTGGGATTGTGAACGTTGTAGGGGGTTTTGACAGGTAAGTGCTCTCCCTGGATGTACGTCCCATTCTTAGTTATGGATCTCGTCGTGTGAAAAATCACTACTGTTTAAATGATCATTATTATCAGGATTGTGCTCGCGTCATATACTCGGAGCATGGCGAAGTAGCAACACTACCATCCATACCTAGACGTTCAATTGACGCCAGAGGGGTATTTAGCATGAAAAGGTCGAGTTGGTGAAATTGTGCTACTCGGTGGAGATTGCTGAAGAACTAGCACAGCATTTTTAGAGATTAATGGTCGCAACGACAGCCTACTGGAATGCCAAATCATCAAATGTAAAATCCATGCATGGTGCGAACGCTCGTCGCATGTTACATGTCCAAAAGTACGACTCTCTACATGGGTAGCTATAATGATCCTCATTGGTGTGGGGAACGTGCTGATCCCGTATTTATCTGCTATGCACGGGACGATACCCACCATATCATTTGTGCGCCTCCGGATCCGATCCCGCCTATTATGTACTAGCATTGCGGGGTTCAATTATTACGATATCTGGACAACATTTGAGCGGCTAGACTAGCATAGGACGCACACTGCTGGTCAGTAGAAGAATACCGTACAAGCGCTTTTAGGGTACCGCATAGTTACAGGACGCGGTACTAATTAGATTAGCCGCTGGCGTTCCCATGGGCATCCTATGACCCCCAAAAAAAAATATAGATGGGAGCTCAGGGGCGACGATCATAAGCCTATAGCCGTGACGGTGATACCCGCCCGTAGAGAGTGATACCCAGCTACTTAGTGGAGCAGCCTGGCGCAGAGAAATTCGACAGATCGCGGACATGGGCTCTTCGACTCTATGACGATGGTTGAAAGAACTACGTAGATATTAGCACCGTCTCTCCCTAAGCTTCCTTCGAATCGTTTCTCGTCTGCGCACTCCACTAATACACCAAAGTAAACGTAAGGGTCAGCCGCCCGTAGAGCGCCCCGGGTAAGCTGGCGAGGTAGTCACTAAAGTCAGCTCCTGATCACGACGGCCTCCCGAGTGGTCTTATCGGGCCCTAAAACTCAGTCTAAGATAAATGCGTAGGTGGGGTGTATTAAGCGCGAGGTCAAACCATTTCAAGGAGGATAATGCGCTGCTGTGGTCATCTGCAGACTAAGCACAGAAGTTCGAGTTAAGATATATGATGGAGCCTTGTGCTCCACCATTCTAAATTGGTAGGCGCGTACCATGGAGCTTCCAGCTAAAGTGCGCGCCAAGCCTGGATGGAGGCCGGAATCAATCTGGGGGGTCGACGAGGCCCCTTCTAGTGGCCATAGCCCATTAATGTATAAACATCGATTAAGTTGAAAGCGTCACGGTGATGACATGTTGGCCGGGCAAGACTACCGGTCTCCTGCAATGGACATCGTGCTGACGTTGTCCTCGGAGTAGCTCCGTTAGCTAATATATTGAAAAATCCCGTTCGTGAATTCCTATCTATCCCGACGCGGCAGGAAGTCGGACATGGATTGATCCCTGTATAGGCATCGGTAGCAGGCAAAATTAGTACAGCCAATGCACGCATTATCCTCGTGTTGAGGGCCCTCCGGAAGTAGCTGGGCCATCTCGGATACGGTGACTTCCGGTTTAAGAACAGAGGCGTATACCCACTGCCCTGAACACAGCTGCAGCTCGGCTGATAGTGAGACCATATTTCACAGCCCAGTACTCGATAAAGCAGTCTAGTGTCATCCACAGACATCCATTAAGCTCTCGCAGCCGGCCGATCGCCGACACTCGGGCTATACGGGACCATTCCGCCACGCCTGTATTAGCTGACCTCGGGTCAGACCGCGTAGAAGAGTCTCGGATCAGCGATAATTCGGTTAGCCTCATTCAAGAAGTAGTCGCGTGGTAAATTTAGTTGATTAGGGATGAAGGGCCTGTAAACGAACGGGTAATTGAATCGTACTTGACCACTCAGCCCAGTCAGCTATTCGAGCTCTATTCACGCAAGTGAGGGAACGACGAGTAGTCTTATGTGAAGGTAACTGTTTCCGTAAAAGTCGCACACCGTTCAGATAGCAATGACTTAGCTTCCTCGCACAGTTCTTCGAAGGATCTGGACCAAAAACATTATTCCCCCCCCCGTGCTAGGGGGGGCTCCGGGGATTCACTAGGCGAAAAACTCAAGCCGTAGGGGATCTAGTGGGGCTTTTCGTCCAGCTGAAACGTTGCAGACCCTTGTGCCGGTAAAGTGTGCACCCACACTGAGCTTGTGACTATTCATCATTCCGTTGGCAGGAGGTGCATTACTCAGCTCTTCTACCATGGGGATCCTATCAGGATCGGGACTGTATCGAGATGAAGGCGTTGATCCTCTCAATGAACTTCCACATATATGGTCGCAGAAACATGACTATGGGGGGGCAAATCTGCATGCACAACCTAGACGTATCATGGTGAGAAGGAGGCCGTCCCGGAATGTGCTGTAACACTTCTCGTCATAATGACTATAGAGAGGTTCTGCCCTGGCCTCAGGAAGATGTAGTGAGGGCTGCGATGCTATTCAAAATTCTCGTCGGGGTGCGCAATCACACTAAGGTCCTTTAGTCATGCGATCCAAGCTAGTTGCCAATAACGTAGGGCTGGTGTAACGACGTTTTGGGAGACCCTTTGATTAGTTTCATGGCCCAATCATCTGTGAAGTGAGCATACTCCCATGTA$
6"""
'''
input_list = inputstr.split("\n")
my_input_str = input_list[0].strip()
k = int(input_list[1].strip())     
     
input_len = len(my_input_str)

f = open('partial_suffix_array.out', 'w') 
new = sorted((input_len - i - 1 for i in range(input_len)), key=lambda(x): my_input_str[x:])

for i,v in enumerate(new):
    if v % k == 0:
        f.write(str(i) + "," + str(v) + "\n")

