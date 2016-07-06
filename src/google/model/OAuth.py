# -*- coding: utf-8 -*-

class OAuth():
    def __init__(self, clientId="", clientSecret="", callback="", refreshToken="", accessToken=""):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.callback = callback
        self.refreshToken = refreshToken
        self.accessToken = accessToken