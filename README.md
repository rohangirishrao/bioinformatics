## Programming in Bioinformatics

This is the README that contains instructions and answers to the exercises of Block 3.

### Exercise 1
The code for the first exercise is in the folder marked src under ex1.py.

To run the code, running the bash script `run_me.sh` should run the script ex1.py and the tests. If this does not work,
the reason could be because of the path chosen, as the IDE I used needed different path signifiers than a command line. 

The current state of the code is to be run from the BASH script. If you wish to run it from an editor, please uncomment
the lines 131 and 137, as the path that an editor needs isn't the same as the path that the bash script needs, for whatever reason. 
I tried to fix this issue, but somehow the path is taken from the location of the bash script and not the script path.

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

Unfortunately, the bash script seems to have some sort of issue with running correctly. The individual commands run without
issue, but the script as a whole cannot find the relevant files and fails at finding options that the command line gets easily.
It actually worked perfectly for a long time, right until I was about to submit. 

I hope I can still get some points for the script, as I believe that the code and the thought process is correct behind it. 
I had changed nothing in the script and it worked correctly, but I must have changed something else, and it screwed it up. 

Thanks! 
