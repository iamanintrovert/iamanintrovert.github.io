#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:42:36 2019

@author: croc
"""

from pybtex.database import parse_file, BibliographyData, Entry
import re

def year_parser(entry):
    try:
        year = entry.fields['year'] 
    except:
        year = ""
    return year

def pages_parser(entry):
    try:
        pages = entry.fields['pages']
    except:
        pages = ""
    return pages

def number_parser(entry):
    try:
        number = entry.fields['number']
    except:
        number = ""
    return number

def volume_parser(entry):
    try:
        volume = entry.fields['volume']
    except:
        volume = ""
    return volume

def doi_parser(entry):
    try:
        doi = entry.fields['doi']
    except:
        doi = ""
    return doi

def author_parser(entry):
    authors = ""
    for author in entry.persons['author']:
        authors = authors = authors + author.first_names[0] + ' ' +author.last_names[0] + ', '
    authors = authors[:-2] # for removing last ', '
    return authors

def article_parser(entry):
    key = entry.key
    title = entry.fields['title']
    publisher = re.sub('{|}','',entry.fields['journal']) # for removing {}
    authors = author_parser(entry)
    volume = volume_parser(entry)
    number = number_parser(entry)
    pages = pages_parser(entry)
    year = year_parser(entry)
    bibtex = BibliographyData({entry.key:entry}).to_string('bibtex')
    doi = doi_parser(entry)
    article_dict = dict([('key',key),('author',authors),('title',title),('publisher',publisher),('volume',volume),('number',number),('pages',pages),('year',year),('bibtex',bibtex),('doi',doi)])
    return article_dict
        
def inproceedings_parser(entry):
    key = entry.key
    title = entry.fields['title']
    publisher = re.sub('{|}','',entry.fields['booktitle'])
    authors = author_parser(entry)
    volume = volume_parser(entry)
    number = number_parser(entry)
    pages = pages_parser(entry)
    year = year_parser(entry)
    bibtex = BibliographyData({entry.key:entry}).to_string('bibtex')
    doi = doi_parser(entry)
    inproceedings_dict = dict([('key',key),('author',authors),('title',title),('publisher',publisher),('volume',volume),('number',number),('pages',pages),('year',year),('bibtex',bibtex),('doi',doi)])
    return inproceedings_dict
        