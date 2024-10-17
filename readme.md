# GeminiDecode: Multilanguage Document Extraction by Gemini Pro

GeminiDecode: Multilanguage Document Extraction by Gemini Pro is a cutting-edge solution designed to extract and process data from documents in multiple languages with unparalleled efficiency. By leveraging advanced natural language processing (NLP) and machine learning algorithms, it seamlessly identifies, extracts, and categorizes information from diverse document formats, ensuring accuracy and speed. Ideal for global businesses, GeminiDecode supports over 50 languages, providing robust data extraction capabilities that streamline workflows, enhance productivity, and improve decision-making processes.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/GeminiDecode.git
    cd GeminiDecode
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv .venv
    On Windows: .venv\Scripts\activate #On linux:source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Google API Key:**
    - Create a `.env` file in the root directory.
    - Add your API key to the `.env` file:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Features
- **Multilanguage Support:** Extracts data from documents in over 50 languages.
- **Advanced NLP and ML:** Utilizes cutting-edge natural language processing and machine learning algorithms.
- **Efficiency and Accuracy:** Ensures high accuracy and speed in data extraction and processing.
- **Versatile Document Formats:** Supports diverse document formats.

## Project Flow

1. **User Interaction:** User interacts with the UI to enter the input.
2. **Data Transmission:** User input is collected from the UI and transmitted to the backend using the Google API key.
3. **Model Processing:** The input is forwarded to the Gemini Pro pre-trained model via an API call.
4. **Result Generation:** The Gemini Pro pre-trained model processes the input and generates the output.
5. **Output Display:** The results are returned to the frontend for formatting and display.

![Screenshot 2024-10-17 125126](https://github.com/user-attachments/assets/0ef988c4-0606-4be2-ac9a-7339aabd3d12)

## Requirements Specification

### Steps to Complete the Project

1. **Requirements Specification**

   Create a `requirements.txt` file to list the required libraries.Install the required libraries.
   Specifying the required libraries making it easier for others to replicate the development environment.

    - Streamlit:  Streamlit is a powerful framework for building interactive web applications with Python.
    - Streamlit_extras:  Additional utilities and enhancements for Streamlit applications.
    - Google-generativeai:  Python client library for accessing the GenerativeAI API, facilitating interactions with pre-trained language models like Gemini Pro.
    - Python-dotenv:  Python-dotenv allows you to manage environment variables stored in a .env file for your Python projects.
    - PyPDF2:  It is a Python library for extracting text and manipulating PDF documents.
    - Pillow:  Pillow is a Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats.
    - LangChain: Provides tools and abstractions to improve the customization, accuracy, and relevancy of the information the models generate
 

3. **Initialization of Google API Key**
    - Generate Google API Key.
    - Initialize Google API Key.

4. **Interfacing with Pre-trained Model**
    - Load the Gemini Pro pre-trained model.
    - Implement a function to get Gemini response.
    - Implement a function to read PDF content.
    - Write a prompt for Gemini model.

5. **Model Deployment**
    - Integrate with Web Framework.
    - Host the Application.

## Prior Knowledge Required

- **Google Profile:** https://www.cloudskillsboost.google/public_profiles/6aa8a062-b154-4515-975a-a810500ef3bb

Its benificial to have prior knowledge of the following topics to complete this project:

- **Generative AI Concepts**
    - [NLP](https://www.tutorialspoint.com/natural_language_processing/index.htm)
    - [Generative AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence)
    - [Gemini API](https://ai.google.dev/gemini-api/docs/get-started/python)
    - [Streamlit](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)
