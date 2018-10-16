#!/usr/bin/env python

#To display menu for user to make selection
# 1 Translate a protein-coding nucleotide sequence to amino acids
# 2 Randomly draw a codon from the sequence

print (30 * "-" , "MENU" , 30 * "-")
print ("Select an option below by entering the number")
selection = input ("(1) translate a protein-coding nucleotide sequence to amino acids -or- (2) randomly draw a codon from sequence: ")
print (67 * "-")

DnaSeq = input("Enter your DNA Sequence: ")

#In case any of the sequence is not uppercase, this will make it uppercase so the rest of the script runs correctly
DnaSeq = DnaSeq.upper()

#Both options will need an RNA codon, so it is easier to translate it before the rest of the script

RnaSeq = DnaSeq.replace("T","U")

#Dictionary to translate codons to amino acids

codon = {
'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',

'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',

'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',


'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
}

#Option 1
if selection == "1":
	AminoAcidSequence = ""
	for i in range(0, len(RnaSeq), 3):
			if RnaSeq[i:i+3] in codon:
				AminoAcidSequence += codon[RnaSeq[i:i+3]]
	print ("Amino Acid Sequence: ")
	print (AminoAcidSequence)

#Option 2
elif selection == "2":
	DnaSeq = DnaSeq.upper()
	codon = [DnaSeq[n:n+3] for n in range(0, len(RnaSeq), 3)]
	print(codon)
	import random
	randomCodon = random.choice(codon)
	print(randomCodon)
