'''
Created on 2016/07/06

@author: samuraimasa
'''

import configparser
from google.model.OAuth import OAuth
from google.util.GoogleAnalyticsUtil import GoogleAnalyticsUtil
import json

# confファイル読込み
confFile = configparser.SafeConfigParser()
confFile.read("../../conf/app.conf")
#  oAuth生成
clientId = confFile.get("google_oauth", "client_id")
clientSecret = confFile.get("google_oauth", "client_secret")
callback = confFile.get("google_oauth", "callback")
refreshToken = confFile.get("google_oauth", "refresh_token")
oAuth = OAuth(clientId,clientSecret,callback,refreshToken)

googleAnalyticsUtil = GoogleAnalyticsUtil(oAuth)
googleAnalyticsUtil.setAccessToken()

id = ''
# v4
params = {"reportRequests":[{
          'viewId':id,
          'dateRanges':[{'startDate':'2016-06-01', 'endDate':'2016-06-30'}],
          'dimensions':[{'name':'ga:sourceMedium'}],
          'metrics':[{'expression':'ga:sessions'},{'expression':'ga:pageviews'}]
           }]}
gaData = googleAnalyticsUtil.getV4(params)
print(gaData)

# v3
params = {'ids':id,
          'metrics':'ga:sessions',
          'dimensions':'ga:deviceCategory',
          'start-date':'2016-06-01',
          'end-date':'2016-06-30'
          }
gaData = googleAnalyticsUtil.getV3(params)
print(gaData)