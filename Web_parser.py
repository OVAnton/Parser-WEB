import requests
from bs4 import BeautifulSoup as bs
import telebot
import time

URL_TEMPLATE = "https://psd-info.com/products/%D0%BF%D0%B0%D1%82%D1%87-%D0%BC%D0%B0%D0%BD%D0%B4%D1%80%D1%83%D0%B9-%D1%81%D1%82%D1%80%D1%96%D0%BB%D1%8F%D0%B9-%D0%BA%D0%BE%D1%85%D0%B0%D0%B9-psdinfo%C2%AE?variant=45036061557041"
r = requests.get(URL_TEMPLATE)
print(r.status_code)

token = "TOKEN_BOT"
bot = telebot.TeleBot(token)
chat_id = "Your_Telegram_ID"

soup = bs(r.text, "html.parser")
title = soup.find('div', class_="product-block product-block__title").find('h1').text
button_buy = soup.find('div', class_="product-form__buttons").text
visually_hidden = soup.find('div', class_="price__regular").find('span', class_="visually-hidden").text
price = soup.find('div', class_="price__regular").find('span', class_="price-item price-item--regular").text
main_text = str(title + '\n' + visually_hidden + " - " + price)

def main():
    x = "Додати в кошик"
    if x in button_buy:
        bot.send_message(chat_id, main_text + '\n' + '<a href = "https://psd-info.com/products/%D0%BF%D0%B0%D1%82%D1%87-%D0%BC%D0%B0%D0%BD%D0%B4%D1%80%D1%83%D0%B9-%D1%81%D1%82%D1%80%D1%96%D0%BB%D1%8F%D0%B9-%D0%BA%D0%BE%D1%85%D0%B0%D0%B9-psdinfo%C2%AE?variant=45036061557041">Додати в кошик:</a>',
                         parse_mode="HTML", )
    else:
        time.sleep(86400)
        main()

if __name__ == '__main__':
    main()
