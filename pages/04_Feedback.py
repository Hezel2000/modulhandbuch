import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

# Google Sheets setup
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["google"]["credentials"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Feedback Form").sheet1  # Replace with your Google Sheet name
    return sheet

# Streamlit feedback form
st.title("Feedback Form")

with st.form("feedback_form"):
    name = st.text_input("Name (optional):")
    email = st.text_input("Email (optional):")
    feedback = st.text_area("Your Feedback:")
    rating = st.slider("Rate your experience (1 - Poor, 5 - Excellent):", 1, 5, 3)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if feedback.strip():
            try:
                # Connect to Google Sheets
                sheet = connect_to_gsheet()
                
                # Append feedback to the sheet
                sheet.append_row([name, email, feedback, rating])
                
                st.success("Thank you for your feedback! Your message has been saved.")
            except Exception as e:
                st.error(f"Failed to save feedback. Error: {e}")

        else:
            st.error("Feedback cannot be empty. Please provide your feedback.")
