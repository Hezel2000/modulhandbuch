import streamlit as st
import utils

st.logo('images/Goethe-Logo.jpg')


# Volltextsuche
def search_all(data, search_query):
    results = {}

    for file_name, json_data in data.items():
        # Implement your search logic here
        if search_query in json.dumps(json_data):
            results[file_name] = json_data

st.subheader('Willkommen beim online-Modulhandbuch des Ifg')

st.markdown('''
            :orange[Alle Einträge hier sind rechtlich nicht bindend. Es handelt sich um eine inoffizielle Seite,
            die zwar von der Studienkommission gepflegt wird, jedoch zählen im Zweifelsfall immer und ausschließlich
            die Angaben im Modulhandbuch, sowie die von der Studienkommission beschlossenen Änderungen.]  
            Das offizielle Modulhandbuch ist [hier](https://www.uni-frankfurt.de/89797195/Modulhandbuch_Geowissenschaften.pdf) zu finden, allerdings sind die beschlossenen Änderungen der Studienkommission
            zu beachten, die hier soweit es möglich ist abgebildet sind.  
            Alle weiteren Infos zum Studium  [hier](https://www.uni-frankfurt.de/45741218/Willkommen_am_Institut_für_Geowissenschaften?legacy_request=1).
            ''')

st.markdown('''
            - Diese Version ist zunächst für eine interne Evaluationsphase gedacht. Alles grundlegende funktioniert, aber es gibt noch ein paar Korrekturen an denen ich arbeite, die unten gelistet sind. 
            - Im Moment geht es darum einmal zu schauen, ob so alles passt, und wie die Funktionalität erweitert/verbessert/angepasst/... werden könnte. Außerdem kann ein bisschen gelernt werden, wie man die Einträge aktualisiert.  
            - Kommentare am Besten ins Feedback schreiben, das geht in ein Sheet, in dem alles gesammelt wird und dort entsprechend abgekakt werden kann.
            ''')


st.subheader(''':blue[Bemerkungen]''')
st.markdown('''
            - Ich gehe nach und nach alle Einträge durch und vergleich die mit dem Modulhandbuch. Gecheckt bis inkl. BP20, aber irgendwie ist nicht klar, ob das pdf oder das doc gilt.
            ''')


st.sidebar.image('images/Goethe-Logo.jpg')