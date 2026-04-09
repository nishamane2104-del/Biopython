from Bio.Blast import NCBIXML

with open("blast_result.xml") as result_handle:
    blast_records = NCBIXML.parse(result_handle)

    for blast_record in blast_records:
        for alignment in blast_record.alignments[:5]:  # top 5 hits
            for hsp in alignment.hsps:
                print("Sequence:", alignment.title)
                print("Length:", alignment.length)
                print("E-value:", hsp.expect)
                print("Identity:", hsp.identities)
                print("-" * 50)
                