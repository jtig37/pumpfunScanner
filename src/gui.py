import streamlit as st

ss = st.session_state


@st.cache_data(show_spinner=False)
def load_css_cache(element):
    with open(f"css/{element}.css") as f:
        element_css = f.read()
    st.markdown(element_css, unsafe_allow_html=True)


def load_fake_df(data, progress):
    if data:
        with st.sidebar:
            progress.progress(value=0, text='Loading trades ...')
        for i in range(len(data)):
            progress.progress(value=(i / len(data)), text='Loading trades ...')
            with st.container(border=True):
                col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1, ])
                sCol1, sCol2, sCol3, sCol4 = st.columns([1, 1, 1, 1])
                st.info(data[i]['info'], icon='ℹ️')
                col2.write("**:green[TICKER]**")
                col3.write("**:green[NAME]**")
                col4.write("**:green[MARKETCAP]**")
                col5.write("**:green[AGE]**")

                col1.image(data[i]['icon'])
                col2.write(data[i]['ticker'])
                col3.write(data[i]['name'])
                col4.write(f"${str(data[i]['marketCap'])} USD")
                col5.write(data[i]['age'])

                if data[i]['twitter']:
                    sCol1.link_button('Twitter', url=data[i]['twitter'], use_container_width=True)

                if data[i]['telegram']:
                    sCol2.link_button('Telegram', url=data[i]['telegram'], use_container_width=True)

                if data[i]['website']:
                    sCol3.link_button('Website', url=data[i]['website'], use_container_width=True,
                                      help=':red[BE CAREFUL CLICKING ANY LINKS!]')

                sCol4.link_button(':green[pump.fun]', url=f"https://pump.fun/{data[i]['link']}",
                                  use_container_width=True)
    progress.empty()


def load_stats(data):
    if data:
        with st.container(border=True):

            st.image(data['icon'], use_column_width=True)

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[TICKER]**')
                sCol.write(data['ticker'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[NAME]**')
                sCol.write(data['name'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[MARKETCAP]**')
                sCol.write(f"${data['marketCap']} USD")

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[AGE]**')
                sCol.write(data['age'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[CREATOR]**')
                sCol.write(data['creator'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[X]**')
                sCol.write(data['twitter'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[TELEGRAM]**')
                sCol.write(data['telegram'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[WEBSITE]**')
                sCol.write(data['website'])

            with st.container(border=False):
                nCol, sCol = st.columns([1, 4])
                nCol.write('**:green[REPLIES]**')
                sCol.write(str(data['replies']))

            st.info(data['info'], icon='ℹ️')
            st.link_button(':green[pump.fun]', url=f"https://pump.fun/{data['link']}", use_container_width=True)

    else:
        pass


def load_sidebar():
    with st.form(key='filter'):
        sLCol, sRCol = st.columns([1, 1])
        sLCol.write("# :green[FILTER:]")

        fltr = st.empty()
        koth = st.empty()
        mcap = st.empty()
        replies = st.empty()
        limit = st.empty()

        st.form_submit_button('Apply Filter', use_container_width=True)

        with fltr:
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

        koth.checkbox(
            label='King of the Hill',
            key='koth'
        )
        mcap.slider('Minimum Market Cap', max_value=50000, step=1000, key='mcap')
        replies.slider('Minimum Replies', max_value=100, step=10, key='replies')
        limit.slider('Fetch Limit', min_value=50, max_value=500, step=50, key='limit')

    # st.link_button('UP', url='#test', use_container_width=True)
