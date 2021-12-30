#!/bin/bash
echo "Ex1.py"
python3 src/ex1.py
echo "Test"
python3 tests/tests.py

echo "Running commands for Exercise 2: "
echo "Please make sure that STAR was run in the bioinformatics main folder"
echo "How many alignments were reported?"
    grep -v "@" Aligned.out.sam | wc -l
echo "How many reads were uniquely mapped?"
    grep NH:i:1 Aligned.out.sam | wc -l
echo "How many reads were mapped to multiple loci?"
    grep NH:i:2 Aligned.out.sam | wc -l
echo "+" 
    grep NH:i:3 Aligned.out.sam | wc -l
echo "+"
    grep NH:i:4 Aligned.out.sam | wc -l
echo "How many reads could not be mapped?"
    grep NH:i:0 Aligned.out.sam | wc -l

echo "Exercise 3: FASTA/FASTQ files have been created "
    cat Aligned.out.sam | grep -v ^@ | awk 'NR%2==1 {print "@"$1"\n"$10"\n+\n"$11}' > Aligned.out.fastq
    sed -n '1~4s/^@/>/p;2~4p' Aligned.out.fastq > Aligned.out.fasta


