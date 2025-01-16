import streamlit as st
import utils
import pandas as pd

st.logo('images/Goethe-Logo.jpg')
st.sidebar.image('images/Goethe-Logo.jpg')

st.session_state.all_bsc_lectures = utils.return_all_bsc_lectures().reset_index(drop=True)
st.session_state.all_msc_lectures = utils.return_all_msc_lectures().reset_index(drop=True)

stats_all_lectures = pd.concat([st.session_state.all_bsc_lectures, st.session_state.all_msc_lectures], ignore_index=True)

st.subheader('Statistiken')

overview_modules_lectures = pd.DataFrame([
    ['Module insgesamt', len(st.session_state.all_modules)],
    ['BSc Module', len(st.session_state.bsc_modules)],
    ['MSc Module', len(st.session_state.msc_modules)],
    ['Veranstaltungen insgesamt', len(st.session_state.all_bsc_lectures) + len(st.session_state.all_msc_lectures)],
    ['BSc Veranstaltungen', len(st.session_state.all_bsc_lectures)],
    ['MSc Veranstaltungen', len(st.session_state.all_msc_lectures)]
], columns=['Titel', 'Anzahl'])


tab1, tab2 = st.tabs(['Diagramme', 'Tabellen'])

with tab1:
    overview_modules_lectures.set_index("Titel", inplace=True)
    st.bar_chart(overview_modules_lectures)
    st.bar_chart(stats_all_lectures['Modulbeauftragte*r'].value_counts())
    st.bar_chart(stats_all_lectures['CP'].value_counts())
    st.bar_chart(stats_all_lectures['SWS'].value_counts())
    st.bar_chart(stats_all_lectures['Sprache'].value_counts())

with tab2:
    st.write(overview_modules_lectures)
    st.write(stats_all_lectures.keys())
    st.write(stats_all_lectures['Modulbeauftragte*r'].value_counts())
    st.write(stats_all_lectures['CP'].value_counts())
    st.write(stats_all_lectures['SWS'].value_counts())
    st.write(stats_all_lectures['Sprache'].value_counts())
