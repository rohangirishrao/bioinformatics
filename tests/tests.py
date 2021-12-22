""" Test module to test all the methods of ex1.py"""
import os
from src.ex1 import parse_fasta, discard_ambiguous_seqs, nucleotide_frequencies


def test_parse():
    """
    Test method to test the parse_fasta method

    """

    directory: str = "test_files"
    fname: str = os.path.join(directory, "ref.fasta")
    header, seqeunce = parse_fasta(fname)
    assert header == ['seq1', 'seq2']
    assert seqeunce == ['ATATATCGATTATCATCGTCGATCGTATTAT',
                        'ATTAGTCGATAGCTATTTAAATGCTCAACCT']


def test_discard():
    """
    Test method to test the discard ambiguous seqs method.

    """
    directory: str = "test_files"
    fname = os.path.join(directory, "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    content.close()

    seq = discard_ambiguous_seqs(string)
    assert seq == ['C', 'T', 'G', 'G', 'T', 'A', 'T', 'a', 'T', 't', 'A', 'G', 'g', 'g', 'T']


def test_freqs():
    """
    Test method to test the nucleotide frequencies method

    """
    directory: str = "test_files"
    fname = os.path.join(directory, "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    # print(string)
    content.close()

    frequencies = nucleotide_frequencies(string)
    print(frequencies)
    assert frequencies == [0.12, 0.06, 0.19, 0.31]
