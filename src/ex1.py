# import numpy as np
import os

"""
Method to parse a FASTA file
Opens a file and reads the content and returns the sequence inside each separate block
Denoted with '>' header before each sequence

Args:
    filename (string): name of the file to be parsed

Return:
    A tuple with the header line and the sequence

"""


def parse_fasta(filename):
    stuff = open(filename, 'r').readlines()

    header = []
    sequence = []
    head = None
    seq = ""

    for l in stuff:
        if l.startswith('>'):
            header.append(l[1:-1])
            if head:
                sequence.append(seq)
            seq = ""
            head = l[1:]
        else:
            seq += l.rstrip()
    sequence.append(seq)

    return header, sequence


"""
Method that discards sequences that don't contain the letters we are looking for

Args:
    string (string): string containing all nucleotides

Return:
    A list of nucleotides that only contain our interesting nucleotides

"""


def discard_ambiguous_seqs(seq):
    string = ""
    for l in seq:
        string += l

    resSeq = ""
    for l in string:
        if all(x in ('A', 'C', 'G', 'T', 'a', 'c', 'g', 't') for x in l):
            resSeq += l
    return resSeq


"""
Method takes a list of strings as input and prints out total frequency of each nucleotide

Args:
    string (string) : list of strings containing nucleotides

"""


def nucleotide_frequencies(string):
    # s = ["ATCGTAAAA", 'GCGCGACTCCC']
    l = len(string)
    A = []
    C = []
    G = []
    T = []

    for char in string:
        A.append(char.count('A'))
        C.append(char.count('C'))
        G.append(char.count('G'))
        T.append(char.count('T'))
    Atot = sum(A)
    Ctot = sum(C)
    Gtot = sum(G)
    Ttot = sum(T)
    tot = 0

    for o in range(0, l):
        for x in range(0, len(string[o])):
            tot = tot + 1

    freqA = round(Atot / tot, 2)
    freqC = round(Ctot / tot, 2)
    freqG = round(Gtot / tot, 2)
    freqT = round(Ttot / tot, 2)

    res = [freqA, freqC, freqG, freqT]

    return res


"""
Method to calculate and print the nucleotide frequencies.

Args:
    string: A string of nucleotides
"""


def printNF(string):
    freqs = nucleotide_frequencies(string)

    print('A: ', freqs[0],
          '\nC: ', freqs[1],
          '\nG: ', freqs[2],
          '\nT: ', freqs[3])


"""
Method takes 2 files and parses them, discarding sequences and printing frequencies. Additionally, returns a dictionary
of dictionaries, where the outer dictionary uses the names of query sequences as its keys, and the inner dictionary uses
reference sequence names as keys

Args:
    filename1 (string): name of first file
    filename2 (string): name of second file
    
Returns: 
    dic (dictionary): dictionary with query sequences as keys, and inner dict reference sequences

"""


def map_reads(filename1, filename2):
    head1, seq1 = parse_fasta(filename1)
    head2, seq2 = parse_fasta(filename2)
    indices = []

    s1 = discard_ambiguous_seqs(seq1)
    s2 = discard_ambiguous_seqs(seq2)

    print('Nucleotide frequencies for sequencesfasta.sec :')
    printNF(s1)
    print('Nucleotide frequencies for genomesfasta.sec :')
    printNF(s2)

    for l in seq1:
        for x in seq2:
            if l in x:
                index = x.index(l)
            else:
                index = 0
            indices.append(index)

    ind_list = [indices[i:i + len(seq2)] for i in range(0, len(indices), len(seq2))]

    dic = {k: {v1: v2} for k, v1, v2 in zip(head1, head2, ind_list)}

    return dic


"""
Main method to run the parse functions on FASTA files and print nucleotide frequencies.

"""
if __name__ == "__main__":
    # Add your directory here
    directory = "..\\tests\\test_files"
    file1 = os.path.join(directory, "sequencesfasta.sec")
    file2 = os.path.join(directory, "genomefasta.sec")
    # Path of the directory where STAR was run, assumed to be the main folder
    file3 = os.path.join("..\\", "Aligned.out.fasta")

    h, tup = parse_fasta(file1)
    print("Sequences in sequencesfasta.sec:\n ", tup)

    print(map_reads(file1, file2))

    h2, seq1 = parse_fasta(file3)
    print('-------------')
    print("\nNucleotide frequencies for Aligned.out.fasta: \n")

    s1 = discard_ambiguous_seqs(seq1)
    print(printNF(s1))
