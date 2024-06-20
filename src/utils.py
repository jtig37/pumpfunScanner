import streamlit as st
import time
import humanize


ss = st.session_state


def init_state():
    if 'address' not in ss:
        ss['address'] = False

    if 'walletAddress' not in ss:
        ss['walletAddress'] = False

    if 'mcap' not in ss:
        ss['mcap'] = False

    if 'koth' not in ss:
        ss['koth'] = False


def nav_home():
    if 'address' not in ss:
        ss['address'] = False

    if 'walletAddress' not in ss:
        ss['walletAddress'] = False


def time_ago(timestamp):
    return humanize.naturaltime(time.time() - timestamp / 1000)

