import sys

with open(sys.argv[1]) as plink_map_file:
    chromosome_positions = {}
    for line in plink_map_file:
        parts = line.split()
        chromosome = parts[0]
        position = parts[-1]
        key = "{chromosome}#{position}"
        chromosome_positions[key] = parts

    positions_to_check = set(key for key in chromosome_positions if list(chromosome_positions).count(key) > 1)
    for position in sorted(positions_to_check):
        print(chromosome_positions[position][1])
