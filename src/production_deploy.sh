#!/bin/bash
sed -i 's/^DEBUG = True.*/DEBUG = False/' A_MainSite/settings.py

# generate new password
pass=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)
sed -i 's/SECRET_KEY = 'h=)v+f8o$tff!di57v050wytm^bu!#xup=v#y*34wd=(btx4c$'/SECRET_KEY = '$pass'/ A_MainSite/settings.py
