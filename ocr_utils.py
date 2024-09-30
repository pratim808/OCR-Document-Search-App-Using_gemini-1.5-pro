import google.generativeai as genai
from PIL import Image
import streamlit as st
import io


GOOGLE_API_KEY = "Use_Your_Own_Api_Key"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")


def extract_text(image):
    # Ensure the image is in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Call the model's generate_content method with the PIL image
    response = model.generate_content(
        ["successfully extracts hindi and english text from the image and returns the extracted text in a structured format (plain text)", image]
    )

    return response.text


def highlight_content(full_text, keyword):
    if keyword:
        # Highlight the keyword in the text
        highlighted_text = full_text.replace(
            keyword, f"<span class='highlight'>{keyword}</span>"
        )

        return highlighted_text
    else:
        return "No keyword entered for highlighting."
