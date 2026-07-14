from Bio import SeqIO

def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    return (g_count+c_count)/len(sequence)*100

for record in SeqIO.parse("day03\sample.fasta","fasta"):
    print("="*30)
    print("ID:" ,record.id)
    print("Lenght:",len(record.seq))
    print("Sequence:",record.seq)
    sequence = str(record.seq)
    calculate_gc_content = gc_content(sequence)
    print(f"GC content: {calculate_gc_content:.2f}%")
