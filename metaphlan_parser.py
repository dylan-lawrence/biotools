#Convert bulk metaphlan data to an easy to use, R compatible format
#
#Step 1: Convert all metaphlan output files using 'metahplan2krona.py' (included in metaphlan2 software)
#Step 2: Run this program, specify directory containing "krona-ized" files as argument
#Step 3: Output file can be easily imported into R
#
#Note: this program chooses to remove strain level assignments due to the strange way metaphlan treats this data

import sys
import os

#specify directory of metaphlan output files

files=sys.argv[1]

output=['Sample\tAbundance\tKingdom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\n']

for f in os.listdir(files):
    sample=f.rstrip('.txt')
    data=[]
    with open(files + '/' + f) as temp: data=[x.rstrip('\n').split('\t') for x in temp.readlines()]

    for line in data:
        if line[1] == 'unclassified':
            output.append(sample + '\t' + line[0] + '\t' + line[1] + '\n')
        elif len(line) < 10:
            print(line)
            output.append(sample + '\t' + line[0] + '\t' + '\t'.join(line[2:9]) + '\n')


with open("all_data.txt",'w') as f:
    for line in output: f.write(line)     
    