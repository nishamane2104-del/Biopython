# # Sequence similarity 
# # BLAST : Basic Local Alignment Search Tool
from Bio.Blast import NCBIWWW

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence="MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
)

with open("blast_result.xml", "w") as file:
    file.write(result_handle.read())

print("BLAST search completed and results saved to blast_result.xml")