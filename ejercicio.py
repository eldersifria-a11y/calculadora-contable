import streamlit as st
import pandas as pd
import time

# --- MARCA Y CONFIGURACIÓN ---
NOMBRE_APP = "MonoTax"
ESLOGAN = "Sellar el trato nunca fue tan fácil."
LOGO_URL = "https://img.icons8.com/color/512/handshake.png" # Representa el trato

st.set_page_config(page_title=NOMBRE_APP, layout="wide", page_icon="🐒")

# --- DISEÑO UI PREMIUM (CSS) ---
st.markdown(f"""
    <style>
    /* Fondo general */
    .stApp {{
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }}
    
    /* Estilo de Tarjetas del Dashboard */
    .metric-card {{
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border: 1px solid #eee;
        text-align: center;
    }}
    
    /* Personalización de Botones */
    div.stButton > button:first-child {{
        background: linear-gradient(45deg, #5d4037, #8d6e63);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }}
    
    div.stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(93, 64, 55, 0.3);
    }}

    /* Sidebar moderna */
    [data-testid="stSidebar"] {{
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }}

    /* Títulos */
    h1, h2, h3 {{
        color: #3e2723;
        font-family: 'Inter', sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR MEJORADA ---
with st.sidebar:
    st.image(LOGO_URL, width=100)
    st.markdown(f"# {NOMBRE_APP}")
    st.markdown(f"*{ESLOGAN}*")
    st.markdown("---")
    
    menu = st.radio("MENÚ", 
        ["📊 Mi Estado", "🤝 Sellar Trato", "🚗 Plataformas", "💬 Consultorio IA"],
        label_visibility="collapsed")
    
    st.markdown("---")
    st.caption("🔒 **Seguridad Nivel Bancario**")
    st.caption("Conectado con ARCA v2.4")

# --- CONTENIDO DINÁMICO ---

if menu == "📊 Mi Estado":
    st.markdown(f"## 🐒 ¡Hola, Mono!")
    st.markdown("Tu resumen fiscal actualizado al día de hoy.")
    
    # Grid de métricas con estilo manual para mejor visual
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Ventas Acumuladas", "$ 450.000")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Margen Cat. A", "$ 750.000")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Impuesto a Pagar", "$ 26.600")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Progreso de Categoría")
    # Barra de progreso personalizada
    st.progress(0.37)
    st.caption("Estás al 37% de tu límite anual de Categoría A. ¡Venís perfecto!")

elif menu == "🤝 Sellar Trato":
    st.markdown("## 📄 Emitir Nueva Factura")
    st.markdown("Completá los datos y nosotros nos encargamos de los monos de ARCA.")
    
    with st.container():
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        cuit = st.text_input("CUIT del Cliente")
        monto = st.number_input("Monto a Facturar ($)", min_value=0.0)
        detalle = st.text_input("Concepto o Descripción")
        
        if st.button("Sellar Trato"):
            with st.spinner("Procesando firma digital..."):
                time.sleep(2)
                st.success("✅ ¡Trato Sellado! Factura emitida con éxito.")
                st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🚗 Plataformas":
    st.markdown("## 🚗 Conexión de Plataformas")
    st.markdown("Sincronizá tus ingresos automáticamente.")
    
    col_u, col_r = st.columns(2)
    with col_u:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png", width=80)
        st.button("Vincular Uber")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_r:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/06/Rappi_logo.svg", width=80)
        st.button("Vincular Rappi")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "💬 Consultorio IA":
    st.markdown("## 💬 Tu Asistente Mono-Expert")
    st.markdown("Preguntá lo que sea, no pagás IVA por las dudas.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("¿Cuánto puedo facturar hoy?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant", avatar="🐒"):
            response = "Basado en tu facturación actual, podés facturar hasta $150.000 esta semana para mantenerte seguro en tu categoría."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
