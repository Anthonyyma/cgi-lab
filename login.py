#!/usr/bin/env python3
import os
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie

# set up cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

# check if login info correct
loginGood = username == secret.username and password == secret.password

# set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookieUsername = None
cookiePassword = None
if cookie.get("username"):
    cookieUsername = cookie.get("username").value
if cookie.get("password"):
    cookiePassword = cookie.get("password").value

# check if cookie user/pass == secret user/pass
cookieGood = cookieUsername == secret.username and cookiePassword == secret.password

if cookieGood:
    username = cookieUsername
    password = cookiePassword

print("Content-Type: text/html")
if loginGood:
    # set cookie iff login info correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

# show login page and print form data
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
