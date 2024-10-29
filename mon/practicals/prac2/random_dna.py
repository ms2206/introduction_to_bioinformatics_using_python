from random import choices, randint, choice

nucleotides = ['A', 'G', 'C', 'T']

sequence = choices(nucleotides, k=100)
mutated_DNA = sequence

sequence_string = ''.join(sequence)

mutation_site = randint(0, len(mutated_DNA))

mutated_DNA[mutation_site] = choice(nucleotides)

mutated_DNA = ''.join(sequence)

# print(sequence_string)
# print(mutated_DNA)
# print(mutation_site)


def complement(nucliodide: str) -> str:
    match nucliodide:
        case 'A':
            return 'T'
        case 'T':
            return 'U'
        case 'G':
            return 'C'
        case 'C':
            return 'G'


rna = []
for base in sequence:

    rna += complement(base)

# print(sequence_string)
# print(''.join(rna))


def dna_generator(n):
    nucleotides = ['A', 'G', 'C', 'T']

    sequence = choices(nucleotides, k=n)


    sequence_string = ''.join(sequence)

    return sequence_string