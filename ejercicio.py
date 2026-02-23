import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Tienda Mica - Versión Final", layout="wide")

# 2. BLOQUE DE ESTILO INTEGRADO (CSS + Filtros SVG)
st.markdown("""
<style>
    /* Estética General */
    .stApp { background-color: #001f3f; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Tarjeta de Producto (Estilo Limpio) */
    .producto-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 10px;
        color: #333;
        border: 2px solid #333;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .img-producto {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 15px;
    }

    /* BOTÓN ARTÍSTICO (Uiverse - AatreyuShau) */
    .stButton>button {
        position: relative;
        text-align: center;
        transition: 0.3s ease-in-out;
        cursor: pointer;
        background-color: #FFF159 !important;
        filter: url(#handDrawnNoise);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-family: "Courier New", monospace !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        border: 2px solid #333 !important;
        border-radius: 2rem !important;
        box-shadow: #33333366 4px 4px 0 1px !important;
        color: #333 !important;
        width: 100% !important;
        animation: idle 1.5s infinite ease-in-out;
    }
    @keyframes idle {
        0% { filter: url(#handDrawnNoise); rotate: 0deg; }
        50% { rotate: 1.5deg; filter: url(#handDrawnNoise2); }
        100% { filter: url(#handDrawnNoise); rotate: 0deg; }
    }
    .stButton>button:hover {
        rotate: -2.5deg !important;
        background-color: #ffdb00 !important;
    }

    /* LOADER (Uiverse - KSAplay) */
    .loader { display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 5px; margin: 20px 0; }
    .loading-text { color: white; font-size: 14pt; font-weight: 600; display: flex; }
    .dot { margin-left: 3px; animation: blink 1.5s infinite; }
    .dot:nth-child(2) { animation-delay: 0.3s; }
    .dot:nth-child(3) { animation-delay: 0.6s; }
    .loading-bar-background {
        --height: 30px; display: flex; align-items: center; padding: 5px; width: 200px; height: var(--height);
        background-color: #212121; border-radius: calc(var(--height) / 2);
    }
    .loading-bar {
        position: relative; width: 0%; height: 20px; overflow: hidden;
        background: linear-gradient(0deg, rgba(222, 74, 15, 1) 0%, rgba(249, 199, 79, 1) 100%);
        border-radius: 10px; animation: loading 4s ease-out infinite;
    }
    @keyframes loading { 0% { width: 0; } 80% { width: 100%; } 100% { width: 100%; } }
    @keyframes blink { 0%, 100% { opacity: 0; } 50% { opacity: 1; } }
</style>

<svg style="position: absolute; width: 0; height: 0;">
  <filter id="handDrawnNoise"><feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
  <filter id="handDrawnNoise2"><feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="3" /><feDisplacementMap in="SourceGraphic" scale="3" /></filter>
</svg>
""", unsafe_allow_html=True)

# 3. Lógica del Carrito
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# Datos de Productos
productos = [
    {"id": 1, "nombre": "Pantalón Jean", "precio": 50.0, "url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400"},
    {"id": 2, "nombre": "Remera Algodón", "precio": 120.0, "url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=400"},
    {"id": 3, "nombre": "Buzo Hoodie", "precio": 25.0, "url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400"}
]

# 4. Interfaz - Cabecera
col_logo, col_vacia = st.columns([1, 8])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=80)

st.title("🛍️ Tienda Mica - E-commerce")
st.write("Bienvenido a tu experiencia de compra personalizada.")

# 5. Cuerpo de la Tienda
col_tienda, col_carrito = st.columns([2.5, 1])

with col_tienda:
    cols = st.columns(3)
    for i, p in enumerate(productos):
        with cols[i]:
            st.markdown(f"""
                <div class="producto-card">
                    <img src="{p['url']}" class="img-producto">
                    <h3 style="margin:0;">{p['nombre']}</h3>
                    <p style="font-size: 1.2rem; color: #333;"><b>USD {p['precio']}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"✨ AÑADIR", key=f"btn_{p['id']}"):
                st.session_state.carrito.append(p)
                st.toast(f"✅ {p['nombre']} al carrito")

with col_carrito:
    st.markdown("### 🛒 Carrito de Compras")
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        for item in st.session_state.carrito:
            st.write(f"• {item['nombre']} ($ {item['precio']})")
        
        total = sum(item['precio'] for item in st.session_state.carrito)
        st.divider()
        st.subheader(f"Total: USD {total}")
        
        if st.button("VACIAR CARRITO"):
            st.session_state.carrito = []
            st.rerun()

        if st.button("🔥 FINALIZAR COMPRA"):
            placeholder = st.empty()
            with placeholder:
                # Mostramos el loader de Uiverse
                st.markdown("""
                <div class="loader">
                    <div class="loading-text">Procesando Pago<span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></div>
                    <div class="loading-bar-background"><div class="loading-bar"></div></div>
                </div>""", unsafe_allow_html=True)
                time.sleep(4)
            placeholder.empty()
            st.success("¡Pedido realizado con éxito!")
