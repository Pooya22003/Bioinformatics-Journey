dna_sequence = input("Insert Your Sequence:\n").upper()

valid_bases = {"A", "T", "G", "C"}

print("="*30)
print("DNA Analyzer")
print("="*30)


def valid_sequence(sequence):

    if len(sequence) == 0:
        print("Sequence is empty")
        return False

    for base in sequence:
        if base not in valid_bases:
            print("Validation Status: Invalid bases")
            return False

    print("Validation Status: Valid bases")
    return True


if not valid_sequence(dna_sequence):
    exit()

print("=" * 30)
print(f"Sequence: {dna_sequence}")

length = len(dna_sequence)

a_count = dna_sequence.count("A")
t_count = dna_sequence.count("T")
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

gc_content = (g_count + c_count) / length * 100

print(f"Length     : {length}")
print(f"A Count    : {a_count}")
print(f"T Count    : {t_count}")
print(f"G Count    : {g_count}")
print(f"C Count    : {c_count}")
print(f"GC Content : {gc_content:.2f}%")

print("=" * 30)
