import streamlit as st

st.title('Willkommen beim online-Modulhandbuch des Ifg')

st.markdown('''
            :orange[Alle Einträge hier sind rechtlich nicht bindend. Es handelt sich um eine inoffizielle Seite,
            die zwar von der Studienkommission gepflegt wird, jedoch zählen im Zweifelsfall immer und ausschließlich
            die Angaben im Modulhandbuch, sowie die von der Studienkommission beschlossenen Änderungen.]  
            Das offizielle Modulhandbuch ist hier zu finden, allerdings sind die beschlossenen Änderungen der Studienkommission
            zu beachten, die hier soweit es möglich ist abgebildet sind.
            ''')

st.markdown('''
            Diese Version ist zunächst für eine interne Evaluationsphase gedacht. Alles grundlegende funktioniert, aber es gibt noch einige Fehler, die unten gelistet sind. An deren Korrektur arbeite ich immer mal wieder. 
            Im Moment geht es darum einmal zu schauen, ob so alles passt, und wie die Funktionalität erweitert/verbessert/angepasst/... werden könnte. Außerdem kann ein bisschen gelernt werden, wie man die Einträge aktualisiert.             
            ''')


st.header(''':blue[Bekannte Fehler etc.]''')
st.markdown('''
            - Ich gehe nach und nach alle Einträge durch und vergleich die mit dem Modulhandbuch. Gecheckt bis inkl. BP5 (Reihenfolge entsprechend *Alle Module* links). 
            - Hin und wieder taucht eine Fehlermeldung auf, die mit *DuplicateWidgetID:* beginnt (oder eine ähnliche). Die dürfen getrost ignoriert werden (wenn die strören, reload der Seite)). 
            ''')