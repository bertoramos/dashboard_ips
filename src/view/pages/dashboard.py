
import streamlit as st
from pathlib import Path
import pandas as pd

from view.components.heatmap import create_heatmap

from .db_manager import list_files

def select_dataset():
    selected_dataset = st.selectbox("Choose a dataset", options=[Path(f).name for f in list_files()])
    
    if selected_dataset:
        selected_file = next((f for f in list_files() if f.name == selected_dataset), None)
        if selected_file:
            df = pd.read_csv(selected_file)

            return df
    return None

def render():
    st.header("Dashboard")
    
    selected_df = select_dataset()
    background_image = st.file_uploader("Background image (PNG)", type=["png"])
    if selected_df is None:
        st.warning("Please select a dataset to view the dashboard.")
    else:
        tabs = st.tabs(["Summary", "Data Preview", "Heatmap"])
        with tabs[0]:
            st.subheader("Summary")
            st.write(selected_df.describe())
        
        with tabs[1]:
            st.subheader("Data Preview")
            st.dataframe(selected_df)
        
        with tabs[2]:
            col1, col2, col3 = st.columns(3)
            with col1:
                beacon_options = sorted(selected_df["beacon"].dropna().unique().tolist())
                beacon_default = "P2" if "P2" in beacon_options else (beacon_options[0] if beacon_options else None)
                selected_beacon = st.selectbox(
                    "Beacon",
                    beacon_options,
                    index=beacon_options.index(beacon_default) if beacon_default in beacon_options else 0,
                )

            with col2:
                channel_options = sorted(selected_df["channel"].dropna().unique().tolist())
                channel_default = 37 if 37 in channel_options else (channel_options[0] if channel_options else None)
                selected_channel = st.selectbox(
                    "Channel",
                    channel_options,
                    index=channel_options.index(channel_default) if channel_default in channel_options else 0,
                )

            with col3:
                protocol_options = sorted(selected_df["protocol"].dropna().unique().tolist())
                protocol_default = protocol_options[0] if protocol_options else None
                selected_protocol = st.selectbox(
                    "Protocol",
                    protocol_options,
                    index=protocol_options.index(protocol_default) if protocol_default in protocol_options else 0,
                )
            
            # select data
            df_filtered = selected_df[
                (selected_df["channel"] == selected_channel) &\
                (selected_df["beacon"] == selected_beacon) &\
                (selected_df["protocol"] == selected_protocol)
            ]

            # tomar la primera aparicion por coordenada (x, y)
            df_filtered = df_filtered.sort_index().drop_duplicates(subset=["x", "y"], keep="first")
            puntos = df_filtered[["x", "y", "rssi"]].values

            fig = create_heatmap(puntos, background_image=background_image)
            st.plotly_chart(fig, width='stretch')
            
