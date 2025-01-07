import streamlit as st
import re
import pandas as pd

# Darstellung der Module
def results_modules(volltext_results):
    results = volltext_results
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
                        
            df = pd.DataFrame(module_content['Semester-Tabelle'])

            df.columns = df.iloc[0]  # Set the first row as column headers
            df = df[1:]  # Remove the first row from the data

            # Reset the index for a cleaner display
            df = df.reset_index(drop=True)

            # Display the DataFrame in Streamlit
            st.dataframe(df)


            
            st.divider()
            st.header('Bemerkungen')

            st.write(f'{module_content["Bemerkungen"]}')
            
            st.divider()
            col1, col2 = st.columns([30,70])
            with col1:
                sel_version = st.selectbox('Version', module_content['Version'], key=module_name)
            with col2:
                st.write(f'{module_content["Änderung"][sel_version]}')


def sort_BSc_modules(data):
    # Helper function to split the alphabetic and numeric parts
    def split_alpha_numeric(s):
        match = re.match(r'([^\d]*)(\d*)', s)
        alpha = match.group(1)  # Alphabetic part
        num = int(match.group(2)) if match.group(2) else float('inf')  # Numeric part or high number
        return alpha, num

    # Filter and sort based on 'Modul-Code'
    sorted_items = sorted(
        (item for item in data.items() if item[1]['Modul-Code'].startswith('B')),
        key=lambda x: split_alpha_numeric(x[1]['Modul-Code'])
    )

    # Convert back to a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict



def sort_MSc_modules(data):
    # Helper function to split the alphabetic and numeric parts
    def split_alpha_numeric(s):
        match = re.match(r'([^\d]*)(\d*)', s)
        alpha = match.group(1)  # Alphabetic part
        num = int(match.group(2)) if match.group(2) else float('inf')  # Numeric part or high number
        return alpha, num

    # Filter and sort based on 'Modul-Code'
    sorted_items = sorted(
        (item for item in data.items() if item[1]['Modul-Code'].startswith('M')),
        key=lambda x: split_alpha_numeric(x[1]['Modul-Code'])
    )

    # Convert back to a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict




