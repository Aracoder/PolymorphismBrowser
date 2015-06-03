__author__ = 'weigel'
# This program will define a class "polymorphism"
# The objects will contain information on 1001 Genomes polymorphisms
# The methods will allow for interrogation of the polymorphisms

# global variables


# first line with DNA data
first_polymorphism = 0

# Read a .vcf file
file = open ('1001genomes_snp_short_indel_only_ACGTN_1Mb_100acc.vcf')

# find first line that does not start with ##
current_line = file.readline()
print('First line; is it a VCF file?', current_line)
if current_line.find('vcf', 0, len(current_line)):
    print('This is a .vcf file!')
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
    print(first, ' ', current_line)
    if first != '#':
        break

print(first_polymorphism)














