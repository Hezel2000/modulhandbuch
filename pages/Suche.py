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

# Streamlit app
st.sidebar.header("Volltextsuche")
search_query = st.sidebar.text_input("Sucheingabe", placeholder='Sucheingabe', label_visibility='collapsed')

if search_query:
    results = search_json_files(data, search_query)
    st.write("Suchergebnisse:")
    for file_name, json_data in results.items():
        st.write(f"Module: {file_name}")
else:
    st.write("Enter a search query in the sidebar.")
