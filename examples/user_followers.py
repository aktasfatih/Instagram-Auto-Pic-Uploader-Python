#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import json

from InstagramAPI import InstagramAPI
ID = raw_input("Username: ")
Pass = raw_input("Password: ")
api = InstagramAPI(ID, Pass)

if api.isLoggedIn:
    api.logout()
else:
    print("NOT LOGGED IN")
    api.login()

api.tagFeed("istanbul")  # get media list by tag #cat
media_id = api.LastJson  # last response JSON
api.like(media_id["ranked_items"][0]["pk"])  # like first media
api.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"])  # get first media owner followers

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

pp_json(api.LastJson)
