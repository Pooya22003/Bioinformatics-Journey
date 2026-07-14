from Bio import SeqIO

for record in SeqIO.parse("day03\sample.fasta","fasta"):
    print(len(record.seq))
