import setteings
import tweepy
import requests
import bs4
import time

CSK = setteings.CSK
CSS = setteings.CSS
AST = setteings.AST
ATS = setteings.ATS

auth = tweepy.OAuthHandler(CSK,CSS)
auth.set_access_token(AST, ATS)
api = tweepy.API(auth)

api.update_status("test")