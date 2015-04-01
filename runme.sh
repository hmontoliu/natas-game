#! /bin/bash
# vim:ts=4:sw=4:et:ft=sh
# runs all the natas py files 
# Created: 2012-12-25

# Copyright (c) 2012: Hilario J. Montoliu <hmontoliu@gmail.com>
 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
# the full text of the license.


runall () 
{ 
    NUM=1
    DEST=results.txt
    > $DEST 
    for file in natas??.py;
    do
        password=$(python $file $password 2>/dev/null || echo fixme)
        echo "Password nivel $NUM: $password" | tee -a $DEST;
        let NUM++
    done
}

runall
