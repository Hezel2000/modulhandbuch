import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

st.logo('images/Goethe-Logo.jpg')
st.sidebar.image('images/Goethe-Logo.jpg')

# Function to connect to Google Sheet
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["google"]["credentials"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Feedback Modulhandbuch").sheet1  # Replace with your exact sheet name
    return sheet


st.subheader("Feedback")

with st.form("feedback_form"):
    name = st.text_input("Name (optional):")
    email = st.text_input("Email (optional):")
    feedback = st.text_area("Feedback:")
    st.write(':grey[Bewerte das online Modulhandbuch (optional)]')
    rating = st.feedback(options="stars")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if feedback.strip():
            try:
                # Connect to Google Sheet
                sheet = connect_to_gsheet()
                if rating is None:
                    sheet.append_row([name, email, feedback, rating])
                else:
                    sheet.append_row([name, email, feedback, rating+1])
                
                st.success("Danke für Dein Feedback! Deine Nachricht wurde gespeichert.")
            except Exception as e:
                st.error(f"Failed to save feedback. Error: {e}")
        else:
            st.error("Das Feedback-Feld muss ausgefüllt sein.")
