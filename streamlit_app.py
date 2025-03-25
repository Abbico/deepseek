
import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="DAJANIII Pro", layout="wide", page_icon="🧠")

# Load API key safely
api_key = st.secrets["openrouter"]["api_key"]

# Sidebar Navigation
st.sidebar.title("📂 Navigation")
menu = st.sidebar.radio("Go to", ["📊 Portfolio", "📈 Charts", "💬 Chat", "🔍 Stock Lookup"])

# Check logo path
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=200)
else:
    st.sidebar.warning("Logo not found.")

st.title("🧠 DAJANIII Pro - AI Portfolio Assistant")

# Simple check to confirm no white screen
st.success("App loaded successfully!")

# Test each menu for basic loading
if menu == "📊 Portfolio":
    st.subheader("Portfolio Page Loaded ✅")
elif menu == "📈 Charts":
    st.subheader("Charts Page Loaded ✅")
elif menu == "💬 Chat":
    st.subheader("Chat Page Loaded ✅")
elif menu == "🔍 Stock Lookup":
    st.subheader("Stock Lookup Page Loaded ✅")
