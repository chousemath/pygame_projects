dna_rna_mapping = {
    'A': 'U',
    'T': 'A',
    'G': 'C',
    'C': 'G',
}
def dna_to_rna(dna):
    rna = ''
    for c in dna:
        rna += dna_rna_mapping[c]
    return rna

# one line version of the function
# def dna_to_rna(dna): return ''.join([dna_rna_mapping[c] for c in dna])

ans1 = dna_to_rna("ATTAGCGCGATATACGCGTAC")
exp1 = "UAAUCGCGCUAUAUGCGCAUG"
assert ans1 == exp1, f'Expected {exp1}, got {ans1}'

ans2 = dna_to_rna("CGATATA")
exp2 = "GCUAUAU"
assert ans2 == exp2, f'Expected {exp2}, got {ans2}'

ans3 = dna_to_rna("GTCATACGACGTA")
exp3 = "CAGUAUGCUGCAU"
assert ans3 == exp3, f'Expected {exp3}, got {ans3}'

print('Everything okay')
