import streamlit as st
import pandas as pd
import sqlite3
import time
from datetime import datetime

# --- 1. CAPA DE SERVICIOS (Lógica de Negocio) ---

def logic_emitir_factura(monto, cuit_cliente, modo_test=True):
    """
    Aquí es donde se integra PyAfipWs o Zeep.
    Por ahora simulamos la respuesta de ARCA.
    """
    if modo_test:
        time.sleep(2) # Simula latencia de red
        return {
            "cae": "76123456789012",
            "vto": "2026-03-05",
            "nro": "0001-00000042",
            "status": "success"
        }
    else:
        # Aquí iría el código de la sección anterior (WSAA + WSFE)
        # return call_arca_webservice(monto, cuit_cliente)
        pass

# --- 2. CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(page_title="Contador IA Pro", layout="wide", page_icon="📈")

# Estilo personalizado para el Dashboard
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ESTADO DE SESIÓN ---
if 'facturas' not in st.session_state:
    st.session_state.facturas = []

# --- 4. BARRA LATERAL (MENÚ) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2643/2643533.png", width=100)
    st.title("Contador IA")
    menu = st.radio("Menú Principal", 
                   ["Dashboard", "Facturador Real", "Sincronizar Apps", "Asesor IA"])
    st.divider()
    st.caption("v1.0.0 - Conectado a ARCA (Modo Test)")

# --- 5. MÓDULOS PRINCIPALES ---

if menu == "Dashboard":
    st.header("📊 Panel de Control")
    
    # Métricas dinámicas
    total_ventas = sum([f['monto'] for f in st.session_state.facturas])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Ingresos Mes", f"$ {total_ventas:,.2f}", "+15%")
    col2.metric("Gastos (OCR)", "$ 120.400", "-2%")
    col3.metric("Límite Cat. A", f"{ (total_ventas/1200000)*100 :.1f}%")

    # Gráfico de ventas
    if st.session_state.facturas:
        df = pd.DataFrame(st.session_state.facturas)
        st.line_chart(df.set_index('fecha')['monto'])
    else:
        st.info("Aún no hay facturas emitidas este mes.")

elif menu == "Facturador Real":
    st.header("📄 Emisión de Factura Electrónica")
    
    with st.container():
        col_a, col_b = st.columns(2)
        with col_a:
            cuit = st.text_input("CUIT del Cliente", placeholder="20-XXXXXXXX-9")
            monto = st.number_input("Monto Total ($)", min_value=0.0, step=100.0)
        with col_b:
            concepto = st.selectbox("Concepto", ["Servicios", "Productos", "Varios"])
            punto_vta = st.number_input("Punto de Venta", value=1)

    if st.button("🚀 Generar Factura con CAE"):
        if monto > 0 and cuit:
            with st.status("Conectando con servidores de ARCA...", expanded=True) as status:
                st.write("🔐 Solicitando Token de acceso (WSAA)...")
                # Aquí llamamos a la lógica real
                res = logic_emitir_factura(monto, cuit)
                
                st.write(f"📡 Enviando Comprobante {res['nro']}...")
                time.sleep(1)
                status.update(label="✅ ¡Factura Autorizada!", state="complete")
            
            # Guardamos en el historial del Dashboard
            nueva_fact = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "monto": monto,
                "cae": res['cae'],
                "nro": res['nro']
            }
            st.session_state.facturas.append(nueva_fact)
            
            st.success(f"Comprobante aceptado. CAE: {res['cae']}")
            st.download_button("Descargar PDF", "Contenido del PDF simulado", f"factura_{res['nro']}.pdf")
        else:
            st.error("Por favor completá los datos del cliente y el monto.")

elif menu == "Sincronizar Apps":
    st.header("🚗 Integración Gig-Economy")
    st.write("Conectá con tus plataformas de trabajo.")
    
    col_u, col_r, col_p = st.columns(3)
    with col_u:
        if st.button("Sincronizar Uber"):
            st.toast("Buscando viajes recientes...")
            time.sleep(2)
            st.success("Detectado: $45.200")
    with col_r:
        st.button("Sincronizar Rappi")
    with col_p:
        st.button("Sincronizar PedidosYa")

elif menu == "Asesor IA":
    st.header("💬 Chat Asesor Fiscal")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

    if prompt := st.chat_input("¿Cuánto puedo facturar hoy?"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # Aquí conectarías con la lógica de tu base de datos
            resp = f"Analizando tus {len(st.session_state.facturas)} facturas de este mes... Podés facturar hasta ${1200000 - total_ventas:,.2f} antes de recategorizarte."
            st.markdown(resp)
            st.session_state.chat_history.append({"role": "assistant", "content": resp})
