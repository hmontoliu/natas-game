#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas1.py

prácticamente lo mismo que el nivel0
"""
import libnatas

# url: "http://natas1.natas.labs.overthewire.org"
# user: "natas1"
password="9hSaVoey44Puz0fbWlHtZh5jTooLVplC"

natas = libnatas.NatasBrowser(level=1, password=password)
soup = natas.get_html_soup(natas.level_url)

# obtenmos todo el texto, la password es la ultima palabra.
texto = soup.getText()
password_nl = texto.split(' ')[-1:][0]
natas.print_password(password_nl)
