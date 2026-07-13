from Bio.Seq import Seq
DNA = Seq(input("Enter DNA sequence: ")).strip().upper()

print("="*30)
print("Biopython Analyzer")
print("="*30)

print(f"DNA               : {DNA}")
print(f"Lenght            : {len(DNA)}")
print(f"RNA               : {DNA.transcribe()}")
print(f"Protein           : {DNA.translate()}")
print(f"Rrverse complement: {DNA.reverse_complement()}")

print("\nBase Counts")
print(f"A : {DNA.count("A")}")
print(f"T : {DNA.count("T")}")
print(f"G : {DNA.count("G")}")
print(f"C : {DNA.count("C")}")

print("="*30)
