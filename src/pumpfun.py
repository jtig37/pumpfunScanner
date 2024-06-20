import streamlit as st
import requests

from src.utils import time_ago

ss = st.session_state
sc = st.secrets


def get_global(nsfw="false"):
    url = f'https://frontend-api.pump.fun/coins?offset=0&limit=0&sort=last_trade_timestamp&order=DESC&includeNsfw={nsfw}'
    filtered_data = []
    response = requests.get(url)

    try:
        data = response.json()
        response.raise_for_status()
        if len(data) > 0:
            data = data[:ss['limit']]
            for item in data:

                if not item['complete']:
                    # koth = False if item['king_of_the_hill_timestamp'] is None else True
                    if ((ss['x'] and item['twitter'] is None) or
                            (ss['tg'] and item['telegram'] is None) or
                            (ss['web'] and item['website'] is None) or
                            (ss['koth'] and item['king_of_the_hill_timestamp'] is None) or
                            (ss['mcap'] and item['usd_market_cap'] < ss['mcap']) or
                            (ss['replies'] and item['reply_count'] < ss['replies'])):
                        continue
                    else:
                        filtered_data.append(
                            {
                                'icon': item['image_uri'],
                                'ticker': item['symbol'],
                                'name': item['name'],
                                'marketCap': int(item['usd_market_cap']),
                                'age': time_ago(int(item['created_timestamp'])),  # TODO: Conversion
                                'link': item['mint'],
                                'info': item['description'],
                                # 'twitter': item['twitter'],
                                # 'telegram': item['telegram'],
                                # 'website': item['website'],
                                # 'creator': item['creator'],
                                # 'KOTH': koth,
                                # 'lastTrade': time_ago(int(item['last_trade_timestamp'])),  # TODO: Conversion
                                # 'replies': item['reply_count'],
                                # 'last_reply': item['last_reply']
                            }
                        )

        return filtered_data
    except requests.exceptions.JSONDecodeError:
        return None


def get_koth(nsfw="false"):
    url = f'https://frontend-api.pump.fun/coins/king-of-the-hill?includeNsfw={nsfw}'

    filtered_data = []
    response = requests.get(url)

    try:
        data = response.json()
        response.raise_for_status()
        solPrice = get_sol_price()
        if len(data) > 0:
            if not data['complete']:
                return {
                    'icon': data['image_uri'],
                    'ticker': data['symbol'],
                    'name': data['name'],
                    'marketCap': int(data['market_cap'] * solPrice),
                    'age': time_ago(int(data['created_timestamp'])),
                    'link': data['mint'],
                    'twitter': data['twitter'],
                    'telegram': data['telegram'],
                    'website': data['website'],
                    'creator': data['creator'],
                    'info': data['description'],
                    # 'KOTH': koth,
                    # 'lastTrade': time_ago(int(item['last_trade_timestamp'])),
                    'replies': data['reply_count'],
                    # 'last_reply': item['last_reply']
                }

    except requests.exceptions.JSONDecodeError:
        return None


def get_sol_price():
    url = 'https://frontend-api.pump.fun/sol-price'

    try:
        response = requests.get(url)
        data = response.json()
        return data['solPrice']
    except requests.exceptions.JSONDecodeError:
        return None


@st.cache_data(show_spinner=False)
def check_address(address):
    coin = False
    wallet = False
    try:
        url = f'https://frontend-api.pump.fun/coins/{address}'
        response = requests.get(url)
        data = response.json()

        if data is not None:
            coin = True
        if 'statusCode' in data:
            coin = False

    except requests.exceptions.JSONDecodeError:
        coin = False

    try:
        url = f'https://frontend-api.pump.fun/users/{address}'
        response = requests.get(url)
        data = response.json()

        if data is not None:
            wallet = True
        if 'statusCode' in data:
            wallet = False

    except requests.exceptions.JSONDecodeError:
        wallet = False

    if wallet:
        return 'w'
    elif coin:
        return 'c'
    else:
        return None
