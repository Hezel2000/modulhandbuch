import streamlit as st
import os
import json

folder_path = 'Module as json'
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

data = {}  # Dictionary to store loaded JSON data

for json_file in json_files:
    with open(os.path.join(folder_path, json_file), 'r') as file:
        data[json_file] = json.load(file)

# Search function
def search_json_files(data, search_query):
    results = {}

    for file_name, json_data in data.items():
        # Implement your search logic here
        if search_query in json.dumps(json_data):
            results[file_name] = json_data

    return results


st.header("Volltextsuche")
search_query = st.text_input("Sucheingabe", placeholder='Sucheingabe', label_visibility='collapsed')

if search_query:
    results = search_json_files(data, search_query)
    st.write("Suchergebnisse:")
    for file_name, json_data in results.items():
        module_content = json_data
        module_name = module_content['Titel'][0] + ': ' + module_content['Titel'][2]
        
        with st.expander(module_name, expanded=False):
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
           
            st.write("**Inhalte**")
            st.write(module_content["Inhalte"])
            st.write("**Lernergebnisse / Kompetenzziele**")
            st.write(module_content["Lernergebnisse / Kompetenzziele"])

            st.write('**Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls:**', ' ', module_content['Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls'])
            st.write('**Empfohlene Voraussetzungen:**', ' ', module_content['Empfohlene Voraussetzungen'])
            st.write('**Organisatorische Hinweise:**', ' ', module_content['Organisatorische Hinweise'])
            st.write('**Zuordnung des Moduls (Studiengang / Fachbereich):**', ' ', module_content['Zuordnung des Moduls (Studiengang / Fachbereich)'])
            st.write('**Verwendbarkeit des Moduls für andere Studiengänge:**', ' ', module_content['Verwendbarkeit des Moduls für andere Studiengänge'])
            st.write('**Häufigkeit des Angebots:**', ' ', module_content['Häufigkeit des Angebots'])
            st.write('**Dauer des Moduls:**', ' ', module_content['Dauer des Moduls'])
            st.write('**Modulbeauftragte / Modulbeauftragter:**', ' ', module_content['Modulbeauftragte / Modulbeauftragter'])
            st.write('**Studiennachweise/ ggf. als Prüfungsvorleistungen:**')
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

            st.table(module_content['Übersicht'])


# ---------------------
            
            st.divider()
            st.header('Bemerkungen')

            st.write('**Prüfung:**', ' ', module_content['Prüfung'])
            
            st.divider()
            col1, col2 = st.columns([30,70])
            with col1:
                sel_version = st.selectbox('Version', module_content['Version'], key=module_name)
            with col2:
                st.write(module_content['Änderung'][sel_version])
   
