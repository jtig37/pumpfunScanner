import streamlit as st
from PIL import Image

ss = st.session_state


@st.cache_data(show_spinner=False)
def load_css_cache(element):
    with open(f"css/{element}.css") as f:
        element_css = f.read()
    st.markdown(element_css, unsafe_allow_html=True)


def load_fake_df(data):
    if data:
        for i in range(len(data)):

            with st.container(border=True):
                col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

                col2.write("**:green[TICKER]**")
                col3.write("**:green[NAME]**")
                col4.write("**:green[MARKETCAP]**")
                col5.write("**:green[AGE]**")
                col6.write("**:green[LINK]**")

                col1.image(data[i]['icon'])
                col2.write(data[i]['ticker'])
                col3.write(data[i]['name'])
                col4.write(f"${str(data[i]['marketCap'])} USD")
                col5.write(data[i]['age'])
                col6.link_button('pump.fun', url=f"https://pump.fun/{data[i]['link']}")

    else:
        pass


def load_stats(data):
    if data:
        with st.container(border=True):

            st.image(data['icon'], use_column_width=True)
            nCol, sCol = st.columns([1, 4])
            nCol.write('**:green[TICKER]**')
            nCol.write('**:green[NAME]**')
            nCol.write('**:green[MARKETCAP]**')
            nCol.write('**:green[AGE]**')
            nCol.write('**:green[CREATOR]**')
            nCol.write('**:green[X]**')
            nCol.write('**:green[TELEGRAM]**')
            nCol.write('**:green[WEBSITE]**')
            nCol.write('**:green[REPLIES]**')

            sCol.write(data['ticker'])
            sCol.write(data['name'])
            sCol.write(f"${data['marketCap']} USD")
            sCol.write(data['age'])
            sCol.write(data['creator'])
            sCol.write(data['twitter'])
            sCol.write(data['telegram'])
            sCol.write(data['website'])
            sCol.write(str(data['replies']))

            st.link_button(':green[pump.fun]', url=f"https://pump.fun/{data['link']}", use_container_width=True)

    else:
        pass


def load_sidebar():
    # bools (USERNAME ALS BLACKLIST???)
    lCol, rCol = st.columns([1, 1])

    lCol.checkbox(
        label='Twitter',
        key='x',
    )
    lCol.checkbox(
        label='Telegram',
        key='tg'
    )

    rCol.checkbox(
        label='NSFW',
        key='nsfw'
    )
    rCol.checkbox(
        label='Website',
        key='web'
    )

