import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Portfolio Data Analyst",
    page_icon="📊",
    layout="wide"
)

# CSS Kustom
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Data Contoh (Ganti dengan data Anda)
projects = [
    {
        "title": "Analisis Market E-Commerce",
        "desc": "Analisis perilaku konsumen menggunakan clustering",
        "skills": ["Python", "Pandas", "Scikit-learn"],
        "img": "images/ecommerce.jpg"
    },
    {
        "title": "Dashboard KPI Perusahaan",
        "desc": "Visualisasi indikator kinerja utama",
        "skills": ["Power BI", "SQL", "DAX"],
        "img": "images/dashboard.jpg"
    }
]

# Sidebar
with st.sidebar:
    st.title("Portfolio Data")
    st.image("images/profile.jpg", width=150)
    st.markdown("""
    **Nama Anda**  
    Data Analyst | AI Enthusiast  
    [LinkedIn](#) | [GitHub](#)
    """)
    
    menu = st.radio(
        "Menu Utama",
        ["Beranda", "Proyek", "Visualisasi", "Kontak"],
        index=0
    )

# Halaman Beranda
if menu == "Beranda":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/profile.jpg", width=250)
    
    with col2:
        st.title("Halo, Saya [Nama Anda]")
        st.markdown("""
        ### Data Analyst & Visualization Specialist
        
        Saya memiliki pengalaman dalam:
        - Analisis data bisnis
        - Visualisasi data interaktif
        - Predictive modeling
        - Pembuatan dashboard
        """)
    
    st.divider()
    
    # Skills
    st.header("🛠️ Kemampuan Teknis")
    cols = st.columns(4)
    with cols[0]:
        st.markdown("**Bahasa Pemrograman**")
        st.write("- Python")
        st.write("- R")
        st.write("- SQL")
    
    with cols[1]:
        st.markdown("**Visualisasi Data**")
        st.write("- Matplotlib")
        st.write("- Plotly")
        st.write("- Power BI")
    
    with cols[2]:
        st.markdown("**Machine Learning**")
        st.write("- Scikit-learn")
        st.write("- TensorFlow")
    
    with cols[3]:
        st.markdown("**Tools**")
        st.write("- Git")
        st.write("- Docker")

# Halaman Proyek
elif menu == "Proyek":
    st.title("📂 Portfolio Proyek")
    
    for project in projects:
        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(project["img"], use_column_width=True)
            
            with col2:
                st.subheader(project["title"])
                st.write(project["desc"])
                
                # Skills badges
                for skill in project["skills"]:
                    st.markdown(f"`{skill}`", unsafe_allow_html=True)
                
                # Tombol aksi
                if st.button(f"Lihat Detail {project['title']}"):
                    st.session_state.project = project["title"]
            
            st.divider()

# Halaman Visualisasi
elif menu == "Visualisasi":
    st.title("📊 Demo Visualisasi")
    
    # Contoh visualisasi interaktif
    st.header("Contoh Visualisasi Data")
    
    data = pd.DataFrame({
        'Tahun': [2019, 2020, 2021, 2022, 2023],
        'Pendapatan': [45000, 48000, 51000, 55000, 62000],
        'Pengeluaran': [38000, 40000, 42000, 45000, 48000]
    })
    
    tab1, tab2 = st.tabs(["Garis", "Batang"])
    
    with tab1:
        fig = px.line(data, x='Tahun', y=['Pendapatan', 'Pengeluaran'],
                     title='Trend Pendapatan vs Pengeluaran')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.bar(data, x='Tahun', y=['Pendapatan', 'Pengeluaran'],
                    barmode='group', title='Perbandingan Tahunan')
        st.plotly_chart(fig, use_container_width=True)

# Halaman Kontak
elif menu == "Kontak":
    st.title("📨 Hubungi Saya")
    
    with st.form("contact_form"):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        
        submitted = st.form_submit_button("Kirim Pesan")
        if submitted:
            st.success(f"Terima kasih {name}! Pesan Anda telah dikirim.")
