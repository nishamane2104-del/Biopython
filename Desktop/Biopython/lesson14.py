#How to read BLAST file in xml format
from Bio.Blast import NCBIXML 

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b) 

print(len(blast_record.alignments))