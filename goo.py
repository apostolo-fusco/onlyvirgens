from googlesearch import search
from os import system, name

from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading

#--------
drive ='site:drive.google.com'
famouspaste ='site:famouspaste.com'
pastelink ='site:pastelink.net'
rentry ='site:rentry.co'
pastesite ='site:pastesite.org'
freepaste ='site:freepaste.link'
leaklinks ='site:leaklinks.com'
gofile ='site:gofile.io'
justpaste ='site:justpaste.it'
reddit ='site:reddit.com'
sexyegirls ='site:sexy-egirls.com'

#----------
print(pyfiglet.figlet_format("ONLY VIRGENS", font="slant"))

#--------
print ('NOME DO ANJINHO')
nome = input ('')
print ('')
print ('Analizando...')
print ('')
print ('')


#GOOGLE DRIVE
print ('GOOGLE DRIVE')
print ('')
search_query= nome+drive
for i in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (i)
#-----------

print ('')

#famouspaste
print ('FAMOUS PASTE')
print ('')
search_query= nome+famouspaste
for fp in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (fp)
#-----------
print ('')

#pastelink
print ('PASTE LINK')
print ('')
search_query= nome+pastelink
for pl in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (pl)
#-----------
print ('')

#freepaste
print ('FREE PASTE')
print ('')
search_query= nome+freepaste
for frp in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (frp)
#-----------
print ('')

#leaklinks
print ('LEAK LINKS')
print ('')
search_query= nome+leaklinks
for ll in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (ll)
#-----------
print ('')

#gofile
print ('GO FILE')
print ('')
search_query= nome+gofile
for gf in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (gf)
#-----------
print ('')

#justpaste
print ('JUST PASTE')
print ('')
search_query= nome+justpaste
for jp in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (jp)
#-----------
print ('')

#reddit
print ('REDDIT')
print ('')
search_query= nome+reddit
for re in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (re)
#-----------
print ('')

#socialmediagirls
print ('SOCIAL MEDIA GIRLS')
print ('')
search_query= nome+sexyegirls
for seg in search(search_query,
    tld='com',
    num=5,
    stop=5,
    pause=2.0):
    print (seg)
