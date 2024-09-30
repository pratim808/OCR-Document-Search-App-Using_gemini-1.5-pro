import google.generativeai as genai
from PIL import Image
import streamlit as st
import io

from ocr_utils import extract_text
from ocr_utils import highlight_content

# Streamlit app layout
st.title("OCR Text Extraction from Images")

# File uploader widget
uploaded_file = st.file_uploader(
    "Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open and display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Extract text from the image
    full_text = extract_text(image)

    # Display the extracted text
    st.subheader("Extracted Text")
    st.write(full_text)

    # Text input for keyword search
    keyword = st.text_input("Enter Keyword to Search")
    # Display highlighted content if a keyword is entered
    if keyword:

        highlighted_content = highlight_content(full_text, keyword)
        st.subheader("Highlighted Search Results")

      # CSS styles for highlighting
        st.markdown('''
        <style>
        .highlight {
            background-color: yellow;
            color: black;
            padding: 0.2em;
            border-radius: 4px;
        }
        <style>
        ''', unsafe_allow_html=True)

        # Render the highlighted content with HTML
        st.markdown(highlighted_content, unsafe_allow_html=True)

    else:
        st.subheader("Highlighted Search Results")
        st.write("No keyword entered for highlighting.")
