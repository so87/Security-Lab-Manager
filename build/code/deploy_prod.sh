#!/bin/bash
sed -i 's/^DEBUG = True.*/DEBUG = False/' A_MainSite/settings.py

# generate new password
cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1 > A_MainSite/secret_key.txt

# add security settings if they don't already exist
LINE='CSRF_COOKIE_SECURE = True'
FILE=A_MainSite/settings.py
grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"
LINE='SESSION_COOKIE_SECURE = True'
grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"

# collect static files
rm -rf /code/static/*
python /code/manage.py collectstatic

# uncomment static file
LINE="STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'"
grep -qF -- "$LINE" "$FILE" || echo "$LINE" >> "$FILE"