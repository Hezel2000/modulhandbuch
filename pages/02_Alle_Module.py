import streamlit as st
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


st.subheader('Alle Module')

tab1, tab2 = st.tabs(['BSc', 'MSc'])

with tab1:
    # utils.results_modules(utils.sort_BSc_modules(data), 'alle_module_bsc')
    utils.results_modules(utils.sort_modules(st.session_state.bsc_modules), 'alle_module_bsc')

with tab2:
    # utils.results_modules(utils.sort_MSc_modules(data), 'alle_module_msc')
    utils.results_modules(utils.sort_modules(st.session_state.msc_modules), 'alle_module_bsc')
