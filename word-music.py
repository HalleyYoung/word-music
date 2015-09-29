# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 15:54:28 2014

@author: halley
"""
from nltk.book import *
import nltk
import music21helpers as mh
import sys

f = open(sys.argv[1], 'w+')
text = f.read()

letter_map = {'a':0, 'e':12, 'i':7, 'o':5, 'u':4, 's':2, 'r':9, 'l':11}
pits = []
for letter in text:
    if letter in letter_map:
        pits.append(letter_map[letter] + 48)
    else:
        pits.append(62)

part = mh.listsToPart(pits, [0.5 for i in pits])
part.write(fp=sys.argv[2], fmt='xml')