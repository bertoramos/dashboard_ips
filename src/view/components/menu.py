
import streamlit as st

def menu(pages):
    
    if not pages:
        return None

    with st.sidebar:
        selected = st.navigation(pages)

    return selected
