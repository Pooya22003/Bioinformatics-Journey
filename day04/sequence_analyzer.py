"""
Day 04 - DNA Sequence Analyzer

Analyze DNA sequences from a FASTA file using Biopython.
"""

from Bio import SeqIO


def count_bases(sequence):
    """Count each nucleotide in a DNA sequence."""

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
    }


def calculate_gc_content(sequence):
    """Calculate GC content percentage."""

    if len(sequence) == 0:
        return 0

    bases = count_bases(sequence)

    return (bases["G"] + bases["C"]) / len(sequence) * 100


def calculate_at_content(sequence):
    """Calculate AT content percentage."""

    if len(sequence) == 0:
        return 0

    bases = count_bases(sequence)

    return (bases["A"] + bases["T"]) / len(sequence) * 100


def analyze_sequence(sequence):
    """Analyze a DNA sequence."""

    return {
        "length": len(sequence),
        "bases": count_bases(sequence),
        "gc_content": calculate_gc_content(sequence),
        "at_content": calculate_at_content(sequence),
    }


def display_result(record_id, sequence, result):
    """Display analysis result."""

    print("=" * 40)
    print(f"ID          : {record_id}")
    print(f"Sequence    : {sequence}")
    print(f"Length      : {result['length']}")
    print(f"A Count     : {result['bases']['A']}")
    print(f"T Count     : {result['bases']['T']}")
    print(f"G Count     : {result['bases']['G']}")
    print(f"C Count     : {result['bases']['C']}")
    print(f"GC Content  : {result['gc_content']:.2f}%")
    print(f"AT Content  : {result['at_content']:.2f}%")
    print("=" * 40)
    print()


def main():
    """Main program."""

    fasta_file = "sample.fasta"

    for record in SeqIO.parse(fasta_file, "fasta"):

        sequence = str(record.seq).upper()

        result = analyze_sequence(sequence)

        display_result(record.id, sequence, result)


if __name__ == "__main__":
    main()
