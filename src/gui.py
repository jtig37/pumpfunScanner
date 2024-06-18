import streamlit as st
import pandas as pd


#@st.cache_data(show_spinner=False)
def load_css_cache(element):
    with open(f"css/{element}.css") as f:
        element_css = f.read()
    st.markdown(element_css, unsafe_allow_html=True)


def load_df(data, hide, image=False):
    if data:
        df = pd.DataFrame(data)

        if image is False:
            df.index += 1
            st.dataframe(df, use_container_width=True, hide_index=hide)
        else:
            st.data_editor(
                df,
                column_config={
                    "image_uri": st.column_config.ImageColumn(
                        "image_uri"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
    else:
        pass
