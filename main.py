import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
from bs4 import BeautifulSoup
import requests

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

res = requests.get('https://www.rakuten-sec.co.jp/smartphone/market/info/pagecontent?pid=4021&sym=CADJPY%3DX')
soup = BeautifulSoup(res.text, 'html.parser')
price = soup.find("span", {"class": "base"}).text[0:6]

def main():
    USER_ID = info['USER_ID']
    priceMsg = "$1 = " + price + "円"
    message = TextSendMessage(text=priceMsg)
    line_bot_api.push_message(USER_ID, messages=message)

if __name__ == "__main__":
    main()
