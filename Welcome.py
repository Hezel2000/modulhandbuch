import streamlit as st
import json

with open("Module as json/BP1.json", 'r') as json_file:
  module_content = json.load(json_file)

st.title(module_content['Titel'][0] + ': ' + module_content['Titel'][2])

col1, col2, col3, col4 = st.columns(4)

with col1:
  st.write(module_content['Titel'][1])

with col2:
  st.write(module_content['Titel'][3])

with col3:
  st.write(module_content['Titel'][7])

with col4:
  st.write(module_content['Titel'][4])

st.write(module_content['Titel'][5], ' - & - ', module_content['Titel'][6])


with st.expander('Inhalte', expanded=False):
  module_content["Inhalte"]

with st.expander('Lernergebnisse / Kompetenzziele', expanded=False):
  module_content["Lernergebnisse / Kompetenzziele"]

st.write('**Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls:**', ' ', module_content['Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls'])
st.write('**Empfohlene Voraussetzungen:**', ' ', module_content['Empfohlene Voraussetzungen'])
st.write('**Organisatorische Hinweise:**', ' ', module_content['Organisatorische Hinweise'])
st.write('**Zuordnung des Moduls (Studiengang / Fachbereich):**', ' ', module_content['Zuordnung des Moduls (Studiengang / Fachbereich)'])
st.write('**Verwendbarkeit des Moduls für andere Studiengänge:**', ' ', module_content['Verwendbarkeit des Moduls für andere Studiengänge'])
st.write('**Häufigkeit des Angebots:**', ' ', module_content['Häufigkeit des Angebots'])
st.write('**Dauer des Moduls:**', ' ', module_content['Dauer des Moduls'])
st.write('**Modulbeauftragte / Modulbeauftragter:**', ' ', module_content['Modulbeauftragte / Modulbeauftragter'])
st.write('**Studiennachweise/ ggf. als Prüfungsvorleistungen:**')
#st.write('*Teilnahmenachweise*', module_content['Studiennachweise/ ggf. als Prüfungsvorleistungen']['Teilnahmenachweise'])
#st.write('*Leistungsnachweise*', module_content['Studiennachweise/ ggf. als Prüfungsvorleistungen']['Leistungsnachweise'])
Teilnahmenachweise_coloured = {'colored_text': '<span style="color:#0077be;">&nbsp;&nbsp;&nbsp;&nbsp;*Teilnahmenachweise*</span>',
           'additional_text': module_content['Studiennachweise/ ggf. als Prüfungsvorleistungen']['Teilnahmenachweise']}
st.write(Teilnahmenachweise_coloured['colored_text'], Teilnahmenachweise_coloured['additional_text'], unsafe_allow_html=True)
Leistungsnachweise_coloured = {'colored_text': '<span style="color:#0077be;">&nbsp;&nbsp;&nbsp;&nbsp;*Leistungsnachweise*</span>',
           'additional_text': module_content['Studiennachweise/ ggf. als Prüfungsvorleistungen']['Leistungsnachweise']}
st.write(Leistungsnachweise_coloured['colored_text'], Leistungsnachweise_coloured['additional_text'], unsafe_allow_html=True)
st.write('**Lehr- / Lernformen:**', ' ', module_content['Lehr- / Lernformen'])
st.write('**Unterrichts- / Prüfungssprache:**', ' ', module_content['Unterrichts- / Prüfungssprache'])
st.write('**Modulprüfung:**')
modulabschluss_coloured = {'colored_text': '<span style="color:#0077be;">&nbsp;&nbsp;&nbsp;&nbsp;*Modulabschlussprüfung bestehend aus:*</span>',
           'additional_text': module_content['Modulprüfung']['Modulabschlussprüfung bestehend aus:']}
st.write(modulabschluss_coloured['colored_text'], modulabschluss_coloured['additional_text'], unsafe_allow_html=True)
kumulative_coloured = {'colored_text': '<span style="color:#0077be;">&nbsp;&nbsp;&nbsp;&nbsp;*kumulative Modulprüfung bestehend aus:*</span>',
           'additional_text': module_content['Modulprüfung']['kumulative Modulprüfung bestehend aus:']}
st.write(kumulative_coloured['colored_text'], kumulative_coloured['additional_text'], unsafe_allow_html=True)
modulnote_coloured = {'colored_text': '<span style="color:#0077be;">&nbsp;&nbsp;&nbsp;&nbsp;*Bildung der Modulnote bei kumulativen Modulprüfungen:*</span>',
           'additional_text': module_content['Modulprüfung']['Bildung der Modulnote bei kumulativen Modulprüfungen:']}
st.write(modulnote_coloured['colored_text'], modulnote_coloured['additional_text'], unsafe_allow_html=True)


st.divider()
st.header('Erläuterungen')

st.write('**Prüfung:**', ' ', module_content['Prüfung'])
