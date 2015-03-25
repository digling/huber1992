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



db = LexiBase('tsv/huber1992-analyzed-aligned.tsv')

db.create('huber1992', dbase='sqlite/huber1992.sqlite3')

