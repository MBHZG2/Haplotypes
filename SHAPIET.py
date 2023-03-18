import os
import sys
POPULATION_SIZE = sys.argv[1]
RECOMBINATION_RATES = {"chr1": 0.36, "chr2": 0.62, "chr3": 0.71, "chr4": 0.67, "chr5": 0.84, "chr6": 0.79, "chr7": 0.79, "chr8": 0.65, "chr9": 0.70, "chr10": 0.99, "chr11": 0.74, "chr12": 0.90, "chr13": 0.45, "chr14": 0.67, "chr15": 0.60, "chr16": 0.67, "chr17": 0.79, "chr18": 0.80}
EXCLUDED_CHROMOSOMES = ["chr0", "chrX"]

with open(sys.argv[2]) as contig_file:

    for chromosome in contig_file:
        chromosome = chromosome.strip()  

        if chromosome in EXCLUDED_CHROMOSOMES:
            continue  

       
        command = "bin/shapeit --input-ped /{chromosome}.ped /{chromosome}.map -O /{chromosome}.phased --thread 4 --window 2 --rho {RECOMBINATION_RATES[chromosome]}"

        os.system(command)

