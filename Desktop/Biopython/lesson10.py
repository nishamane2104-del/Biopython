from Bio import SeqIO

for record in SeqIO.parse("cox1.fasta", "fasta"):
    print(record.id)
    print(record.description)
    print(len(record))
    print(">"*50)