import streamlit as st
import requests


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

            for item in data:

                if not item['complete']:
                    filtered_data.append(
                        {
                            'icon': item['image_uri'],
                            'ticker': item['symbol'],
                            'name': item['name'],
                            'marketCap': item['usd_market_cap'],
                            'age': item['created_timestamp'],   # TODO: Conversion
                            'CA': item['mint'],
                            'twitter': item['twitter'],
                            'telegram': item['telegram'],
                            'website': item['website'],
                            'creator': item['creator'],
                            'KOTH': False if item['king_of_the_hill_timestamp'] is None else True,
                            'lastTrade': item['last_trade_timestamp'],  # TODO: Conversion
                            'replies': item['reply_count'],
                            'last_reply': item['last_reply']
                        }
                    )

        return filtered_data
    except requests.exceptions.JSONDecodeError:
        return None


def get_koth(nsfw="false"):
    url = f'https://frontend-api.pump.fun/coins/king-of-the-hill?includeNsfw={nsfw}'

    # TODO: Catch error
    response = requests.get(url)
    data = response.json()
    return [data]


def get_sol_price():
    url = 'https://frontend-api.pump.fun/sol-price'

    # TODO: Catch error
    response = requests.get(url)
    data = response.json()
    return data['solPrice']
