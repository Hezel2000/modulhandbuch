import streamlit as st
import utils
import pandas as pd

st.logo('images/Goethe-Logo.jpg')
st.sidebar.image('images/Goethe-Logo.jpg')

st.session_state.all_bsc_lectures = utils.return_all_bsc_lectures().reset_index(drop=True)
st.session_state.all_msc_lectures = utils.return_all_msc_lectures().reset_index(drop=True)


st.subheader('Alle Veranstaltungen')

st.logo('images/Goethe-Logo.jpg')

tab1, tab2, tab3 = st.tabs(['BSc', 'MSc', 'BSc & MSc'])

with tab1:
    st.markdown(f'''Es gibt insgesamt {len(st.session_state.all_bsc_lectures)} BSc Veranstaltungen.''')
    st.write(st.session_state.all_bsc_lectures)

with tab2:
    st.markdown(f'''Es gibt insgesamt {len(st.session_state.all_msc_lectures)} MSc Veranstaltungen.''')
    st.write(st.session_state.all_msc_lectures)

with tab3:
    st.markdown(f'''Es gibt insgesamt {len(st.session_state.all_bsc_lectures) + len(st.session_state.all_msc_lectures)} Veranstaltungen.''')
    st.write(pd.concat([st.session_state.all_bsc_lectures, st.session_state.all_msc_lectures], ignore_index=True))
    # st.write(pd.concat([st.session_state.all_bsc_lectures.reset_index(drop=True), st.session_state.all_msc_lectures.reset_index(drop=True)], ignore_index=True))