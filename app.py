import streamlit as st
import src.utils as ut
import src.gui as gui
import src.pumpfun as pf

ss = st.session_state

st.set_page_config(
    page_title=" pump.fun Scanner",
    page_icon="💊",
    layout="wide"
)

# gui.load_css_cache('upButton')
# Initialize session state
ut.init_state()

# Loads sidebar
with st.sidebar:
    with st.form(key='filter'):
        sLCol, sRCol = st.columns([1, 1])
        sLCol.write("# :green[FILTER:]")

        fltr = st.empty()
        koth = st.empty()
        mcap = st.empty()

        st.form_submit_button(':green[Apply Filters]', use_container_width=True)

        with fltr:
            gui.load_sidebar()

        koth.checkbox(
            label='King of the Hill',
            key='koth'
        )
        mcap.slider('Minimum Market Cap', max_value=50000, step=1000, key='mcap')

top_left, top_right = st.columns([7, 1])
top_left.header("💊 :green[pump.fun Scanner]")
top_right.markdown(f':green[SOLANA: ${pf.get_sol_price()}]')

gui.load_css_cache('footer')
# gui.load_css_cache('header') TODO: ENABLE


# Columns for responsive Page layout and page structure
h_l_col, h_r_col = st.columns([1, 1])  # Columns header
left_col, right_col = st.columns([4, 3])  # Columns Search

# BUTTONS
with h_r_col:
    h_l_2_col, h_m_2_col, h_r_2_col = st.columns([1, 1, 1])
    pfp_img = h_l_2_col.empty()

    sol_scan = h_m_2_col.empty()
    twitter = h_m_2_col.empty()
    telegram = h_m_2_col.empty()

# SUBMIT FORM
with h_l_col.form(key='search', clear_on_submit=True):
    ss['address'] = st.text_input(label='Look up a contract address')
    button = st.form_submit_button(':green[Search]')


if 'nsfw' in ss and not ss['nsfw']:
    nsfw = 'false'
else:
    nsfw = 'true'


# GET FUNCTION
if not ss['address'] and not button:
    refresh = h_r_2_col.button(':green[REFRESH]', help='Refresh this Site!', use_container_width=True)

    with left_col:
        st.markdown('# :green[Global]')
        globalData = pf.get_global(nsfw=nsfw)
        gui.load_fake_df(globalData)
    with right_col:
        st.markdown('# :green[King of the Hill]')
        kothData = pf.get_koth(nsfw=nsfw)
        gui.load_stats(kothData)

else:
    # Check if wallet or ca
    # catch errors
    addressChecked = pf.check_address(ss['address'])
    print(addressChecked)
    if not addressChecked:
        h_l_col.error('Address not found!')
    if addressChecked == 'w':
        #with h_l_col:
            #gui.load_stats() TODO: Load stats
        with h_r_col:
            st.markdown('# :green[Global]')
            globalData = pf.get_global(nsfw=nsfw)
            gui.load_fake_df(globalData)
    if addressChecked == 'w':
        #with h_l_col:
            #gui.load_stats()
        with h_r_col:
            st.markdown('# :green[Global]')
            globalData = pf.get_global(nsfw=nsfw)
            gui.load_fake_df(globalData)
    h_r_2_col.button(':green[HOME]', use_container_width=True, on_click=ut.nav_home())
    telegram.link_button('Telegram', url=f'https://friend.tech/', use_container_width=True)
    twitter.link_button('Twitter', url=f'https://twitter.com/', use_container_width=True)
    sol_scan.link_button('Solana Scan', url=f'https://solscan.io/token/', use_container_width=True)
