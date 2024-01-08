import streamlit as st
import os
import json

folder_path = '/path/to/your/json/files'
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

data = {}  # Dictionary to store loaded JSON data

for json_file in json_files:
    with open(os.path.join(folder_path, json_file), 'r') as file:
        data[json_file] = json.load(file)
