import streamlit as st
from model.bert_model import classify_text
from model.gpt_response import generate_response
from utils.text_preprocessing import preprocess_text

st.set_page_config(page_title="Cyberbullying Detector", layout="wide")

st.markdown("""
    <style>
        .main {
            background-image: url('https://images.unsplash.com/photo-1605792657660-596af9009e82');
            background-size: cover;
            padding: 2rem;
            color: white;
        }
        .stTextArea textarea {
            background-color: #ffffff20;
            color: white;
        }
        .stButton>button {
            background-color: #6c5ce7;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Real-Time Cyberbullying Detector & Rewriter using Generative AI")

text_input = st.text_area("📩 Paste a comment or message to analyze:", height=150)

if st.button("🔍 Detect & Rephrase"):
    if text_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        processed = preprocess_text(text_input)
        label, score = classify_text(processed)

        st.subheader("🔎 Classification Result:")
        st.write(f"**Detected as:** {'Toxic ❌' if label == 1 else 'Non-Toxic ✅'}")
        st.write(f"**Confidence:** {score*100:.2f}%")

        if label == 1:
            st.subheader("✨ Rephrased Comment (Safe Version):")
            response = generate_response(text_input)
            st.success(response)
        else:
            st.info("This comment is clean. No action needed. 🎉")
