#How to read BLAST file in xml format
from Bio.Blast import NCBIXML 

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b) 

print(len(blast_record.alignments))

first_alignment = blast_record.alignments[0]
# print("Title:", first_alignment.title)
# print("Length:", first_alignment.length)

# for a in blast_record.alignments:
#     print(a.title)
   
print(len(first_alignment.hsps))

first_hsp = first_alignment.hsps[0]
print(first_hsp.score)
print(first_hsp.expect)