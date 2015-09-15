# author   : Johann-Mattis List
# email    : mattis.list@uni-marburg.de
# created  : 2015-03-25 11:11
# modified : 2015-03-25 11:11
"""
App creates Huber data in EDICTOR form.
"""

__author__="Johann-Mattis List"
__date__="2015-03-25"

from lingpyd import *
from lingpyd.plugins.lpserver.lexibase import *


wl = Wordlist('tsv/huber1992.csv')
wl.output('tsv', filename='tsv/huber1992-preparsed', subset=True,
        rows=dict(doculect = "not in ['English', 'Español']"))
print('excluded english and spanish')
wl = Wordlist('tsv/huber1992-preparsed.tsv')
wl.tokenize(orthography_profile='huber1992.prf', target='_tokens', column='ipa')
wl.add_entries('tokens', '_tokens', lambda x: ipa2tokens(''.join(x.split(' ')).replace('NULL',''),
    semi_diacritics='sh', expand_nasals=True, merge_geminates=True,
    merge_vowels=False))
wl.output('tsv', filename='tsv/huber1992-tokens', subset=True, cols=[c for c in
    wl.header if c != '_tokens'])
print("Analyzed Wordlist and added tokens")
lex = LexStat('tsv/huber1992-tokens.tsv', check=True)
lex.cluster(method='sca', threshold=0.3)
lex.add_entries('cogid', 'scaid', lambda x: x)
lex.output('tsv', filename='tsv/huber1992-sca', ignore=['scorer','json'])
print("Clusterd cognate sets with SCA")
alm = Alignments('tsv/huber1992-sca.tsv', ref='cogid')
alm.align(method='library', iteration=True)
alm.output('tsv', filename='tsv/huber1992-msa', ignore=['scorer', 'json', 'msa'])
print("Aligned the data")

db = LexiBase('tsv/huber1992-msa.tsv')
db.create('huber1992', dbase='sqlite3/huber1992.sqlite3')
print("Created SQLITE-DB")
