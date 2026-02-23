import streamlit as st
import pandas as pd

# 1. Configuración de la página (DEBE IR PRIMERO)
st.set_page_config(page_title="Gestión Contable Pro", layout="wide")

# 2. Estilo CSS para el Azul Marino
st.markdown("""
    <style>
    .stApp {
        background-color: #001f3f;
    }
    h1, h2, h3, p, span, label, .stMetric {
        color: white !important;
    }
    [data-testid="stSidebar"] {
        background-color: #003366;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Título y Contenido
st.title("📊 Tablero de Gestión")

with st.sidebar:
    st.header("Ajustes")
    v_enero = st.number_input("Venta Enero", value=5000.0)
    crecimiento = st.number_input("Crecimiento", value=200.0)

# 4. Lógica de cálculos
v_feb = v_enero + crecimiento
v_mar = v_feb + crecimiento
v_abr = v_mar + crecimiento

# 5. Mostrar resultados
col1, col2 = st.columns(2)
col1.metric("Venta proyectada Abril", f"${v_abr:,.2f}")

st.subheader("📈 Gráfico de Evolución")
df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [v_enero, v_feb, v_mar, v_abr]
})
st.bar_chart(df.set_index("Mes"))
