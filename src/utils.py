import streamlit as st

ss = st.session_state


def init_state():
    if 'contractAddress' not in ss:
        ss['contractAddress'] = False

    if 'walletAddress' not in ss:
        ss['walletAddress'] = False

    if 'mcap' not in ss:
        ss['mcap'] = False

    if 'koth' not in ss:
        ss['koth'] = False

