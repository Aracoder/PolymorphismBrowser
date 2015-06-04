__author__ = 'weigel'
# This program will define a class "polymorphism"
# The objects will contain information on 1001 Genomes polymorphisms
# The methods will allow for interrogation of the polymorphisms

# global variables

DNAbases = ['A','T','C','G']
SNPlist = []

# translate SNPs into numeric codes
# None 0000
# A>T 2
# A>C 3
# A>G 4
# T>A 10
# T>C 30
# T>G 40
# C>A 100
# C>T 200
# C>G 400
# G>A 1000
# G>T 2000
# G>C 3000

# generate numeric codes
SNPcodes = []
for ref in range(4):
    for alt in range(4):
        if ref == alt:
            SNPcodes.append(0000)
        else:
            SNPcodes.append(10**(ref) * (alt+1))
    # code 5555 for polymorphism that is not a SNP
    SNPcodes.append(5555)

# generate list of SNP types consisting of two letters
SNPtypes = []
for ref in range(4):
    for alt in range(4):
        SNPtypes.append(DNAbases[ref] + DNAbases[alt])

# first line with DNA data
first_polymorphism = 0

# Read a .vcf file
file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

# find first line that does not start with ##
current_line = file.readline()
print('First line: ', current_line)
if current_line.find('vcf', 0, len(current_line)):
    print('This is a .vcf file, we are good to go.', '\n')
else:
    print('This is not a .vcf file!')
    print(current_line)
    exit()

# set read pointer back to beginning of file
file.seek(0)

for line in range(100):
    first_polymorphism += 1
    current_line = file.readline()
    first = current_line.__getitem__(0)
    if first != '#':
        break

# set read pointer back to beginning of file
file.seek(0)

print('First line with genotype information is line ',first_polymorphism, '\n')

# go back to first line before polymorphism
for line in range(first_polymorphism-1):
    file.readline()

# start analyzing lines

for line in range(10):
    # convert current_line into list elements_cl
    current_line = file.readline()
    elements_cl = current_line.split()
    print(elements_cl)
    # positions: multiply chr with 1,000,000, add positions
    c_pos = int(elements_cl[0]) * 1000000 + int(elements_cl[1])
    print(c_pos)
    # determine whether a position is a SNP or insertion or not, and if a SNP, what type of SNP
    ref = elements_cl[3]
    alt = elements_cl[4]
    print(ref,alt)
    if alt not in ['A','T','C','G']:
        SNPlist.append(5555)
    else:
        SNP = ref + alt
        SNPlist.append(SNPcodes[SNPtypes.index(SNP)])
        print (SNPlist)


















