import streamlit as st
import numpy as np

st.set_page_config(page_title="Kalkulator Dot Product", layout="centered")

st.title("🧮 Kalkulator Vektor: Dot Product")
st.markdown("Masukkan dua vektor 3 dimensi untuk menghitung **Dot Product**.")

with st.form("vector_form"):
    st.subheader("Vektor Pertama (v₁)")
    v1_x = st.number_input("v₁ x", value=0.0, key="v1x")
    v1_y = st.number_input("v₁ y", value=0.0, key="v1y")
    v1_z = st.number_input("v₁ z", value=0.0, key="v1z")

    st.subheader("Vektor Kedua (v₂)")
    v2_x = st.number_input("v₂ x", value=0.0, key="v2x")
    v2_y = st.number_input("v₂ y", value=0.0, key="v2y")
    v2_z = st.number_input("v₂ z", value=0.0, key="v2z")

    submitted = st.form_submit_button("Hitung Dot Product")

if submitted:
    v1 = np.array([v1_x, v1_y, v1_z])
    v2 = np.array([v2_x, v2_y, v2_z])
    dot = np.dot(v1, v2)

    st.success("Hasil Perhitungan:")
    st.write(f"🔹 **Dot Product (v₁ • v₂):** `{dot}`")
