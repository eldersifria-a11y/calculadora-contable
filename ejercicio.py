import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Gestión Contable Pro", layout="wide")

# 2. CÓDIGO PARA EL COLOR AZUL MARINO
st.markdown(
    """
    <style>
    /* Cambia el fondo de la app principal */
    .stApp {
        background-color: #001f3f; /* Azul Marino */
    }
    
    /* Cambia el color de todos los textos a blanco para que resalten */
    h1, h2, h3, p, span, label {
        color: white !important;
    }

    /* Estilo opcional: hace que la barra lateral sea un poco más clara */
    [data-testid="stSidebar"] {
        background-color: #003366;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- De aquí en adelante seguís con tu código normal ---
st.title("📊 Mi Tablero de Gestión")

with st.sidebar:
    st.header("Configuración")
    v_enero = st.number_input("Venta Enero", value=5000.0)
    crecimiento = st.number_input("Crecimiento", value=200.0)

# (El resto de tus cálculos y gráficos...)
v_feb = v_enero + crecimiento
v_mar = v_feb + crecimiento
v_abr = v_mar + crecimiento

col1, col2 = st.columns(2)
col1.metric("Venta Abril", f"${v_abr:,.2f}")

st.subheader("📈 Evolución Mensual")
datos = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [v_enero, v_feb, v_mar, v_abr]
})
st.bar_chart(datos.set_index("Mes"))import streamlit as st
import pandas as pd

# Configuración básica
st.set_page_config(page_title="Calculadora Contable", layout="wide")

st.title("📊 Mi Tablero de Gestión")

# Entradas de datos en la barra lateral
with st.sidebar:
    st.header("Configuración")
    v_enero = st.number_input("Venta Enero", value=5000.0)
    crecimiento = st.number_input("Crecimiento", value=200.0)

# Cálculos
v_feb = v_enero + crecimiento
v_mar = v_feb + crecimiento
v_abr = v_mar + crecimiento

# Cálculo de saldos (Ejemplo contable)
saldo_mar = (v_mar * 0.60) + (v_feb * 0.30)
saldo_abr = (v_abr * 0.60) + (v_mar * 0.30)

# Mostrar Métricas en tarjetas
col1, col2 = st.columns(2)
col1.metric("Venta Abril", f"${v_abr:,.2f}")
col2.metric("Saldo Clientes Abril", f"${saldo_abr:,.2f}")

# Gráfico de barras simple
st.subheader("📈 Evolución Mensual")
datos = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [v_enero, v_feb, v_mar, v_abr]
})
st.bar_chart(datos.set_index("Mes"))

