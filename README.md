## Programming in Bioinformatics

This is the README that contains instructions and answers to the exercises of Block 3.

### Exercise 1
The code for the first exercise is in the folder marked src under ex1.py.

To run the code, replace the string on line 164 in ex1.py to the directory of the location of the files and run the script.


From the result of map_reads, we can see that some sequences do not appear in others. The final sequence, which is the shortest one, 
is the one that has the most presence in others. The first few have multiple 0's in them. This makes sense, as the final sequence is 
far shorter than the others, making it more likely to occur in the others than the first few sequences.

### Exercise 2
The commands for running STAR are taken from the STARManual and are not linked explicitly.

Additionally, please make sure that STAR was run in the main folder, as the script assumes the `Aligned.out.sam` is in this folder.
#### 2.2
i) **How many alignments were reported?**

`grep -v "@" Aligned.out.sam | wc -l`

108

ii) **How many reads were uniquely mapped?**

`grep NH:i:1 Aligned.out.sam | wc -l`

0

iii) **How many reads were mapped to multiple loci?**

`grep NH:i:2 Aligned.out.sam | wc -l`
`grep NH:i:3 Aligned.out.sam | wc -l`
`grep NH:i:4 Aligned.out.sam | wc -l`

108 (100: x2 8: x4)

iv) **How many reads could not be mapped?**

`grep NH:i:0 Aligned.out.sam | wc -l`

0

### Exercise 3

i) `cat Aligned.out.sam | grep -v ^@ | awk 'NR%2==1 {print "@"$1"\n"$10"\n+\n"$11}' > Aligned.out.fastq`

ii) `sed -n '1~4s/^@/>/p;2~4p' Aligned.out.fastq > Aligned.out.fasta`

The ex1.py file already runs the Aligned.out.fasta file and analyzes the nucleotide frequencies.
