#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
libnatas.py

clases y funciones comunes a todos los niveles

Created: 2012-12-24

Copyright (c) 2012: Hilario J. Montoliu  <hmontoliu@gmail.com> 

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
the full text of the license.
"""
import mechanize
import re
from BeautifulSoup import BeautifulSoup

class NatasBrowser(mechanize.Browser):
    """clases comunes a todos los niveles de natas
    
    uso NatasBrowser(level=N, password="pass obtenida en el niv. anterior")
    """

    # valores por defecto (str)
    level_url_str = "http://natas%i.natas.labs.overthewire.org" 
    level_user_str = "natas%i" 
    level_password_str = "%s" 

    def __init__(self, level=0, password="natas0"):
        """inicializacion del browser"""
        mechanize.Browser.__init__(self)
        self.set_handle_referer(False)   # allow everything to be written to
        self.set_handle_robots(False)   # no robots
        self.set_handle_refresh(True)   # can sometimes hang without this
        self.set_handle_redirect(True)
        self.addheaders = [('User-agent', 
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'),]

        self.level_url = self.level_url_str % level
        self.level_user = self.level_user_str % level
        self.level_password = self.level_password_str % password

        # autentificacion
        self.add_password(self.level_url, self.level_user, self.level_password)
        self.nextlevel = int(level) + 1

    def get_html_response(self, url):
        """Devuelve el objeto Browser.open(url)"""
        return self.open(url)

    def get_html_soup(self, url):
        """Devuelve objeto BeautifulSoup con el contenido del la pagina"""
        return BeautifulSoup(self.get_html_response(url))

    def get_password(self, texto, regex):
        """Devuelve la passowrd extraida del *texto* mediante la *regexp* pasada"""
        theregex = re.compile(regex)
        password = theregex.findall(texto)[0]
        return password

    def print_password(self, password_str):
        """Muestra cadena con la password obtenida"""
        resultstr = """Password for level natas%s is %s"""
        print resultstr % (self.nextlevel, password_str)

# ejemplo de uso (level 0), indicamos el nivel actual y la password obtenida del anterior

if __name__ == "__main__":
    natasbr = NatasBrowser(level=0, password="natas0") 
    soup = natasbr.get_html_soup(natasbr.level_url)

    # obtenmos todo el texto, la password es la ultima palanatasbra.
    password = soup.getText().split(' ')[-1:][0]
    print natasbr.print_password(password)
