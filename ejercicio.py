import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- CONFIGURACIÓN DE MARCA ---
NOMBRE_APP = "MonoTax"
ESLOGAN = "Sellar el trato nunca fue tan fácil."
# Imagen representativa (Monos dándose la mano)
LOGO_URL = "https://img.icons8.com/external-flat-icons-invisisteve/512/external-Handshake-shaking-hands-flat-icons-invisisteve.png" 

st.set_page_config(page_title=NOMBRE_APP, layout="wide", page_icon="🐒")

# --- ESTILO VISUAL MONOTAX ---
st.markdown(f"""
    <style>
    .main {{ background-color: #fcfaf7; }}
    .stMetric {{ background-color: #ffffff; border-left: 5px solid #8d6e63; border-radius: 8px; }}
    div.stButton > button:first-child {{
        background-color: #5d4037;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }}
    .sidebar-text {{ color: #ffffff; font-size: 0.9em; }}
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image(LOGO_URL, width=120)
    st.title(NOMBRE_APP)
    st.write(f"*{ESLOGAN}*")
    st.divider()
    
    menu = st.radio("MENÚ PRINCIPAL", [
        "📊 Mi Estado (Dashboard)", 
        "🤝 Sellar Trato (Facturar)", 
        "🚗 Mis Plataformas (Uber/Rappi)", 
        "💬 Consultorio MonoTax (IA)"
    ])
    
    st.divider()
    # SECCIÓN DE SEGURIDAD
    with st.expander("🔐 Seguridad MonoTax"):
        st.caption("Tus datos fiscales se encriptan bajo protocolo bancario AES-256. No almacenamos tu clave fiscal, solo la usamos para 'el trato' con ARCA.")

# --- LÓGICA DE DATOS ---
if 'ingresos' not in st.session_state:
    st.session_state.ingresos = 450000.0  # Dato inicial de ejemplo

# --- MÓDULOS DE LA APP ---

if menu == "📊 Mi Estado (Dashboard)":
    st.header(f"Bienvenido, Mono 🐒")
    st.subheader("Tu salud fiscal hoy")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Ventas Acumuladas", f"$ {st.session_state.ingresos:,.2f}")
    with col2:
        limite = 1200000
        disponible = limite - st.session_state.ingresos
        st.metric("Margen Cat. A", f"$ {disponible:,.2f}")
    with col3:
        st.metric("Próximo Vencimiento", "20/03")

    # Gráfico de progreso de categoría
    st.write("### Progreso de Categoría")
    progreso = st.session_state.ingresos / limite
    st.progress(progreso)
    st.caption(f"Estás al {progreso*100:.1f}% del límite de la Categoría A.")

elif menu == "🤝 Sellar Trato (Facturar)":
    st.header("Emitir Factura Electrónica")
    st.write("Completá los datos para que el robot de **MonoTax** selle el trato con ARCA.")
    
    with st.form("form_factura"):
        cuit_cli = st.text_input("CUIT Cliente", placeholder="20123456789")
        monto_fact = st.number_input("Monto total del servicio", min_value=0.0)
        detalle = st.text_area("Concepto (Ej: Servicios de transporte)")
        enviar = st.form_submit_button("🤝 SELLAR TRATO")
        
        if enviar:
            with st.spinner("Los monos están gestionando tu CAE..."):
                time.sleep(2) # Simulación de robot
                st.session_state.ingresos += monto_fact
                st.success(f"¡Hecho! Factura emitida. Tu margen se actualizó en el Dashboard.")
                st.balloons()

elif menu == "🚗 Mis Plataformas (Uber/Rappi)":
    st.header("Sincronización Automática")
    st.write("Conectá tus cuentas para que **MonoTax** facture tus ganancias por vos.")
    
    col_u, col_r = st.columns(2)
    with col_u:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png", width=100)
        if st.button("Vincular Uber"):
            st.info("Iniciando robot extractor...")
    with col_r:
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/06/Rappi_logo.svg", width=100)
        if st.button("Vincular Rappi"):
            st.info("Iniciando robot extractor...")

elif menu == "💬 Consultorio MonoTax (IA)":
    st.header("Asesoría Instantánea")
    st.write("Preguntale a la IA lo que necesites sobre impuestos.")
    
    pregunta = st.chat_input("Ej: ¿Qué pasa si me paso de categoría?")
    if pregunta:
        with st.chat_message("assistant", avatar="🐒"):
            st.write(f"Analizando para tu caso particular... Respecto a '{pregunta}', mi consejo es que...")
            st.info("Recordá que como estás en CABA, tu IIBB ya está unificado en el mismo pago.")

