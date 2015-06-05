__author__ = 'weigel'
# This program will define a class "polymorphism"
# The objects will contain information on 1001 Genomes polymorphisms
# The methods will allow for interrogation of the polymorphisms

# global variables

# the four bases
DNAbases = ['A','G','C','T']
# first line with DNA data
firstPolymorphism = 0
snpList = []
# number of genotypes
samples = 0


# generate list of potential SNPs consisting of two letters and of SNP types
# substitution_types = ['AA', 'AG', 'AC', 'AT', 'GA', 'GG', 'GC', 'GT', 'CA', 'CG', 'CC', 'CT', 'TA', 'TG', 'TC', 'TT']
# transition_transversion = ['notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP', 'trvsn', 'trvsn', 'trvsn', 'trvsn', 'notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP']

substitutionTypes = []
transitionTransversion = []
numbers = []
for ref in range(4):
    for alt in range(4):
        substitutionTypes.append(DNAbases[ref] + DNAbases[alt])
        if ref == alt:
            transitionTransversion.append('notaSNP')
        elif (ref+alt) in [1,5]:
            transitionTransversion.append('trstn')
        else:
            transitionTransversion.append('trvsn')


# define class SNP
class SNP:
    def __init__(self, position=0, snp='', snpType='', snpFrequency=0, annotation='', methylation=''):
        self.p = position
        self.s = snp
        self.t = snpType
        self.f = snpFrequency
        self.a = annotation
        self.m = methylation

    def print(self):
        print(self.p, self.s, self.t, self.f, self.a, self.m)

# Read a .vcf file
file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

# count lines in file
with file as f:
    for linesInFile, l in enumerate(f):
        pass

file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

file.seek(0)

# determine whether it's a VCF file
currentLine = file.readline()
print('First line: ', currentLine)
if currentLine.find('vcf', 0, len(currentLine)):
    print('This is a .vcf file, we are good to go.')
else:
    print('This is not a .vcf file!')
    print(currentLine)
    exit()

# set read pointer back to beginning of file
file.seek(0)

# find header line
for line in range(100):
    firstPolymorphism += 1
    currentLine = file.readline()
    elementsCL = currentLine.split()
    if elementsCL[0] == '#CHROM':
        samples = len(elementsCL) - 9
        print("There are", samples, "samples.")
        break

# set read pointer back to beginning of file
file.seek(0)

print('First line with genotype information is line '+str(firstPolymorphism+1)+"." '\n')

# go back to first line before polymorphism
for line in range(firstPolymorphism):
    file.readline()


# start analyzing lines
for line in range(linesInFile - firstPolymorphism +1):
    # convert current_line into list elements_cl
    currentLine = file.readline()
    elementsCL = currentLine.split()
    # positions: multiply chr with 1,000,000, add positions
    snpList.append(SNP())
    snpList[line].p = int(elementsCL[0]) * 1000000 + int(elementsCL[1])
    # determine whether a position is a SNP or insertion or not, and if a SNP, what type of SNP
    ref = elementsCL[3]
    alt = elementsCL[4]
    change = ref + alt
    if not change in substitutionTypes:
        snpList[line].s = 'notaSNP'
        snpList[line].t = 'NA'
    else:
        snpList[line].s = change
        snpList[line].t = transitionTransversion[substitutionTypes.index(change)]
    # count number of lines with SNP
    for accession in range(9,samples+9):
        if elementsCL[accession].startswith('1|1'):
            snpList[line].f += 1







    if int(elementsCL[1]) < 100 or int(elementsCL[1]) > 999400:
        snpList[line].print()




















