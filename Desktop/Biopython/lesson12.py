# Sequence similarity 
# BLAST : Basic Local Alignment Search Tool
from Bio.Blast import NCBIWWW 

result_handel = NCBIWWW.qblast(
    program = "blastp",
    database = "nr", # non-redundant protein sequence database  
    sequence = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
)

with open ("blast_result.xml", "w") as b :
    b.write(result_handel.read())