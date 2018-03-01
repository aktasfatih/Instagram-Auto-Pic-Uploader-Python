#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("aydinlatmaurunleri", "YokArtik1")
InstagramAPI.login()  # login

photo_path = './1.jpeg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
