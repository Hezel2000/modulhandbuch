import streamlit as st
import re
import os
import json
import pandas as pd

# folder_path = 'Module als json'
# json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# st.session_state.all_modules = {}  # Dictionary to store loaded JSON data
# st.session_state.bsc_modules = {}
# st.session_state.msc_modules = {}

# for json_file in json_files:
#     with open(os.path.join(folder_path, json_file), 'r') as file:
#         st.session_state.all_modules[json_file] = json.load(file)

# all_module_names = list(st.session_state.all_modules.keys())

# for i in all_module_names:
#     if st.session_state.all_modules[i]['Modul-Code'][0] == 'B':
#         st.session_state.bsc_modules[i] = st.session_state.all_modules[i] 
#     elif st.session_state.all_modules[i]['Modul-Code'][0] == 'M':
#         st.session_state.msc_modules[i] = st.session_state.all_modules[i]
#     else:
#         st.write('something went wrong')



# def initialise_all_modules_bsc_modules_msc_modules():
#     folder_path = 'Module als json'
#     json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

#     for json_file in json_files:
#         with open(os.path.join(folder_path, json_file), 'r') as file:
#             st.session_state.all_modules[json_file] = json.load(file)

#     all_module_names = list(st.session_state.all_modules.keys())

#     for i in all_module_names:
#         if st.session_state.all_modules[i]['Modul-Code'][0] == 'B':
#             st.session_state.bsc_modules[i] = st.session_state.all_modules[i] 
#         elif st.session_state.all_modules[i]['Modul-Code'][0] == 'M':
#             st.session_state.msc_modules[i] = st.session_state.all_modules[i]
#         else:
#             st.write('something went wrong')
#     return st.session_state.all_modules, st.session_state.bsc_modules, st.session_state.msc_modules


def initialise_all_modules():
    folder_path = 'Module als json'
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    all_modules = {}
    for json_file in json_files:
        with open(os.path.join(folder_path, json_file), 'r') as file:
            all_modules[json_file] = json.load(file)

    all_module_names = list(all_modules.keys())
    
    bsc_modules = {}
    msc_modules = {}
    for i in all_module_names:
        if all_modules[i]['Modul-Code'][0] == 'B':
            bsc_modules[i] = all_modules[i] 
        elif all_modules[i]['Modul-Code'][0] == 'M':
            msc_modules[i] = all_modules[i]

    return all_modules, all_module_names, bsc_modules, msc_modules





