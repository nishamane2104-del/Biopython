# cox1.fasta 
# from Bio import SeqIO  
# record = SeqIO.read("cox1.fasta", "fasta")
# print(record.id)
# print (record.description)
# print(len(record)) 
# # print(record.seq)

# cox1.gb (GenBank file)
from Bio import SeqIO 
record = SeqIO.read("cox1.gb", "genbank")
# print(record.id)
# print(record.description)
# print(record.annotations)
print(len(record.features))

for features in record.features:
    print(features.type, features.location)
#insulin
# from Bio import SeqIO
# record = SeqIO.read("insulin.fasta", "fasta")
# print(record.id)
# print(record.description)
# print(len(record))


