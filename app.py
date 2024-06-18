import streamlit as st
import src.utils as ut
import src.gui as gui
import src.pumpfun as pf


ss = st.session_state

st.set_page_config(
    page_title="pump.fun Scanner",
    page_icon="💊",
    layout="wide"
)

# Initialize session state
ut.init_state()

# Loads sidebar
with st.sidebar:
    progress = st.empty()
    st.write("FILTER FOR SIDEBAR")

st.header("pump.fun Scanner")

gui.load_css_cache("footer")
gui.load_css_cache("header")


# Columns for responsive Page layout and page structure
h_l_col, h_r_col = st.columns([1, 1])  # Columns header
left_col, right_col = st.columns([1, 1])  # Columns Search
m_l_c, m_r_c = st.columns([1, 1])
b_l_c, b_r_c = st.columns([1, 1])

# BUTTONS
with h_r_col:
    h_l_2_col, h_m_2_col, h_r_2_col = st.columns([1, 1, 1])
    pfp_img = h_l_2_col.empty()

    if not ss['contractAddress']:
        refresh = h_m_2_col.button("REFRESH", help="Refresh this Site!", use_container_width=True)

    sol_scan = h_r_2_col.empty()
    twitter = h_r_2_col.empty()
    telegram = h_r_2_col.empty()

# SUBMITFORM
with h_l_col.form(key="search", clear_on_submit=True):
    ss["contractAddress"] = st.text_input(label="Look up a contract address")
    button = st.form_submit_button("Search")

# GET FUNCTION
if not ss['contractAddress']:

    with left_col:
        st.markdown("# Global")
        globalFeed = pf.get_global()
        gui.load_df(globalFeed, hide=False, image=True)
    with right_col:
        st.markdown("# Trending")

    with m_l_c:
        st.markdown("# Top Buyers")

    with m_r_c:
        st.markdown("# Top Sellers")

    st.markdown("")  # Spacer for columns

else:
    telegram.link_button("Telegram", url=f"https://friend.tech/", use_container_width=True)
    twitter.link_button("Twitter", url=f"https://twitter.com/", use_container_width=True)
    sol_scan.link_button("Solana Scan", url=f"https://solscan.io/token/", use_container_width=True)

