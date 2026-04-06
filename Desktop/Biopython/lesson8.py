# what is SEQRECORD?
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord 
dna = Seq("ATGCGT")

record = SeqRecord(
    dna,
    id = "Gene1",
    name = "Example gene",
    description = "Sample DNA seq for Practice"
) 

print(record.id)
print(record.name)
print(record.description)
print(record.seq)




protein_seq= Seq("MKTLLV")

protein_record = SeqRecord(
    protein_seq,
    "Prot01" ,
    "Test Protein",
    "Sample protein sequence for practice"
)

print(protein_record.id)
print(protein_record.name)
print(protein_record.description)
print(protein_record.seq)


# Que 1 
"""
Create a DNA sequence "ATGCGT" using Biopython 
and print the sequence.
"""
from Bio.Seq import Seq
DNA = Seq("ATGCGT") 
print(DNA)

# Que 2
"""
Given the DNA seq "ATGC", 
write code to print:
- Complement 
- Transcribed Rna 
"""
from Bio.Seq import Seq
seq = Seq("ATGC")
print("Complement:", seq.complement())
print("Transcribed RNA:", seq.transcribe()) 

# Que 3
"""
create two SeqRecords:
ID = "GeneA", sequence = "ATGC"
ID = "GeneB", sequence = "CGTA"

Store them in a list and print each ID using a for loop 
"""
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord 
record1 = SeqRecord(Seq("ATGC"), id="GeneA")
record2 = SeqRecord(Seq("CGTA"), id="GeneB")

records = [record1, record2]

for record in records:
    print(record.id)