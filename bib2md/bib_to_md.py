#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:55:49 2019

@author: croc
"""

from pybtex.database import parse_file, BibliographyData, Entry
import utils

bib_data = parse_file('bibliography.bib')

# each article/book entry is of Entry class => Entry.fields => dict type key:value
# a collection of entries is of BibligraphyData class => dict type key:value <- Entry
# print bib_data.entries to be clear about data structures

article_list = []
inproceedings_list = []
for entry in bib_data.entries.values():
    if entry.type == 'article':
        article_list.append(utils.article_parser(entry))
        # sort by year
        article_list = sorted(article_list, key=lambda i: i['year'], reverse=True)
    if entry.type == 'inproceedings':
        inproceedings_list.append(utils.inproceedings_parser(entry))
        inproceedings_list = sorted(inproceedings_list, key=lambda i: i['year'], reverse=True)
        
# write md file
file_name= 'md_file.md'
with open(file_name,'w')as f:
    for entry in article_list:
        f.write('* %s  \n'%(entry['author']))
        f.write('  **%s**  \n'%(entry['title']))
        f.write('  *%s*'%(entry['publisher']))
        if entry['volume'] != '':
            f.write(', vol. %s'%(entry['volume']))
        if entry['number'] !='':
            f.write(', no. %s'%(entry['number']))
        if entry['pages'] !='':
            f.write(', pp. %s'%(entry['pages']))
        if entry['year'] !='':
            f.write(', %s'%(entry['year']))
        # bibtex
        f.write('  \n')
        f.write('  [[BibTeX]](javascript:toggleBibtex(\'%s\')) [[PDF]](https://doi.org/%s)  \n'%(entry['key'],entry['doi']))
        f.write('  <div id="bib_%s" class="bibtex noshow">  \n'%(entry['key']))
        f.write('  <pre>  \n')
        f.write('  %s'%(entry['bibtex']))
        f.write('  </pre>  \n  </div>')
        f.write('  \n\n')
        
    for entry in inproceedings_list:
        f.write('* %s  \n'%(entry['author']))
        f.write('  **%s**  \n'%(entry['title']))
        f.write('  *%s*'%(entry['publisher']))
        if entry['volume'] != '':
            f.write(', vol. %s'%(entry['volume']))
        if entry['number'] !='':
            f.write(', no. %s'%(entry['number']))
        if entry['pages'] !='':
            f.write(', pp. %s'%(entry['pages']))
        if entry['year'] !='':
            f.write(', %s'%(entry['year']))
        # bibtex
        f.write('  \n')
        f.write('  [[BibTeX]](javascript:toggleBibtex(\'%s\')) [[PDF]](https://doi.org/%s)  \n'%(entry['key'],entry['doi']))
        f.write('  <div id="bib_%s" class="bibtex noshow">  \n'%(entry['key']))
        f.write('  <pre>  \n')
        f.write('  %s'%(entry['bibtex']))
        f.write('  </pre>  \n  </div>')
        f.write('  \n\n')
    
        