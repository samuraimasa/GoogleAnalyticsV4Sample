# -*- coding: utf-8 -*-

from google.util.GoogleOauthUtil import GoogleOauthUtil
import pycurl, urllib.parse, json
from io import BytesIO

class GoogleAnalyticsUtil(GoogleOauthUtil):
    def getV3(self, params):
        query = urllib.parse.urlencode(params)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://www.googleapis.com/analytics/v3/data/ga?' + query)
        c.setopt(c.HTTPHEADER, ['Authorization: Bearer ' + self.oAuth.accessToken])
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        return json.loads(body.decode('utf-8'))
    
    def getV4(self, params):
        post = json.dumps(params)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'https://analyticsreporting.googleapis.com/v4/reports:batchGet')
        c.setopt(c.HTTPHEADER, ['Content-Type: application/json', 'Authorization: Bearer ' + self.oAuth.accessToken])
        c.setopt(c.POSTFIELDS, post)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        return json.loads(body.decode('utf-8'))