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
def search_all(data, search_query):
    results = {}

    for file_name, json_data in data.items():
        # Implement your search logic here
        if search_query in json.dumps(json_data):
            results[file_name] = json_data

    return results


st.header("Volltextsuche")
search_query = st.text_input("Sucheingabe", placeholder='Sucheingabe', label_visibility='collapsed')

if search_query:
    results = search_all(data, search_query)
    for file_name, json_data in results.items():
        module_content = json_data
        module_name = module_content['Modul-Code'] + ': ' + module_content['Modul-Name-de']
        
        with st.expander(module_name, expanded=False):
            st.title(module_content['Modul-Code'] + ': ' + module_content['Modul-Name-de'])

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write(module_content['Modul-Name-de'])

            with col2:
                st.write(module_content['Modul-Typ'])

            with col3:
                st.write(module_content['Anzahl SWS'])

            with col4:
                st.write(module_content['Anzhal CP und Arbeitsaufwand'])

            st.markdown(f'Kontaktstudium {module_content["Kontaktstudium"]}  & Selbststudium {module_content["Selbststudium"]}')
            st.markdown(f''':blue[**Inhalte**]\n {module_content["Inhalte"]}''')
            st.markdown(f''':blue[**Lernergebnisse / Kompetenzziele**]\n {module_content["Lernergebnisse / Kompetenzziele"]}''')
            st.markdown(f''':blue[**Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls:**]\n {module_content["Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls"]}''')
            st.markdown(f''':blue[**Empfohlene Voraussetzungen**] \n {module_content["Empfohlene Voraussetzungen"]}''')
            st.markdown(f''':blue[**Organisatorische Hinweise**]\n {module_content["Organisatorische Hinweise"]}''')
            st.markdown(f''':blue[**Zuordnung des Moduls (Studiengang / Fachbereich)**]\n {module_content["Zuordnung des Moduls (Studiengang / Fachbereich)"]}''')
            st.markdown(f''':blue[**Verwendbarkeit des Moduls für andere Studiengänge**]\n {module_content["Verwendbarkeit des Moduls für andere Studiengänge"]}''')
            st.markdown(f''':blue[**Häufigkeit des Angebots**]\n {module_content["Häufigkeit des Angebots"]}''')
            st.markdown(f''':blue[**Dauer des Moduls**]\n {module_content["Dauer des Moduls"]}''')
            st.markdown(f''':blue[**Modulbeauftragte / Modulbeauftragter:**] {module_content["Modulbeauftragte / Modulbeauftragter"]}''')
            st.markdown(f"""
            <div style="color: #4a90e2; font-weight: bold; margin-bottom: 10px;">Studiennachweise/ ggf. als Prüfungsvorleistungen</div>
            <ul style="list-style-type: none; margin-left: 0; padding-left: 0;">
                <li>
                    <span style="color: green; font-weight: bold;">Teilnahmenachweise:</span> {module_content["Studiennachweise/ ggf. als Prüfungsvorleistungen"]["Teilnahmenachweise"]}
                </li>
                <li>
                    <span style="color: green; font-weight: bold;">Leistungsnachweise:</span> {module_content["Studiennachweise/ ggf. als Prüfungsvorleistungen"]["Leistungsnachweise"]}
                </li>
            </ul>
            """, unsafe_allow_html=True)
            st.markdown(f''':blue[**Lehr- / Lernformen:**] {module_content["Lehr- / Lernformen"]}''')
            st.markdown(f''':blue[**Unterrichts- / Prüfungssprache:**] {module_content["Unterrichts- / Prüfungssprache"]}''')
            st.markdown(f"""
            <div style="color: #4a90e2; font-weight: bold; margin-bottom: 10px;">Modulprüfung</div>
            <ul style="list-style-type: none; margin-left: 0; padding-left: 0;">
                <li>
                    <span style="color: green; font-weight: bold;">Modulabschlussprüfung bestehend aus</span> {module_content["Modulprüfung"]["Modulabschlussprüfung bestehend aus"]}
                </li>
                <li>
                    <span style="color: green; font-weight: bold;">kumulative Modulprüfung bestehend aus</span> {module_content["Modulprüfung"]["kumulative Modulprüfung bestehend aus"]}
                </li>
                <li>
                    <span style="color: green; font-weight: bold;">Bildung der Modulnote bei kumulativen Modulprüfungen</span> {module_content["Modulprüfung"]["Bildung der Modulnote bei kumulativen Modulprüfungen"]}
                </li>
            </ul>
            """, unsafe_allow_html=True)
                        
            # st.table(module_content['Übersicht'])


# # ---------------------
            
#             st.divider()
#             st.header('Bemerkungen')

#             st.write('**Prüfung:**', ' ', module_content['Prüfung'])
            
            # st.divider()
            # col1, col2 = st.columns([30,70])
            # with col1:
            #     sel_version = st.selectbox('Version', module_content['Version'], key=module_name)
            # with col2:
            #     st.write(module_content['Änderung'][sel_version])
   
