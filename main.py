import requests
import json
import os
import sys
import time


def display_price():
    # get current price
    response = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin')
    data = response.json()
    current_price = data['market_data']['current_price']['usd']
    # get previous price
    with open('price.txt', 'r') as f:
        previous_price = f.read()
    # compare current price with previous price
    if current_price > float(previous_price):
        print('\033[92m' + str(current_price) + '\033[0m')
    else:
        print('\033[91m' + str(current_price) + '\033[0m')
    # save current price to price.txt
    with open('price.txt', 'w') as f:
        f.write(str(current_price))
    # wait 60 second
    time.sleep(60)
    # call display_price function again
    display_price()

def main():
    # check if price.txt exists
    if os.path.exists('price.txt'):
        # if price.txt exists, call display_price function
        display_price()
    else:
        # if price.txt doesn't exist, create price.txt and call display_price function
        with open('price.txt', 'w') as f:
            f.write('0')
        display_price()


if __name__ == '__main__':
    main()
    sys.exit()
