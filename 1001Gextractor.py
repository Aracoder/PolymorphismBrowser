__author__ = 'weigel'
# This program will define a class "polymorphism"
# The objects will contain information on 1001 Genomes polymorphisms
# The methods will allow for interrogation of the polymorphisms

# global variables

# the four bases
DNAbases = ['A','G','C','T']
# first line with DNA data
headerLine = 0
# initialize variant list - holds objects of the Variant class
variantList = []
# number of genotypes
samples = 0
# number of variants
variantCounter = 0
# accession IDs
accessions = []


# generate list of potential SNPs consisting of two letters and of SNP types
# substitution_types = ['AA', 'AG', 'AC', 'AT', 'GA', 'GG', 'GC', 'GT', 'CA', 'CG', 'CC', 'CT', 'TA', 'TG', 'TC', 'TT']
# transition_transversion = ['notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP', 'trvsn', 'trvsn', 'trvsn', 'trvsn', 'notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP']

substitutionTypes = []
transitionTransversion = []

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
class Variant:
    def __init__(self, position=0, variant='', variantType='', variantFrequency=0, alleleDistribution=[], missingData=0, missingDistribution=[], annotation='', methylation=''):
        self.p = position
        self.v = variant
        self.t = variantType
        self.f = variantFrequency
        self.a = alleleDistribution
        self.m = missingData
        self.md = missingDistribution
        self.an = annotation
        self.mt = methylation

    def print(self):
        print(self.p, self.v, self.t, self.f, self.a, self.m, self.md, self.an, self.mt)

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
    headerLine += 1
    currentLine = file.readline()
    elementsCL = currentLine.split()
    if elementsCL[0] == '#CHROM':
        samples = len(elementsCL) - headerLine
        print("There are", samples, "samples.")
        accessions = elementsCL[headerLine:headerLine+samples]
        print(accessions)
        break

# set read pointer back to beginning of file
file.seek(0)

print('Header line is line '+str(headerLine)+"." '\n')

# go back to first line before first data lines
for line in range(headerLine):
    file.readline()


# start analyzing lines
for line in range(linesInFile - headerLine +1):
    # convert current_line into list elements_cl
    currentLine = file.readline()
    elementsCL = currentLine.split()


    alleleCounter = 0
    alleleDistribution = []
    missingCounter = 0
    missingDistribution = []
    # count accessions with variant, store in alleleDistribution
    # count accessions with missing info, store in missingDistribution
    for accession in range(9,samples+9):
        if elementsCL[accession].startswith('1|1'):
            alleleCounter += 1
            alleleDistribution.append(accessions[accession-9])
        elif elementsCL[accession].startswith('./.'):
            missingCounter += 1
            missingDistribution.append(accessions[accession-9])

    # add to variant list only if there are variants
    if alleleCounter > 0:
        # increment variantCounter
        variantCounter =+ 1
        # append instance of variant to variant list
        variantList.append(Variant())
        # positions: multiply chr with 1,000,000, add positions
        variantList[variantCounter-1].p = int(elementsCL[0]) * 1000000 + int(elementsCL[1])
        # record allele frequency
        variantList[variantCounter-1].f = alleleCounter
        # store info on accessions containing variant
        variantList[variantCounter-1].a = alleleDistribution
        # record missing data frequency
        variantList[variantCounter-1].m = missingCounter
        # store info on accessions with missing info
        variantList[variantCounter-1].md = missingDistribution
        # determine whether a position is a SNP or insertion or not, and if a SNP, what type of SNP
        ref = elementsCL[3]
        alt = elementsCL[4]
        # store info on variant sequence change
        variantList[variantCounter-1].v = ref + '|' + alt
        # store info on variant type
        if len(ref) > 1 and len(alt) == 1:
            variantList[variantCounter-1].t = 'delet'
        elif len(ref) == 1 and len(alt) > 1:
            variantList[variantCounter-1].t = 'inser'
        elif len(ref) > 1 and len(alt) > 1:
            variantList[variantCounter-1].t = 'cmplx'
        else:
            variantList[variantCounter-1].t = transitionTransversion[substitutionTypes.index(ref+alt)]
        # count missing data







        if int(elementsCL[1]) < 500 or int(elementsCL[1]) > 999000:
            variantList[variantCounter-1].print()




















