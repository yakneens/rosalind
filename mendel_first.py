myFilename = input("Eneter filename:")

f = open(myFilename, 'r')
inputstr = f.read()

inputs = inputstr.split(' ')

k = int(inputs[0])
m = int(inputs[1])
n = int(inputs[2])

population = k + m + n

AA = k / population
aA = Aa = m / population
aa = n / population

AA_AA = (k - 1) / (population - 1)
AA_aA = AA_aa = k / (population - 1)

aA_aA = (m - 1) / (population - 1)
aA_AA = aA_aa = m / (population - 1)

aa_aa = (n - 1) / (population - 1)
aa_AA = aa_aA = n / (population - 1)


ans = \
AA * AA_AA + \
AA * aA_AA  + \
AA * aa_AA + \
aA * AA_aA + \
aA * aA_aA * 3/4 + \
aA * aa_aA * 1/2 + \
aa * aA_aa * 1/2 + \
aa * AA_aa

print(ans)