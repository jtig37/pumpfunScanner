import streamlit as st

ss = st.session_state


def init_state():
    if "contractAddress" not in ss:
        ss["contractAddress"] = False

