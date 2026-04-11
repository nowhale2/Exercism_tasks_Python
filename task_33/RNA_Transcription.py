def to_rna(dna_strand):
    dict_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    new_dna_strand = ""
    for symbol in dna_strand:
        new_dna_strand += dict_rna[symbol]
    return new_dna_strand
        
