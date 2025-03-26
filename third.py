import streamlit as st
import pandas as pd

# Page title
st.title("📋 Feedback Form")

# User input fields
name = st.text_input("Your Name", placeholder="Enter your name")

rating = st.slider("Rate your experience (1-5)", 1, 5, 3)

feedback = st.text_area("Your Feedback", placeholder="Share your thoughts...")

# Submit button
if st.button("Submit Feedback"):
    if name and feedback:
        # Save feedback (optional: store in a CSV)
        data = {"Name": [name], "Rating": [rating], "Feedback": [feedback]}
        df = pd.DataFrame(data)
        df.to_csv("feedback.csv", mode="a", header=False, index=False)
        
        st.success("✅ Thank you for your feedback!")
    else:
