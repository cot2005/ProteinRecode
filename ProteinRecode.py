#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:12:09 2019

@author: Colin Tang

Script to recode the nucleotide sequence of a protein sequence

inputs are .txt files. AACodonFile is tab delimited with codons comma delimited
"""
    
import random
    
def ProteinRecode(proteinSeqFile, AACodonFile, outputName = "outputSeq.txt"):
    #builds AA codon dictionary
    with open(AACodonFile) as a: 
        AAcodonList = a.read().splitlines()
        a.close()
    
    AAcodonDict = {}
    for i in AAcodonList:
        AArow = i.split("\t")
        AAcodonDict[AArow[0]] = AArow[1].split(",")
    #gets protein sequence from input file
    with open(proteinSeqFile) as p: 
        protSeq = p.read().strip("\n")
        p.close()    
        
    aaList = list(protSeq)
    translatedSeq = list()
    #loop to translate peptide sequence to nucleotide codon randomly
    for i in aaList:
        translatedSeq.append(random.choice(AAcodonDict[i]))
    recoded = "".join(translatedSeq)
    with open(outputName, "w") as textFile:
        textFile.write(recoded)
        textFile.close()