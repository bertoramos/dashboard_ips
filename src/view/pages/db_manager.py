
import logging
from pathlib import Path
import streamlit as st
import pandas as pd

def list_files():
    project_dir = Path(__file__).parent.parent.parent.parent
    data_dir = project_dir / Path("data/uploaded_files")

    if not data_dir.exists():
        logging.warning(f"Data directory does not exist: {data_dir}")
        return []

    files = list(data_dir.glob("*.csv"))
    logging.info(f"Found {len(files)} files in {data_dir}")
    return files

def load_file(uploaded_file):
    project_dir = Path(__file__).parent.parent.parent.parent

    output_path = project_dir / Path("data/uploaded_files") / uploaded_file.name

    pd.read_csv(uploaded_file).to_csv(output_path, index=False)
    
    logging.info(f"File saved to: {output_path}")

def load_file_handler(uploaded_file):

    if uploaded_file is not None:
        filename = uploaded_file.name

        if Path(filename).suffix in [".csv"]:
            load_file(uploaded_file)
            st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        else:
            st.error("Unsupported file type. Please upload a CSV file.")
    else:
        st.warning("No file uploaded. Please choose a file to upload.")


def render():
    st.header("Database")

    with st.container():
        st.markdown(
            """
            <style>
            .db-upload-row .stButton > button {
                margin-top: 1.65rem;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("Choose a file")
        
        col_left, col_right = st.columns([3, 1])
        with col_left:
            uploaded_file = st.file_uploader(
                "Choose a file to load",
                label_visibility="collapsed",
                accept_multiple_files=False, type="csv")
        
        with col_right:
            st.markdown("<div class='db-upload-row'>", unsafe_allow_html=True)
            if st.button("Upload", width='stretch'):
                load_file_handler(uploaded_file)
            st.markdown("</div>", unsafe_allow_html=True)
        
        option = st.selectbox("Select a file to view", options=[f.name for f in list_files()])
        if option:
            selected_file = next((f for f in list_files() if f.name == option), None)
            if selected_file:
                df = pd.read_csv(selected_file)
                st.dataframe(df)
