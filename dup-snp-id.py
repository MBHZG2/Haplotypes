import sys

with open(sys.argv[1]) as plink_map_file:
    chromosome_positions = {}
    SNP_positions = {}
    for line in plink_map_file:
        parts = line.split()
        SNP = parts[1]
        position = parts[-1]
        chromosome=parts[0]
        tag = chromosome+"#"+position
        chromosome_positions[SNP]=tag
        SNP_positions[tag]=SNP
    rev_dict = {}
    for key, value in chromosome_positions.items():
        rev_dict.setdefault(value, set()).add(key)

    result = [key for key, values in rev_dict.items() if len(values) > 1]
    for marker in result:
                print SNP_positions[marker]
