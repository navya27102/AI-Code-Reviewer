import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables from the .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    raise ValueError("API key is not set in environment variables.")

# Set up Gemini client with the API key
client = genai.Client(api_key=api_key)

# Function to analyze Python code using Gemini
def analyze_code_with_gemini(code: str):
    try:
        # Send the code to Gemini for review
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Choose the appropriate model
            contents=f"Review the following Python code and suggest fixes if necessary:\n\n{code}"
        )

        feedback = response.text  # Extract feedback
        # Assuming the feedback contains suggestions and fixes
        return feedback.strip()
    
    except Exception as e:
        return f"Error during Gemini API call: {str(e)}"

# Streamlit UI setup
st.title("AI Code Reviewer")
st.subheader("Submit your Python code below for review:")

user_code = st.text_area("Enter your Python code here...", height=300)

if st.button("Review Code"):
    if user_code:
        st.write("Analyzing your code...")

        feedback = analyze_code_with_gemini(user_code)

        st.subheader("Feedback:")
        st.write(feedback)

    else:
        st.error("Please enter some Python code.")
