#!/bin/bash

# Usage: bash script.sh <input plink file prefix> <output directory> <SHAPEIT2 options>

# Set variables
input=$1
outdir=$2
shapeit2_opts=$3

# Filter out low frequency variants and genotyping call rate
plink --bfile $input --make-bed --allow-extra-chr --mind 0.1 --geno 0.1 --maf 0.01 --recode --out $input.filtered

# Split the plink format files to chromosomes. One file for each chromosome.
# contigs.txt contains chromosome IDs, one per line (e.g. chr1, chr2, chr3, etc.)
for chr in $(cat contigs.txt); do
    plink --noweb --file $input.filtered --chr $chr --allow-extra-chr --recode --out $outdir/$chr
done

# Check for duplicated SNPs (markers at the same position)
for chr in $(cat contigs.txt); do
    python2 dup-snp-id.py $outdir/$chr.map > $outdir/$chr.lista.dup
done

# Exclude duplicated SNPs and filter the remaining variants
for chr in $(cat contigs.txt); do
    plink --noweb --file $outdir/$chr --exclude $outdir/$chr.lista.dup --allow-extra-chr --recode --out $outdir/$chr.filteredDuplicates
done

# Run SHAPEIT2 on the filtered and non-duplicated data
python2 SHAPIET.py $outdir $shapeit2_opts $outdir/contigs.txt

