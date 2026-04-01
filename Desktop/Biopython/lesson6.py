# handling DNA sequences in Python
seq = ["ATGC", "GGCTA", "TTAAC"] #LIST 
print(type(seq))
# indexing in list 
seq = ["ATGC", "GGCTA", "TTAAC"] 
#        0       1         2 

# two types of lenght : 
# print(len(seq)) # gives the number of items in the list
# print(len(seq[1])) # gives the number of characters in the second item of the list

# # for Loop in python 
# for s in seq: # look inside the variable seq and assign each item to the variable s one by one
#     print(s)

# genes = ["BRCA1", "TP53", "EGFR", "VEGFA"]
# for gene in genes:
#     print(gene)

# fruits = ["apple", "banana", "cherry", "date"]
# for fruit in fruits:
#     print(fruit)

# dna_seq = ["ATGC", "CGTAA", "TTGCA"]
# print(type(dna_seq))

dna_seq = ["ATGC", "CGTAA", "TTGCA"]
"""
Print:
the first nucleotide of the second sequence 
the last nucleotide of the third sequence
"""
print("The first nucleotide of the second sequence is", dna_seq[1][0])
print("The last nucleotide of the third sequence is", dna_seq[2][-1])