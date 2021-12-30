""" Test module to test all the methods of ex1.py"""
import os
from pathlib import Path

from src.ex1 import parse_fasta, discard_ambiguous_seqs, nucleotide_frequencies

directory: Path = Path(__file__).parents[0] / "test_files"


def test_parse():
    """
    Test method to test the parse_fasta method

    """
    fname: str = str(directory / "ref.fasta")
    header, seqeunce = parse_fasta(fname)
    assert header == ['seq1', 'seq2']
    assert seqeunce == ['ATATATCGATTATCATCGTCGATCGTATTAT',
                        'ATTAGTCGATAGCTATTTAAATGCTCAACCT']


def test_discard():
    """
    Test method to test the discard ambiguous seqs method.

    """
    fname: str = str(directory / "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    content.close()
    list_of = []
    for stuff in string:
        list_of.append(stuff)

    seq = discard_ambiguous_seqs(list_of)
    assert seq == 'CTGGTATaTtAGggT'


def test_freqs():
    """
    Test method to test the nucleotide frequencies method

    """
    fname: str = str(directory / "q.fasta")

    content = open(fname, 'r')
    string = content.read()
    # print(string)
    content.close()

    frequencies = nucleotide_frequencies(string)
    print(frequencies)
    assert frequencies == [0.12, 0.06, 0.19, 0.31]
