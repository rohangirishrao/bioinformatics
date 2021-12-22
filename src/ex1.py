""" Module to run the exercises of session 1 in bioinformatics Block 3"""
import os


def parse_fasta(filename: str):
    """
    Method to parse a FASTA file
    Opens a file and reads the content and returns the sequence inside each separate block
    Denoted with '>' header before each sequence

    """
    stuff = open(filename, 'r').readlines()

    header: list = []
    sequence: list = []
    head = None
    seq = ""

    for line in stuff:
        if line.startswith('>'):
            header.append(line[1:-1])
            if head:
                sequence.append(seq)
            seq = ""
            head = line[1:]
        else:
            seq += line.rstrip()
    sequence.append(seq)

    return header, sequence


def discard_ambiguous_seqs(seq: list):
    """
    Method that discards sequences that don't contain the letters/nucleotides we are looking for

    """
    string = ""
    for part in seq:
        string.join(part)

    result_sequence: str = ""
    for part in string:
        if all(x in ('A', 'C', 'G', 'T', 'a', 'c', 'g', 't') for x in part):
            result_sequence.join(part)
    return result_sequence


def nucleotide_frequencies(string: str):
    """
    Method takes a list of strings as input and prints out total frequency of each nucleotide

    """
    # s = ["ATCGTAAAA", 'GCGCGACTCCC']
    length = len(string)
    a_list = []
    c_list = []
    g_list = []
    t_list = []

    for char in string:
        a_list.append(char.count('A'))
        c_list.append(char.count('C'))
        g_list.append(char.count('G'))
        t_list.append(char.count('T'))
    a_total = sum(a_list)
    c_total = sum(c_list)
    g_total = sum(g_list)
    t_total = sum(t_list)
    tot = 0

    for i in range(0, length):
        for j in range(0, len(string[i])):
            tot = tot + 1

    freq_a = round(a_total / tot, 2)
    freq_c = round(c_total / tot, 2)
    freq_g = round(g_total / tot, 2)
    freq_t = round(t_total / tot, 2)

    res: list = [freq_a, freq_c, freq_g, freq_t]

    return res


def print_frequencies(string: str):
    """
    Method to calculate and print the nucleotide frequencies.

    """
    freqs = nucleotide_frequencies(string)

    print('A: ', freqs[0],
          '\nC: ', freqs[1],
          '\nG: ', freqs[2],
          '\nT: ', freqs[3])


def map_reads(filename1: str, filename2: str):
    """
    Method takes 2 files and parses them, discarding sequences and printing frequencies.
    Additionally, returns a dictionary of dictionaries, where the outer dictionary uses
    the names of query sequences as its keys, and the inner dictionary uses reference
    sequence names as keys
    """
    head1, sequence1 = parse_fasta(filename1)
    head2, seq2 = parse_fasta(filename2)
    indices = []

    das1 = discard_ambiguous_seqs(sequence1)
    das2 = discard_ambiguous_seqs(seq2)

    print('Nucleotide frequencies for sequencesfasta.sec :')
    print_frequencies(das1)
    print('Nucleotide frequencies for genomesfasta.sec :')
    print_frequencies(das2)

    for seqpart in sequence1:
        for part in seq2:
            if seqpart in part:
                index = part.index(seqpart)
            else:
                index = 0
            indices.append(index)

    ind_list = [indices[i:i + len(seq2)] for i in range(0, len(indices), len(seq2))]

    dic: dict = {k: {v1: v2} for k, v1, v2 in zip(head1, head2, ind_list)}

    return dic


if __name__ == "__main__":
    # Uncomment this line if you want to run the script from the IDE
    # directory = "../tests/test_files"
    DIRECTORY = "tests/test_files"
    file1 = os.path.join(DIRECTORY, "sequencesfasta.sec")
    file2 = os.path.join(DIRECTORY, "genomefasta.sec")

    # Same here to run from an editor
    # file3 = os.path.join("../", "Aligned.out.fasta")
    file3 = os.path.join("", "Aligned.out.fasta")

    h, tup = parse_fasta(file1)
    print("Sequences in sequencesfasta.sec:\n ", tup)

    print(map_reads(file1, file2))

    h2, seq1 = parse_fasta(file3)
    print('-------------')
    print("\nNucleotide frequencies for Aligned.out.fasta: \n")

    S1 = discard_ambiguous_seqs(seq1)
    print(print_frequencies(S1))
