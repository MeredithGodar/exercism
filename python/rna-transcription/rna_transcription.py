import re


def to_rna(dna):
    if re.search(r"[^GCTA]", dna):
        return ''
    else:
        return dna.translate(str.maketrans("GCTA", "CGAU"))
