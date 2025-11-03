import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import requests

# ===========================
# 🚨 Konfigurasi Halaman
# ===========================
st.set_page_config(
    page_title="Portfolio Data Science",
    page_icon="📊",
    layout="wide"
)

# ===========================
# CSS Kustom
# ===========================
st.markdown('''
<style>
/* Sidebar */
.sidebar-title { font-size:24px; font-weight:bold; color:#4B8BBE; margin-bottom:10px; }
.sidebar-box { background-color:#f0f2f6; padding:15px; border-radius:10px; border:1px solid #ccc; }

/* Main Title & Subtitle */
.main-title { font-size:48px; font-weight:bold; color:#2C3E50; text-align:center; margin-bottom:30px; }
.subtitle { font-size:24px; color:#7F8C8D; text-align:center; margin-bottom:50px; }

/* Card */
.card { background-color:#F9F9F9; padding:20px; border-radius:10px; box-shadow:2px 2px 12px rgba(0,0,0,0.1); margin-bottom:20px; }
</style>
''', unsafe_allow_html=True)

# ===========================
# Sidebar
# ===========================
st.sidebar.markdown('<div class="sidebar-title">Navigasi</div>', unsafe_allow_html=True)
with st.sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    menu = st.radio("", ["🏠 Home", "📂 Projects", "📰 Blog", "📞 Contact"])
    st.markdown('</div>', unsafe_allow_html=True)

# ===========================
# Halaman Home
# ===========================
if menu == "🏠 Home":
    st.markdown("<div class='main-title'>👨‍💻 Data Science Portfolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Explore our projects and latest insights in Data Science and AI</div>", unsafe_allow_html=True)

    st.subheader("Selamat datang di DGrafika!")
    st.markdown('''
<div style='text-align: justify; background-color: #ffffff; padding: 25px; border-radius: 10px;
            border: 1px solid #ddd; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-bottom:20px;
            font-size:18px; line-height:1.6;'>
  <h3 style='text-align:center; color:#4B8BBE;'>About Us</h3>
  <p style='text-align:justify; font-size:18px; line-height:1.7;'>
      🚀 <strong>Startup kami bergerak dalam bidang Data
