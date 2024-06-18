import streamlit as st
import requests


ss = st.session_state
sc = st.secrets


def get_global():
    url = f'https://frontend-api.pump.fun/coins?offset=0&limit=50&sort=last_trade_timestamp&order=DESC&includeNsfw=true'

    response = requests.get(url)
    data = response.json()
    return data

