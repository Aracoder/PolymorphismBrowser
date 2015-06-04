__author__ = 'weigel'
# This program will define a class "polymorphism"
# The objects will contain information on 1001 Genomes polymorphisms
# The methods will allow for interrogation of the polymorphisms

# global variables

# the four bases
DNAbases = ['A','G','C','T']
# first line with DNA data
first_polymorphism = 0
snplist = []
# number of genotypes
samples = 0


# generate list of potential SNPs consisting of two letters and of SNP types
# substitution_types = ['AA', 'AG', 'AC', 'AT', 'GA', 'GG', 'GC', 'GT', 'CA', 'CG', 'CC', 'CT', 'TA', 'TG', 'TC', 'TT']
# transition_transversion = ['notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP', 'trvsn', 'trvsn', 'trvsn', 'trvsn', 'notaSNP', 'trstn', 'trvsn', 'trvsn', 'trstn', 'notaSNP']

substitution_types = []
transition_transversion = []
numbers = []
for ref in range(4):
    for alt in range(4):
        substitution_types.append(DNAbases[ref] + DNAbases[alt])
        if ref == alt:
            transition_transversion.append('notaSNP')
        elif (ref+alt) in [1,5]:
            transition_transversion.append('trstn')
        else:
            transition_transversion.append('trvsn')


# define class SNP
class SNP:
    def __init__(self, position=0, snp='', snptype='', annotation='', methylation=''):
        self.p = position
        self.s = snp
        self.t = snptype
        self.a = annotation
        self.m = methylation

    def print(self):
        print(self.p, self.s, self.t)

# Read a .vcf file
file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

# count lines in file
with file as f:
    for lines_in_file, l in enumerate(f):
        pass

file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

file.seek(0)

# determine whether it's a VCF file
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

# find header line
for line in range(100):
    first_polymorphism += 1
    current_line = file.readline()
    elements_cl = current_line.split()
    if elements_cl[0] == '#CHROM':
        samples = len(elements_cl) - 9
        print("samples", samples)
        break

# set read pointer back to beginning of file
file.seek(0)

print('First line with genotype information is line ',first_polymorphism, '\n')

# go back to first line before polymorphism
for line in range(first_polymorphism):
    file.readline()

# start analyzing lines

for line in range(lines_in_file - first_polymorphism + 1):
# for line in range(6):
    # convert current_line into list elements_cl
    current_line = file.readline()
    elements_cl = current_line.split()
    # positions: multiply chr with 1,000,000, add positions
    snplist.append(SNP())
    snplist[line].p = int(elements_cl[0]) * 1000000 + int(elements_cl[1])
    # determine whether a position is a SNP or insertion or not, and if a SNP, what type of SNP
    ref = elements_cl[3]
    alt = elements_cl[4]
    change = ref + alt
    if not change in substitution_types:
        snplist[line].s = 'notaSNP'
        snplist[line].t = 'NA'
    else:
        snplist[line].s = change
        snplist[line].t = transition_transversion[substitution_types.index(change)]
    if int(elements_cl[1]) < 100 or int(elements_cl[1]) > 999400:
        snplist[line].print()



















