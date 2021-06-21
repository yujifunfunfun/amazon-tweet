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


class Amazon:
    def check_stock(self,page_url):
        res = requests.get(page_url)
        soup = bs4.BeautifulSoup(res.text, features="html.parser")
        selected_html = soup.select('#add-to-cart-button')

        stock = 'none'
        while True:
            selected_html = soup.select('#add-to-cart-button')

            if selected_html and stock == 'none':
                api.update_status("在庫あり")
                stock = 'yes'
            elif not selected_html:
                stock = 'none'
            else:
                time.sleep(10)

page_url = 'https://www.amazon.co.jp/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97-SHARP-SJ-AF50G-R-%E3%83%97%E3%83%A9%E3%82%BA%E3%83%9E%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B0%E3%83%A9%E3%83%87%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051'

amazon = Amazon()
amazon.check_stock(page_url)