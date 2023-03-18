# Haplotypes
Haplotypes from SNP beadchip
you can run the bash script Filtering-phasing-dataset.sh


SNP Filtering and Phasing with SHAPEIT2


Filtering SNPs
First, filter the PLINK dataset using your desired parameters. Here's an example using PLINK

Identifying Duplicate SNPs
To identify duplicate SNPs in the filtered dataset, run dup-snp-id.py

Haplotype Phasing
To phase the filtered dataset, run SHAPEIT.py
This will produce a new dataset with phased haplotypes (my_phased_dataset.haps and my_phased_dataset.sample).
Note that the recombination rates used in SHAPEIT.py are for the sus-scrofa genome. If you are working with human data, you can use a genomic map appropriate for human data.



Dependencies:

This project requires the following dependencies:

Python 2.7 or later

SHAPEIT2 (available from https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.html)

PLINK (available from https://www.cog-genomics.org/plink/)
