import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Visualisasi Data dengan Chart Tipe Pilihan")

# Mengunggah dataset
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca dataset
    df = pd.read_csv(uploaded_file)
    
    # Menampilkan beberapa data awal
    st.write("Data yang diunggah:")
    st.write(df.head())

    # Pilihan kolom untuk X dan Y
    x_col = st.selectbox("Pilih kolom untuk X-axis", df.columns)
    y_col = st.selectbox("Pilih kolom untuk Y-axis", df.columns)

    # Pilihan tipe chart
    chart_type = st.selectbox(
        "Pilih tipe chart",
        ("Line Chart", "Bar Chart", "Area Chart")
    )

    # Menampilkan chart berdasarkan pilihan
    st.write(f"Tipe chart yang dipilih: {chart_type}")
    
    if chart_type == "Line Chart":
        st.line_chart(df[[x_col, y_col]].set_index(x_col))

    elif chart_type == "Bar Chart":
        st.bar_chart(df[[x_col, y_col]].set_index(x_col))

    elif chart_type == "Area Chart":
        st.area_chart(df[[x_col, y_col]].set_index(x_col))

else:
    st.write("Silakan unggah file CSV untuk melanjutkan.")
