#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas0.py

en el cod. fuente hay un comentario con la password.
"""
import libnatas

# browser instance:
natas = libnatas.NatasBrowser(level=0, password="natas0")
soup = natas.get_html_soup(natas.level_url)
# obtenmos todo el texto; la password es la ultima palabra.
password = soup.getText().split(' ')[-1:][0]
natas.print_password(password)
