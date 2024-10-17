import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Google Generative AI API with the provided key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit app setup
st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
st.header("GeminiDecode: Multilanguage Document Extraction by Gemini Pro")
page_bg_color = """
<style>
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
        color: white;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);  # Make header transparent
    }
    [data-testid="stText"], [data-testid="stMarkdown"], h1, h2, h3, h4, h5, h6, p, label {
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;  /* Optional: Style buttons if you want */
        color: white;
    }
</style>
"""
# Apply background color
st.markdown(page_bg_color, unsafe_allow_html=True)

# Description text with custom style
text = """
<p style='text-align: justify; font-family: serif;'>
    Utilizing <strong>Gemini Pro AI</strong>, this project effortlessly extracts vital information from diverse multilingual 
    documents, transcending language barriers with precision and efficiency for enhanced productivity and decision-making.
    Gemini Pro delivers unparalleled accuracy, speed, and clarity.
</p>

<p style='text-align: justify; font-family: serif;'>
    With <strong>Gemini Pro’s state-of-the-art AI</strong>, you can unlock valuable insights from any text, regardless of the 
    language or format, allowing you to focus on what truly matters—delivering results and achieving excellence.
</p>
"""

# Apply styled text
st.markdown(text, unsafe_allow_html=True)

# Function to interact with Gemini AI
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure this is the correct usage
    # Modify the content generation to suit your needs, based on the model's requirements
    response = model.generate_content([input_text, image, prompt])
    return response.text

# Image file uploader
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

# Display uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Load the image as PIL.Image.Image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Custom question input
    custom_question = st.text_input("Ask a question about the document:")

# Button for triggering document analysis
submit = st.button("Get Document Information")

# Input prompt for Gemini AI
input_prompt = """
You are an expert in understanding images.
We will upload an image, and you will have to answer any questions based on the uploaded image.
"""

# Handle the form submission
if submit and uploaded_file is not None and custom_question:
    # Pass the image directly (as a PIL.Image.Image object) to the API
    full_prompt = input_prompt + f"\nQuestion: {custom_question}"
    response = get_gemini_response(full_prompt, image, uploaded_file.name)
    st.subheader("The response is:")
    st.write(response)
else:
    if submit and not custom_question:
        st.error("Please enter a question before submitting.")




