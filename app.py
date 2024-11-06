import streamlit as st
import src.utils as ut
import src.gui as gui
import src.pumpfun as pf
import streamlit as st

# Initialize session state for 'limit' if it doesn't exist
if 'limit' not in st.session_state:
    st.session_state['limit'] = 10  # Set a default value (e.g., 10)

# The rest of your app code
import pumpfun as pf  # Assuming this is how you import the module

# Now you can safely access 'limit' in session state
globalData = pf.get_global(nsfw=nsfw)

ss = st.session_state

st.set_page_config(
    page_title=" pump.fun Scanner",
    page_icon="💊",
    layout="wide"
)

# Initialize session state
ut.init_state()

# Loads sidebar
with st.sidebar:
    gui.load_sidebar()
    progress = st.empty()


top_left, top_right = st.columns([7, 1])
top_left.header("💊 :green[pump.fun Scanner]")
top_right.markdown(f':green[SOLANA: ${pf.get_sol_price()}]')

gui.load_css_cache('footer')
gui.load_css_cache('header')


# Columns for responsive Page layout and page structure
h_l_col, h_r_col = st.columns([1, 1])  # Columns header
left_col, right_col = st.columns([5, 3])  # Columns Search

# BUTTONS
with h_r_col:
    h_l_2_col, h_m_2_col, h_r_2_col = st.columns([1, 1, 1])
    pfp_img = h_l_2_col.empty()

if 'nsfw' in ss and not ss['nsfw']:
    nsfw = 'false'
else:
    nsfw = 'true'

h_r_2_col.button('REFRESH', help='Refresh this Site!', use_container_width=True)

with left_col:
    st.markdown('# :green[Global]')
    globalData = pf.get_global(nsfw=nsfw)
    gui.load_fake_df(globalData, progress)
with right_col:
    st.markdown('# :green[King of the Hill]')
    kothData = pf.get_koth(nsfw=nsfw)
    gui.load_stats(kothData)