# Darstellung der Module
def results_modules(volltext_results, version_key):
    results = volltext_results
    for file_name, json_data in results.items():
        module_content = json_data
        module_name = module_content['Modul-Code'] + ': ' + module_content['Modul-Name-de']
        
        with st.expander(module_name, expanded=False):
            st.markdown(f'''#### :blue[{module_content['Modul-Code']}: {module_content['Modul-Name-de']}]''')

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write(module_content['Modul-Name-de'])

            with col2:
                st.write(module_content['Modul-Typ'])

            with col3:
                st.write(module_content['Anzahl SWS'])

            with col4:
                st.write(module_content['Anzhal CP und Arbeitsaufwand'])

            st.markdown(f'<div style="text-align: right;">Kontaktstudium {module_content["Kontaktstudium"]}  & Selbststudium {module_content["Selbststudium"]}</div>', unsafe_allow_html=True)
            st.markdown(f':blue[**Inhalte**]')
            st.markdown(module_content["Inhalte"].replace("\n", "<br>"), unsafe_allow_html=True)
            st.markdown(f':blue[**Lernergebnisse / Kompetenzziele**]')
            st.markdown(module_content["Lernergebnisse / Kompetenzziele"].replace("\n", "<br>"), unsafe_allow_html=True)
            st.markdown(f':blue[**Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls**]')
            st.markdown(module_content["Teilnahmevoraussetzungen für Modul bzw. für einzelne Lehrveranstaltungen des Moduls"].replace("\n", "<br>"), unsafe_allow_html=True)
            st.markdown(f':blue[**Empfohlene Voraussetzungen**]')
            st.markdown(module_content["Empfohlene Voraussetzungen"].replace("\n", "<br>"), unsafe_allow_html=True)
            st.markdown(f':blue[**Organisatorische Hinweise**]')
            st.markdown(module_content["Organisatorische Hinweise"].replace("\n", "<br>"), unsafe_allow_html=True)
            st.markdown(f''':blue[**Zuordnung des Moduls (Studiengang / Fachbereich)**]\n {module_content["Zuordnung des Moduls (Studiengang / Fachbereich)"]}''')
            st.markdown(f''':blue[**Verwendbarkeit des Moduls für andere Studiengänge**]\n {module_content["Verwendbarkeit des Moduls für andere Studiengänge"]}''')
            st.markdown(f''':blue[**Häufigkeit des Angebots**]\n {module_content["Häufigkeit des Angebots"]}''')
            st.markdown(f''':blue[**Dauer des Moduls**]\n {module_content["Dauer des Moduls"]}''')
            st.markdown(f''':blue[**Modulbeauftragte / Modulbeauftragter**] {module_content["Modulbeauftragte / Modulbeauftragter"]}''')
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
            st.markdown(f''':blue[**Lehr- / Lernformen**] {module_content["Lehr- / Lernformen"]}''')
            st.markdown(f''':blue[**Unterrichts- / Prüfungssprache**] {module_content["Unterrichts- / Prüfungssprache"]}''')
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
            
            df = pd.DataFrame(module_content['Semester-Tabelle'])
            if module_content['Modul-Code'][0] == 'B':                
                df.columns = ["Titel", "LV-Form", "SWS", "CP", "1. Sem", "2. Sem", "3. Sem", "4. Sem", "5. Sem", "6. Sem"]
            elif module_content['Modul-Code'][0] == 'M':
                df.columns = ["Titel", "LV-Form", "SWS", "CP", "1. Sem", "2. Sem", "3. Sem", "4. Sem"]

            df = df.reset_index(drop=True)
            st.dataframe(df)

            
            st.divider()
            st.header('Bemerkungen')

            st.write(f'{module_content["Bemerkungen"]}')
            
            st.divider()
            col1, col2 = st.columns([30,70])
            with col1:
                sel_version = st.selectbox('Version', module_content['Version'], key=f'{module_content["Modul-Code"]}_{version_key}')
            with col2:
                st.write(f'{module_content["Änderung"][sel_version]}')



def sort_modules(data):
    # Helper function to split the alphabetic and numeric parts
    def split_alpha_numeric(s):
        match = re.match(r'([^\d]*)(\d*)', s)
        alpha = match.group(1)  # Alphabetic part
        num = int(match.group(2)) if match.group(2) else float('inf')  # Numeric part or high number
        return alpha, num

    # Filter and sort based on 'Modul-Code'
    sorted_items = sorted(
        (item for item in data.items() if item[1]['Modul-Code']),
        key=lambda x: split_alpha_numeric(x[1]['Modul-Code'])
    )

    # Convert back to a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict


# def sort_MSc_modules(data):
#     # Helper function to split the alphabetic and numeric parts
#     def split_alpha_numeric(s):
#         match = re.match(r'([^\d]*)(\d*)', s)
#         alpha = match.group(1)  # Alphabetic part
#         num = int(match.group(2)) if match.group(2) else float('inf')  # Numeric part or high number
#         return alpha, num

#     # Filter and sort based on 'Modul-Code'
#     sorted_items = sorted(
#         (item for item in data.items() if item[1]['Modul-Code'].startswith('M')),
#         key=lambda x: split_alpha_numeric(x[1]['Modul-Code'])
#     )

#     # Convert back to a dictionary
#     sorted_dict = dict(sorted_items)
#     return sorted_dict


