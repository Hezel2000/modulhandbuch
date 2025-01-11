import streamlit as st
import pandas as pd

stats_all_lectures = pd.concat([st.session_state.all_bsc_lectures, st.session_state.all_msc_lectures], ignore_index=True)

st.subheader('Statistiken')
st.markdown(''':red[Sind noch komplett in Vorbereitung]''')
# st.divider()

# st.markdown(f'''Es gibt insgesamt  
#             - {len(st.session_state.all_modules)} Module insgesamt  
#             - {len(st.session_state.bsc_modules)} BSc Module  
#             - {len(st.session_state.msc_modules)} MSc Module  
#             - {len(st.session_state.all_bsc_lectures) + len(st.session_state.all_msc_lectures)} Veranstaltungen insgesamt  
#             - {len(st.session_state.all_bsc_lectures)} BSc Veranstaltungen  
#             - {len(st.session_state.all_msc_lectures)} BSc Veranstaltungen  
#             ''')

# overview_modules_lectures = pd.DataFrame([
#             ['Module insgesamt', {len(st.session_state.all_modules)}],
#             ['BSc Module', {len(st.session_state.bsc_modules)}],
#             ['MSc Module', {len(st.session_state.msc_modules)}],
#             ['Veranstaltungen insgesamt', {len(st.session_state.all_bsc_lectures) + len(st.session_state.all_msc_lectures)}],
#             ['BSc Veranstaltungen', {len(st.session_state.all_bsc_lectures)}],
#             ['BSc Veranstaltungen', {len(st.session_state.all_msc_lectures)}]
#     ], columns=['Titel', 'Anzahl'])

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
