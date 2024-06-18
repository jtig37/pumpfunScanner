import streamlit as st
import pandas as pd

ss = st.session_state


@st.cache_data(show_spinner=False)
def load_css_cache(element):
    with open(f"css/{element}.css") as f:
        element_css = f.read()
    st.markdown(element_css, unsafe_allow_html=True)


def load_df(data, hide=True, image=False):
    if data:
        df = pd.DataFrame(data)

        if image is False:
            df.index += 1
            st.dataframe(df, use_container_width=True, hide_index=hide)
        else:
            st.data_editor(
                df,
                column_config={
                    "icon": st.column_config.ImageColumn(
                        "icon"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
    else:
        pass


def load_sidebar():
    # TODO: Define Filter options: (MCAP) -> Slider,( X, TG, WEBSITE, NSFW,) -> bools (USERNAME ALS BLACKLIST???)
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


