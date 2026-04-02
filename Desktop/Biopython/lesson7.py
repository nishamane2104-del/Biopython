import Bio
print(Bio.__version__)

from Bio.Seq import Seq

dna = Seq("ATGCGT")
print(type(dna)) 
from Bio.Seq import Seq

seq = Seq("ATGAATCGC")
print(seq)
# print(seq.complement())

rna = dna.transcribe()
print(rna)

print(rna.translate())
