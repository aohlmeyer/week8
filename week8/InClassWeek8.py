#!/usr/bin/env python

#to notion user to input DNA sequence 

dnaSeq = input("Enter your DNA sequence: ")

#to convert to lowercase

dnaSeq = dnaSeq.lower() 

#to make the complimentary strnd

dnaSeq = dnaSeq.replace("c", "G")
dnaSeq = dnaSeq.replace("a", "T")
dnaSeq = dnaSeq.replace("t", "A")
dnaSeq = dnaSeq.replace("g", "C")

#to print the reverse order

print(dnaSeq[::-1])
