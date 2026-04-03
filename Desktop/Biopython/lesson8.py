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
