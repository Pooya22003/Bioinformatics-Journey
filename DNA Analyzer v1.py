dna = "ATGCGTAGCTA"

print(f"Sequence: {dna}")
length = len(dna)
print(f"Lenghth: {length}")

a = dna.count("A")
g = dna.count("G")
c = dna.count("C")
t = dna.count("T")

print(f"A count: {a}")
print(f"G count: {g}")
print(f"C count: {c}")
print(f"T count: {t}")

def calculate_gc(sequence):
    g = dna.count("G")
    c = dna.count("C")

    gc = (g+c)/len(sequence)*100

    return gc

result = calculate_gc(dna)
print(f"GC content: {result:2f}%")
