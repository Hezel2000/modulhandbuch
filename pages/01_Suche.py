import streamlit as st
import os
import json
import re
import utils

st.logo('images/Goethe-Logo.jpg')
st.sidebar.image('images/Goethe-Logo.jpg')

# folder_path = 'Module als json'
# json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# data = {}  # Dictionary to store loaded JSON data

# for json_file in json_files:
#     with open(os.path.join(folder_path, json_file), 'r') as file:
#         data[json_file] = json.load(file)

st.session_state.all_modules, st.session_state.all_module_names, st.session_state.bsc_modules, st.session_state.msc_modules = utils.initialise_all_modules()

# Volltextsuche
def search_all(data, search_query):
    results = {}

    for file_name, json_data in data.items():
        # Implement your search logic here
        if search_query in json.dumps(json_data):
            results[file_name] = json_data

    return results


# Suche nach Modulbeauftragte / Modulbeauftragter
def get_unique_modulbeauftragte(data):
    names = {
        module.get("Modulbeauftragte / Modulbeauftragter")
        for module in data.values()
        if "Modulbeauftragte / Modulbeauftragter" in module
    }
    return sorted(names, key=lambda x: x.split()[-1] if x else "")

def filter_data_by_modulbeauftragte(data, selected_name):
    return {
        filename: module
        for filename, module in data.items()
        if module.get("Modulbeauftragte / Modulbeauftragter") == selected_name
    }


# Suche nach Modul CP
def get_unique_cp(data):
    cp_values = set()
    for module in data.values():
        cp_info = module.get("Anzhal CP und Arbeitsaufwand", "")
        match = re.search(r"(\d+)\s*CP", cp_info)
        if match:
            cp_values.add(match.group(1))  # Extract the CP number
    return sorted(cp_values, key=int)

# Filter data by selected CP value
def filter_data_by_cp(data, selected_cp):
    return {
        filename: module
        for filename, module in data.items()
        if re.search(fr"{selected_cp}\s*CP", module.get("Anzhal CP und Arbeitsaufwand", ""))
    }


# ---------------------------

st.subheader('Suche')
# select_BSc_MSc = st.radio('',('BSc', 'MSc', 'BSc & MSc'), horizontal=True, disabled=True)
tab1, tab2, tab3 = st.tabs(['Volltext', 'Modulbeauftragte', 'Modul CP'])

with tab1:
    st.write('''Groß-/Kleinschreibung beachten.  
             Derzeit gibt es noch ein Problem mit Umlauten. Also eher "mpker", statt "Rümpker" schreiben.  
             Es kann nach allem gesucht werden, also: *BP*, *BP2*, *Voigt*, *3 CP*, *Praktikum*, *Seminar*, usw.''')
    search_query = st.text_input("Sucheingabe", placeholder='Sucheingabe', label_visibility='collapsed')

    if search_query:
        volltext_results = search_all(st.session_state.all_modules, search_query)
        utils.results_modules(utils.sort_modules(volltext_results), 'suche_volltext')

with tab2:
    unique_modulbeauftragte = get_unique_modulbeauftragte(st.session_state.all_modules)
    selected_name = st.selectbox("", unique_modulbeauftragte, label_visibility="collapsed")

    if selected_name:
        modulbeauftragte = filter_data_by_modulbeauftragte(st.session_state.all_modules, selected_name)
        utils.results_modules(utils.sort_modules(modulbeauftragte), 'suche_modulbeauftragte')

with tab3:
    unique_cp_values = get_unique_cp(st.session_state.all_modules)
    selected_cp = st.selectbox("", unique_cp_values, label_visibility="collapsed")

    # Show matching entries
    if selected_cp:
        modul_cp = filter_data_by_cp(st.session_state.all_modules, selected_cp)
        utils.results_modules(utils.sort_modules(modul_cp), 'suche_modul_cp')
