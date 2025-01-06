import streamlit as st

# Title
st.title("Feedback Form")
st.markdown(''':red[Ist bislang nur ein dummy, d.h., im Moment kommmt das noch nicht bei mir an!]''')

# Collect feedback
with st.form("feedback_form"):
    name = st.text_input("Name (optional):")
    email = st.text_input("Email (optional):")
    feedback = st.text_area("Your Feedback:")
    rating = st.slider("Rate your experience (1 - Poor, 5 - Excellent):", 1, 5, 3)
    
    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        if feedback.strip():
            st.success("Thank you for your feedback!")
            st.write("Here's what you submitted:")
            st.write(f"Name: {name if name else 'N/A'}")
            st.write(f"Email: {email if email else 'N/A'}")
            st.write(f"Feedback: {feedback}")
            st.write(f"Rating: {rating}/5")
        else:
            st.error("Feedback cannot be empty. Please provide your feedback.")

# Additional note
st.info("Your feedback helps us improve our application. Thank you!")

