import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

# Function to connect to Google Sheet
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["google"]["credentials"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Feedback Modulhandbuch").sheet1  # Replace with your exact sheet name
    return sheet

# Streamlit feedback form
st.title("Feedback Form")

with st.form("feedback_form"):
    name = st.text_input("Name (optional):")
    email = st.text_input("Email (optional):")
    feedback = st.text_area("Dein Feedback:")
    st.write(':grey[Bewerte das online Modulhandbuch]')
    rating = st.feedback(options="stars", value=3) #st.slider("Rate your experience (1 - Poor, 5 - Excellent):", 1, 5, 3)
    submitted = st.form_submit_button("Submit")

    if submitted:
        if feedback.strip():
            try:
                # Connect to Google Sheet
                sheet = connect_to_gsheet()
                
                # Append feedback to the sheet
                sheet.append_row([name, email, feedback, rating+1])
                
                st.success("Thank you for your feedback! Your message has been saved.")
            except Exception as e:
                st.error(f"Failed to save feedback. Error: {e}")
        else:
            st.error("Feedback cannot be empty. Please provide your feedback.")


st.sidebar.image('images/Goethe-Logo.jpg')