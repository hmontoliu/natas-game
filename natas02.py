
#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas02.py

la clave esta en files/users.txt
"""
import libnatas

# url: "http://natas2.natas.labs.overthewire.org"
# user: "natas2"
password = "aRJMGKT6H7AOfGwllwocI2QwVyvo7dcl"

# la password esta en files/users.txt
natas = libnatas.NatasBrowser(level=2, password=password)
soup = natas.get_html_soup(natas.level_url + '/files/users.txt')
password_nl = natas.get_password(soup.prettify(), '.*natas3:(.*)\W.*')
natas.print_password(password_nl)
