import setteings
import tweepy
import urllib.request
import bs4
import time

CSK = setteings.CSK
CSS = setteings.CSS
AST = setteings.AST
ATS = setteings.ATS

auth = tweepy.OAuthHandler(CSK,CSS)
auth.set_access_token(AST, ATS)
api = tweepy.API(auth)
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
'AppleWebKit/537.36 (KHTML, like Gecko) '\
'Chrome/55.0.2883.95 Safari/537.36 '

class Amazon:
    def check_stock(self,page_url):
        
        stock = 'none'
        while True:
            req = urllib.request.Request(page_url, headers={'User-Agent': ua})
            html = urllib.request.urlopen(req)
            soup = bs4.BeautifulSoup(html, "html.parser")
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
