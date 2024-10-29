#!/usr/bin/env python3
'''
Created on: 2024-10-28
Author: Matthew Spriggs
Description: Practicals from Introduction to bioinformatics using python :: Cranfield University

'''

sequence1 = "GAGCCTACTAACGGGAT"
sequence2 = "CATCGTAATGACGGCCT"

distance = 0
alignment = ''

for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
        distance += 1
        alignment += '|'
    else:
        alignment += ' '

print("The hamming distance: ", distance)

print(sequence1)
print(alignment)
print(sequence2)