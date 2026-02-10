
import streamlit as st
from pathlib import Path

def render():
    basedir = Path(__file__).parent.parent

    st.markdown("""
<div style='background:#f7fafc;padding:2.5rem 2rem 1.5rem 2rem;border-radius:18px;margin-bottom:2rem;border:1.5px solid #d1d5db;'>
    <h1 style='color:#22223b;margin-bottom:0.5em;'>IPS Dashboard</h1>
    <h3 style='color:#22223b;margin-top:0;'>Visualize and analyze indoor positioning data in seconds</h3>
    <p style='font-size:1.1rem;color:#22223b;margin-top:1.5em;'>
        <b>Quick steps:</b>
        <ol style='margin-top:0.5em;margin-bottom:0.5em;color:#22223b;'>
            <li><b>Choose a dataset</b> in the Dashboard</li>
            <li><b>Filter</b> by Channel, Mac, Protocol, and Time (if available)</li>
            <li><b>See the heatmap</b> and measurement points over your background image</li>
            <li><b>Switch pages</b> from the sidebar for more features</li>
        </ol>
    </p>
</div>
        """, unsafe_allow_html=True)

    st.markdown("""
<div style='display:flex;gap:2rem;flex-wrap:wrap;margin-bottom:2rem;'>
    <div style='flex:1;min-width:260px;background:#f8f9fa;padding:1.2rem 1rem 1rem 1rem;border-radius:12px;border-left:6px solid #495057;'>
        <b style='color:#22223b;'>Load & Explore</b><br>
        <span style='color:#22223b;'>Select a dataset, see stats and preview the data table instantly.</span>
    </div>
    <div style='flex:1;min-width:260px;background:#f1f3f5;padding:1.2rem 1rem 1rem 1rem;border-radius:12px;border-left:6px solid #364fc7;'>
        <b style='color:#22223b;'>Heatmap Visualization</b><br>
        <span style='color:#22223b;'>Filter by channel, protocol, Mac, and time. Visualize RSSI as a heatmap over your own background image.</span>
    </div>
    <div style='flex:1;min-width:260px;background:#f8f9fa;padding:1.2rem 1rem 1rem 1rem;border-radius:12px;border-left:6px solid #adb5bd;'>
        <b style='color:#22223b;'>Database Management</b><br>
        <span style='color:#22223b;'>Upload new files and manage datasets from the Database section.</span>
    </div>
</div>
        """, unsafe_allow_html=True)

    st.markdown("""
<div style='background:#f1f3f5;padding:1.2rem 1rem 1.5rem 1rem;border-radius:12px;margin-bottom:2rem;'>
    <b style='color:#22223b;'>What is this for?</b><br>
    <span style='color:#22223b;'>
        This tool makes it easy and interactive to analyze indoor localization experiments visually and statistically. Ideal for researchers and engineers working with IPS data.
    </span>
</div>
        """, unsafe_allow_html=True)

    # Example image (replace with your own if available)
    st.markdown("<div style='text-align:center;margin-bottom:1.5rem;'><b style='color:#22223b;'>Example Heatmap Output</b></div>", unsafe_allow_html=True)
    st.image(basedir / Path("assets/heatmap/heatmap_example.png"), width='stretch', caption="Sample heatmap visualization (replace with your own experiment image)")
    
