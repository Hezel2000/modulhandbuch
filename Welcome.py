import streamlit as st

# t = {
#     "Titel": ["BP1", "Geosciences 1", "Geowissenschaften 1", "Pflichtmodul", "7 CP (insg.) = 210 h", "Kontaktstudium 100 h", "Selbststudium 110 h", "4 SWS + 5 Tage"],
#     "Inhalte": "Das Modul umfasst die für die Studierenden grundlegende Haupteinführungsveranstaltung „System Erde“ sowie 5 Tage Geländeübung. \\n In „System Erde“ werden grundlegende geowissenschaftliche Konzepte einführend vorgestellt und die Verbindungen zwischen den Einzeldisziplinen betont. Die Studierenden lernen den Planeten Erde, seine Entwicklungsgeschichte, aber auch notwendige geowissenschaftliche Konzepte und Begriffe kennen. Durch einfache Übungen im Selbststudium können Studierende die Lerninhalte aktiv festigen, während ein Tutorium weitere Hilfestellung bietet. In den 5 Geländetagen aus dem Angebot an geologischen Anfänger*innen-Geländeübungen lernen die Studierenden die Grundprinzipien der geowissenschaftlichen Geländearbeit kennen. Im Gelände werden so Prinzipien der Stratigraphie, der Gesteinserkennung und von 3D-Strukturen verknüpfend eingeführt.",
#     "Lernergebnisse / Kompetenzziele": "In diesem Modul erlernen die Studierenden die Grundprinzipien der Geowissenschaften und praktizieren diese im Rahmen von ersten Geländeübungen. Dadurch werden die Grundlagen für alle weiteren geowissenschaftlichen Lehrveranstaltungen - sowohl theoretisch als auch praktisch – sichergestellt. Die Inhalte umfassen unter anderem die Entstehung von Sonnensystem und Erde, Zusammensetzung, Schalenbau und Bausteine der Erde, Plattentektonik als übergreifendes Konzept, geologische Zeit und ihre Bestimmung, Entwicklung des Lebens und Evolution, Erosion und Sedimentation. Die Wechselwirkungen und Rückkopplungsmechanismen zwischen den diversen Sphären sowie die zeitliche Entwicklung des Planeten Erde sollen die Neugier auf weiterführende Lehrveranstaltungen wecken.",
#     "Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls": "-",
#     "Empfohlene Voraussetzungen": "\-",
#     "Organisatorische Hinweise": "-",
#     "Zuordnung des Moduls (Studiengang / Fachbereich)": "B.Sc. Geowissenschaften / FB11",
#     "Verwendbarkeit des Moduls für andere Studiengänge": "B.Sc. Orientierungsstudium Natur- und Lebenswissenschaften, B.Sc. Geographie, B.Sc. Mathematik, B.Sc. Chemie",
#     "Häufigkeit des Angebots": "„System Erde“: jährlich im Wintersemester Geländeübungen: nach Angebot",
#     "Dauer des Moduls": "2 Semester",
#     "Modulbeauftragte / Modulbeauftragter": "Prof. Dr. Wolfgang Müller",
#     "Studiennachweise/ ggf. als Prüfungsvorleistungen":
#       {"Teilnahmenachweise": "-", "Leistungsnachweise": "Erfolgreich absolvierte Übungen zu „System Erde“ (Prüfungsvorleistung) Berichte zu den Geländeübungen"},
#     "Lehr- / Lernformen": "Vorlesung, Übung, Geländeübung ",
#     "Unterrichts- / Prüfungssprache": "Deutsch, Englisch",
#     "Modulprüfung":
#       {"Modulabschlussprüfung bestehend aus:": 'Klausur (90 min) zu "System Erde"', "kumulative Modulprüfung bestehend aus:": '-', "Bildung der Modulnote bei kumulativen Modulprüfungen:": '-'},
#     "Prüfung": "Was auch immer"
# }
t = "Module as json/BP1.json"
st.write(t)

st.title(t['Titel'][0])

col1, col2, col3, col4 = st.columns(4)

with col1:
  st.write(t['Titel'][2])

with col2:
  st.write(t['Titel'][3])

with col3:
  st.write(t['Titel'][7])

with col4:
  st.write(t['Titel'][4])

st.write(t['Titel'][5], ' ---- ', t['Titel'][6])


with st.expander('Inhalte', expanded=False):
  t["Inhalte"]

with st.expander('Lernergebnisse / Kompetenzziele', expanded=False):
  t["Lernergebnisse / Kompetenzziele"]

st.write('**Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls:**', ' ', t['Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls'])
st.write('**Empfohlene Voraussetzungen:**', ' ', t['Empfohlene Voraussetzungen'])
st.write('**Organisatorische Hinweise:**', ' ', t['Organisatorische Hinweise'])
st.write('**Zuordnung des Moduls (Studiengang / Fachbereich):**', ' ', t['Zuordnung des Moduls (Studiengang / Fachbereich)'])
st.write('**Verwendbarkeit des Moduls für andere Studiengänge:**', ' ', t['Verwendbarkeit des Moduls für andere Studiengänge'])
st.write('**Häufigkeit des Angebots:**', ' ', t['Häufigkeit des Angebots'])
st.write('**Dauer des Moduls:**', ' ', t['Dauer des Moduls'])
st.write('**Modulbeauftragte / Modulbeauftragter:**', ' ', t['Modulbeauftragte / Modulbeauftragter'])
st.write('**Studiennachweise/ ggf. als Prüfungsvorleistungen:**', ' ', t['Studiennachweise/ ggf. als Prüfungsvorleistungen'])
st.write('**Lehr- / Lernformen:**', ' ', t['Lehr- / Lernformen'])
st.write('**Unterrichts- / Prüfungssprache:**', ' ', t['Unterrichts- / Prüfungssprache'])
st.write('**Modulprüfung:**', ' ', t['Modulprüfung'])

st.divider()

st.write('**Prüfung:**', ' ', t['Prüfung'])