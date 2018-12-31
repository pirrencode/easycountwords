# -*- coding: utf-8 -*-
"""
Easy Count Words

Created on Mon Dec 31 13:55:12 2018

Counts the number of individual words and symbols in a string.

@author: pirrencode
"""

text = input("Please enter text and I will return number of words. ")

countsymbols = len(text)

countwords = len(text.split())

print("This text contents " + str(count) + " words and " + str(countsymbols) + " characters. Thanks for using EasyCountWords!")