import streamlit as st
import os
import base64

def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True) 

