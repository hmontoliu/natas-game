#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:et:ft=python:
"""
natas08.py

"""
import libnatas

# url: "http://natas8.natas.labs.overthewire.org"
# user: "natas8"
password = "maabkdexUStb6JJXUqmBx7Re8M61cksn"

natas = libnatas.NatasBrowser(level=8, password=password)

# para ver el source code del nivel descargar index-source.html
# dentro hay un hash:
hash = natas.get_password(natas.get_html_soup(natas.level_url + '/index-source.html').prettify(), '"([a-zA-Z0-9]{32})"')

# este hash es usado para validar la passsword en la expresión:
# realpass == bin2hex(strrev(base64_encode($secret)))
# donde $secret es el hash 
# por lo que hay que revertir la expresión. 

#-php-# En php se haría (inversa de la funcion de index-source)::
#-php-# 
#-php-#  <?
#-php-#  function hex2bin($data) {
#-php-#  $len = strlen($data);
#-php-#     for($i=0;$i<$len;$i+=2) {
#-php-#         $newdata .= pack("C",hexdec(substr($data,$i,2)));
#-php-#     }
#-php-#  return $newdata;
#-php-#  }
#-php-# 
#-php-#  $secret = "3d3d516343746d4d6d6c315669563362"; /* hash */
#-php-#  $hex = hex2bin($secret);
#-php-#  $base = base64_decode(strrev($hex));
#-php-#  print $base;
#-php-#  ?>
#-php-# 
#-php-# Dónde $base es la password que revelará la del siguiente nivel en el formulario

# en python quedaría:
# hex2bin->reverse->decodebase64
import base64, binascii
secret = base64.decodestring(binascii.a2b_hex(hash)[::-1])

# reabrimos la pagina principal y rellenamos el formulario
natas.open(natas.level_url)
natas.select_form(nr=0) # primera form (y unica)
natas.form['secret'] = secret

html = natas.submit()
password_nl = natas.get_password(html.read(), '.*natas9 is (.*)\W.*')
natas.print_password(password_nl)

