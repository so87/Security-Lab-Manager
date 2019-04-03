#!/bin/bash
 
# ensure debug is on
sed -i 's/^DEBUG = False.*/DEBUG = True/' A_MainSite/settings.py

# ensure clsf is off
sed -i 's/^SESSION_COOKIE_SECURE = True.*/SESSION_COOKIE_SECURE = False/' A_MainSite/settings.py

# secure cookies aren't being used
sed -i 's/^CSRF_COOKIE_SECURE = True.*/CSRF_COOKIE_SECURE = False/' A_MainSite/settings.py

# ensure whitenoise isn't delivering static files
sed -i 's/^STATICFILES_STORAGE =.*/#/' A_MainSite/settings.py