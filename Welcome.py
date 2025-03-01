import streamlit as st
import utils


st.logo('images/Goethe-Logo.jpg')
st.sidebar.image('images/Goethe-Logo.jpg')
# if 'all_modules' not in st.session_state:
#     st.session_state.all_modules = {}

st.session_state.all_modules, st.session_state.all_module_names, st.session_state.bsc_modules, st.session_state.msc_modules = utils.initialise_all_modules()
st.session_state.all_bsc_lectures = utils.return_all_bsc_lectures().reset_index(drop=True)
st.session_state.all_msc_lectures = utils.return_all_msc_lectures().reset_index(drop=True)

# # Volltextsuche
# def search_all(data, search_query):
#     results = {}

#     for file_name, json_data in data.items():
#         # Implement your search logic here
#         if search_query in json.dumps(json_data):
#             results[file_name] = json_data

st.subheader('Willkommen beim digitalen Modulhandbuch des IfG')


with st.expander(':orange[Haftungsausschluss]'):
    st.info('''
    :orange[Die Einträge in diesem digitalen Modulhandbuch werden zwar von der Studienkommission gepflegt, sind aber dennoch **rechtlich nicht bindend**.  
    Rechtlich gelten ausschließlich das offizielle Modulhandbuch (s. unten) zusammen mit den beschlossenen Änderungen durch die Studienkommission.]

    Das offizielle Modulhandbuch ist [hier](https://www.uni-frankfurt.de/89797195/Modulhandbuch_Geowissenschaften.pdf) zu finden. Beschlossene Änderungen durch die Studienkommission sind zu beachten.

    Alle weiteren Informationen zum Studium gibt es [hier](https://www.uni-frankfurt.de/45741218/Willkommen_am_Institut_für_Geowissenschaften?legacy_request=1).
''')



st.subheader(''':blue[Kurzanleitung]''')
st.markdown('''
            **:green[Navigation]**  
            Bei kleinen Bildschirmen wie z.B. Mobilgeräten wird die Navigationsleiste zur Linken eventuell versteckt. Mit dem kleinen Pfeil links oben lässt sich die Navitationsleiste ausklappen.
            
            **:green[Tabellen]**  
            In Tabellen kann je nach Bildschirmgröße nach unten und/oder rechts gescrollt werden.  
            Durch einen Klick auf einen Spalten-Titel wird die gesamte Tabelle nach der entsprechenden Spalte sortiert.  
            Rechts oben über jeder Tablle gibt es 3 icons: Download der Tablle, Suche in der Tabelle, Vergrößern der Tabelle


            **:green[Abbildungen/Bilder]**  
            Wird die Maus über eine Abbildung beweget, erscheint rechts oben neben dem Bild ein icon, das, angeklickt, die Abbildung vergrößert.
            ''')

st.subheader(''':blue[Feedback, Fragen & Fehlerkorrektur ...]''')
st.markdown('''... und weiteres am Besten ins Feedback-Formular schreiben, s. links ganz unten.''')
