import streamlit as st

st.logo('images/Goethe-Logo.jpg')

st.title('Willkommen beim online-Modulhandbuch des Ifg')

st.markdown('''
            :orange[Alle Einträge hier sind rechtlich nicht bindend. Es handelt sich um eine inoffizielle Seite,
            die zwar von der Studienkommission gepflegt wird, jedoch zählen im Zweifelsfall immer und ausschließlich
            die Angaben im Modulhandbuch, sowie die von der Studienkommission beschlossenen Änderungen.]  
            Das offizielle Modulhandbuch ist [hier](https://www.uni-frankfurt.de/89797195/Modulhandbuch_Geowissenschaften.pdf) zu finden, allerdings sind die beschlossenen Änderungen der Studienkommission
            zu beachten, die hier soweit es möglich ist abgebildet sind. Alle weiteren Infos zum Studium dann [hier](https://www.uni-frankfurt.de/45741218/Willkommen_am_Institut_für_Geowissenschaften?legacy_request=1)
            ''')

st.markdown('''
            - Diese Version ist zunächst für eine interne Evaluationsphase gedacht. Alles grundlegende funktioniert, aber es gibt noch einige Fehler, die unten gelistet sind. An deren Korrektur arbeite ich immer mal wieder. 
            - Im Moment geht es darum einmal zu schauen, ob so alles passt, und wie die Funktionalität erweitert/verbessert/angepasst/... werden könnte. Außerdem kann ein bisschen gelernt werden, wie man die Einträge aktualisiert.  
            - Kommentare am Besten ins Feedback schreiben, das geht in ein Sheet, in dem alles gesammelt wird und dort entsprechend abgekakt werden kann.
            ''')


st.header(''':blue[Bekannte Fehler etc.]''')
st.markdown('''
            - Ich gehe nach und nach alle Einträge durch und vergleich die mit dem Modulhandbuch. Gecheckt bis inkl. BP5 (Reihenfolge entsprechend *Alle Module* links), 15a, 15b, 16a, 16b. 
            - Hin und wieder taucht eine Fehlermeldung auf, die mit *DuplicateWidgetID:* beginnt (oder eine ähnliche). Die dürfen getrost ignoriert werden (wenn die strören, reload der Seite)). 
            ''')


st.sidebar.image('images/Goethe-Logo.jpg')

