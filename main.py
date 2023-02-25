from bs4 import BeautifulSoup
import requests


def get_price(coin):
    url = 'https://www.google.com/search?q=' + coin + 'price'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    price = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    return price


def main():
    coin = input('Enter a coin: ')
    price = get_price(coin)
    print('The current price of ' + coin + ' is ' + price)


if __name__ == '__main__':
    main()
