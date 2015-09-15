from lingpyd import *
from lingpyd.plugins.lpserver.lexibase import *

db = LexiBase('huber1992', dbase='sqlite3/huber1992.sqlite3')

wl = Wordlist('huber1992-3.tsv')
head = sorted(wl.header, key=lambda x: wl.header[x])
for k in wl:

    tmp = dict(zip(head, wl[k]))
    for a,b in tmp.items():
        db[k][db.header[a]] = b


for k in db:
    
    ipa = db[k,'ipa']
    if rc('nasal_placeholder') in ipa:
        db[k][db.header['ipa']] = ipa.replace(
                rc('nasal_placeholder'),
                ''
                )
    alm = db[k,'alignment']
    tks = db[k,'tokens']
    if '#' in alm:
        if type(alm) == str:
            alm = alm.split(' ')
        if type(tks) == str:
            tks = tks.split(' ')

        alm = ' '.join(alm).replace('#', '_')
        if '_' in alm:
            alm = alm[:alm.index('_')-1]
        tks = ' '.join(tks).replace('#', '_')
        if '_' in tks:
            tks = tks[:tks.index('_')-1]

        if type(alm) == str:
            alm = alm.split(' ')
        if type(tks) == str:
            tks = tks.split(' ')
            

        db[k][db.header['note']] = '! '+db[k,'note']
        db[k][db.header['alignment']] = alm
        db[k][db.header['tokens']] = tks
print('done')
for k in db:
    if not ''.join(db[k,'alignment']):
        db[k][db.header['alignment']] = ['-'] 

db.update('huber1992', verbose=True)

