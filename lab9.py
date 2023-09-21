# lab9.py
# Celvis
"""
raft-small-words.txt
Daniel Miessler: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/raft-small-words.txt
"""

# Import
import requests

# Make request to the desired web page
r = requests.get('http://172.25.0.29/index.php')

# web page information
webHeaders = r.headers
webHtml = r.text
webStatusCodes = r.status_code
webCookies = r.cookies

# output headers, body, status codes of request, and any cookies
print("Web headers returned:\n")
print(webHeaders)
print("Web html returned:\n")
print(webHtml)
print("Web HTTP status codes returned:\n")
print(webStatusCodes)
print("Web cookies returned:\n")
print(webCookies)