def return_all_bsc_lectures():
    header = ['Titel', 'Code', 'Modul', 'Typ', 'SWS', 'CP', 'Modulbeauftragte*r', 'Studiennachweise', 'Lehr-/Lernform', 'Modulabschlussprüfung', 'kumulative Modulabschlussprüfung', 'Sprache']
    all_module_names = list(st.session_state.all_modules.keys())
    all_bsc_lectures = []
    for i in all_module_names:
        if st.session_state.all_modules[i]['Modul-Code'][0] == 'B':
            full_semester_table = st.session_state.bsc_modules[i]['Semester-Tabelle']
            semester_table_titles = [k[0] for k in full_semester_table]
            items_to_remove = {"Auswahl aus", "Auswahl aus:", "Modulprüfung", "Modulprüfung:", "Summe", "Summe:"}
            semester_table = [item for item in semester_table_titles if item not in items_to_remove]
            modul_lectures = []
            for j in semester_table:
                modul_lectures.append([j, st.session_state.all_modules[i]['Modul-Code'], st.session_state.all_modules[i]['Modul-Name-de'], st.session_state.all_modules[i]['Modul-Typ'], st.session_state.all_modules[i]['Anzahl SWS'], st.session_state.all_modules[i]['Anzhal CP und Arbeitsaufwand'], st.session_state.all_modules[i]["Modulbeauftragte / Modulbeauftragter"], st.session_state.all_modules[i]["Studiennachweise/ ggf. als Prüfungsvorleistungen"]["Teilnahmenachweise"], st.session_state.all_modules[i]["Lehr- / Lernformen"], st.session_state.all_modules[i]["Modulprüfung"]["Modulabschlussprüfung bestehend aus"], st.session_state.all_modules[i]["Modulprüfung"]["kumulative Modulprüfung bestehend aus"], st.session_state.all_modules[i]["Unterrichts- / Prüfungssprache"]])
            all_bsc_lectures.extend(modul_lectures)
    return pd.DataFrame(all_bsc_lectures, columns=header)

def return_all_msc_lectures():
    header = ['Titel', 'Code', 'Modul', 'Typ', 'SWS', 'CP', 'Modulbeauftragte*r', 'Studiennachweise', 'Lehr-/Lernform', 'Modulabschlussprüfung', 'kumulative Modulabschlussprüfung', 'Sprache']
    all_module_names = list(st.session_state.all_modules.keys())
    all_msc_lectures = []
    for i in all_module_names:
        if st.session_state.all_modules[i]['Modul-Code'][0] == 'M':
            full_semester_table = st.session_state.msc_modules[i]['Semester-Tabelle']
            semester_table_titles = [k[0] for k in full_semester_table]
            items_to_remove = {"Auswahl aus", "Auswahl aus:", "Modulprüfung", "Modulprüfung:", "Summe", "Summe:"}
            semester_table = [item for item in semester_table_titles if item not in items_to_remove]
            modul_lectures = []
            for j in semester_table:
                modul_lectures.append([j, st.session_state.all_modules[i]['Modul-Code'], st.session_state.all_modules[i]['Modul-Name-de'], st.session_state.all_modules[i]['Modul-Typ'], st.session_state.all_modules[i]['Anzahl SWS'], st.session_state.all_modules[i]['Anzhal CP und Arbeitsaufwand'], st.session_state.all_modules[i]["Modulbeauftragte / Modulbeauftragter"], st.session_state.all_modules[i]["Studiennachweise/ ggf. als Prüfungsvorleistungen"]["Teilnahmenachweise"], st.session_state.all_modules[i]["Lehr- / Lernformen"], st.session_state.all_modules[i]["Modulprüfung"]["Modulabschlussprüfung bestehend aus"], st.session_state.all_modules[i]["Modulprüfung"]["kumulative Modulprüfung bestehend aus"], st.session_state.all_modules[i]["Unterrichts- / Prüfungssprache"]])
            all_msc_lectures.extend(modul_lectures)
    return pd.DataFrame(all_msc_lectures, columns=header)




# ['SWS', 'CP', 'Modulbeauftragte*r', 'Studiennachweise', 'Lehr-/Lernform', 'Modulabschlussprüfung', 'kumulative 'Modulabschlussprüfung', 'Sprache']

# 
