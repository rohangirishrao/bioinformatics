import os
import pytest
from ex1 import *

"""
Test method to test the parse_fasta method

"""


def test_parse():
    directory = "C:\\Users\\droon\\OneDrive\\Desktop\\UNI\\Semester 5\\" \
                "Programming in Bioinformatics\\Exercises Block 3\\tests\\test_files"
    fname = os.path.join(directory, "ref.fasta")
    h, s = parse_fasta(fname)
    assert h == ['seq1', 'seq2']
    assert s == [['ATATATCGATTATCATCGTCGATCGTATTAT'],
                 ['ATTAGTCGATAGCTATTTAAATGCTCAACCT']]


"""
Test method to test the discard ambiguous seqs method.

"""


def test_discard():
    directory = "C:\\Users\\droon\\OneDrive\\Desktop\\UNI\\Semester 5\\" \
                "Programming in Bioinformatics\\Exercises Block 3\\tests\\test_files"
    fname = os.path.join(directory, "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    content.close()

    seq = discard_ambiguous_seqs(string)
    assert seq == ['C', 'T', 'G', 'G', 'T', 'A', 'T', 'a', 'T', 't', 'A', 'G', 'g', 'g', 'T']


"""
Test method to test the nucleotide frequencies method

"""


def test_freqs():
    directory = "C:\\Users\\droon\\OneDrive\\Desktop\\UNI\\Semester 5\\" \
                "Programming in Bioinformatics\\Exercises Block 3\\tests\\test_files"
    fname = os.path.join(directory, "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    # print(string)
    content.close()

    nf = nucleotide_frequencies(string)
    print(nf)
    assert nf == (0.12, 0.06, 0.19, 0.31)
