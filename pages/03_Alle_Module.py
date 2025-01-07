import streamlit as st
import os
import json
import utils

folder_path = 'Module als json'
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

data = {}  # Dictionary to store loaded JSON data

for json_file in json_files:
    with open(os.path.join(folder_path, json_file), 'r') as file:
        data[json_file] = json.load(file)


import streamlit as st

import streamlit as st

# Example dictionary with text values
example_dict = {
    "key1": "This is the first line.\nThis is the second line.",
    "key2": "Another text value.\nIt also has a line break.",
    "key3": "No line break here.",
    "Inhalte": "Das Modul umfasst die für die Studierenden grundlegende Haupteinführungsveranstaltung \"System Erde\" sowie 5 Tage Geländeübung.\nIn \"System Erde\" werden grundlegende geowissenschaftliche Konzepte einführend vorgestellt und die Verbindungen zwischen den Einzeldisziplinen betont. Die Studierenden lernen den Planeten Erde, seine Entwicklungsgeschichte, aber auch notwendige geowissenschaftliche Konzepte und Begriffe kennen. Durch einfache Übungen im Selbststudium können Studierende die Lerninhalte aktiv festigen, während ein Tutorium weitere Hilfestellung bietet.\nIn den 5 Geländetagen aus dem Angebot an geologischen Anfänger*innen-Geländeübungen lernen die Studierenden die Grundprinzipien der geowissenschaftlichen Geländearbeit kennen. Im Gelände werden so Prinzipien der Stratigraphie, der Gesteinserkennung und von 3D-Strukturen verknüpfend eingeführt.",
}

# Display each key and its value in an expander
for key, value in example_dict.items():
    with st.expander(key):  # Create an expander with the key as the title
        st.text(value)      # Display the value inside the expander

with st.expander(key):  # Create an expander with the key as the title
    st.text(example_dict['Inhalte'])      # Display the value inside the expander
        



st.title('Alle BSc Module')
utils.results_modules(utils.sort_modules(data))