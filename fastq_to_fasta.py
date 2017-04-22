"""
Converts fastq to fasta file format
"""

import sys

f = open(sys.argv[1])
fout =(sys.argv[2])

fout = open(fout, 'a')

counter = 0

#counter2 = 0

for each_line in f:
        each_line = each_line.replace("\n","")
        if counter % 4 == 0:
                header = each_line
                fout.write(">" + header + "\n")
        elif (counter - 1) % 4 == 0:
                seq = each_line
                fout.write(seq + "\n")
        counter += 1


f.close()
~           
