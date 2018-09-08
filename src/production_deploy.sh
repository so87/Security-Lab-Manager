#!/bin/bash
sed -i 's/^DEBUG = True.*/DEBUG = False/' A_MainSite/settings.py

# generate new password
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 >> A_MainSite/secret_key.txt

# security settings
cat "CSRF_COOKIE_SECURE = True" >> A_MainSite/settings.py
cat "SESSION_COOKIE_SECURE = True" >> A_MainSite/settings.py
