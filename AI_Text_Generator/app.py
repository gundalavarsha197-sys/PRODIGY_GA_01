import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(page_title="AI Smart Text Generator", page_icon="🧠")

# Title
st.title("🧠 AI Smart Text Generator")
st.write("Generate intelligent text using AI ✨")

# Sidebar settings
st.sidebar.header("Settings")
max_len = st.sidebar.slider("Max Length", 20, 200, 50)
num_seq = st.sidebar.slider("Number of Results", 1, 5, 1)

# User input
prompt = st.text_area("Enter your prompt:")

# Load model (cached for speed)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# Generate button
if st.button("Generate 🚀"):
    if prompt.strip() != "":
        with st.spinner("Generating text... ⏳"):
            results = generator(prompt, max_length=max_len, num_return_sequences=num_seq)

        for i, res in enumerate(results):
            st.subheader(f"Result {i+1}")
            st.write(res['generated_text'])

            # Download option
            st.download_button(
                label="Download",
                data=res['generated_text'],
                file_name=f"result_{i+1}.txt"
            )
    else:
        st.warning("Please enter a prompt!")