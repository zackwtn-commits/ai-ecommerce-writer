import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="AI E-com Writer")
st.title("🛍️ AI Product Description Generator")

api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-2.0-flash')
    uploaded_file = st.file_uploader("Upload product photo...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        if st.button("Generate Description"):
            with st.spinner('Writing...'):
                prompt = "Write a catchy Amazon title and description for this item."
                response = model.generate_content([prompt, image])
                st.write(response.text)
else:
    st.info("Enter your free Google API Key in the sidebar to start.")
