# -*- coding: utf-8 -*-

import pycurl, urllib.parse, json
from io import BytesIO

class GoogleOauthUtil():
    def __init__(self, oAuth):
        self.oAuth = oAuth

    def setAccessToken(self):
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://accounts.google.com/o/oauth2/token')
        c.setopt(c.HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded'])
        postData = urllib.parse.urlencode({ \
                                           'grant_type':'refresh_token', \
                                           'refresh_token':self.oAuth.refreshToken, \
                                           'client_id':self.oAuth.clientId, \
                                           'client_secret':self.oAuth.clientSecret})
        c.setopt(c.POSTFIELDS, postData)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        value = json.loads(body.decode('utf-8'))
        try:
            self.oAuth.accessToken = value['access_token']
        except IndexError:
            self.oAuth.accessToken = None
