import streamlit as st

# 1. Configuración inicial
st.set_page_config(page_title="Tienda Mica Artística", layout="wide")

# 2. TODO EL ESTILO (CSS + Filtros SVG para el efecto dibujo)
st.markdown("""
<style>
    /* Fondo y fuentes generales */
    .stApp { background-color: #001f3f; color: white; }
    
    /* Tarjeta de producto */
    .producto-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 10px;
        color: #333;
        border: 2px solid #333;
    }

    /* EL BOTÓN QUE ELEGISTE (Adaptado para Streamlit) */
    .stButton>button {
        position: relative;
        text-align: center;
        transition: 0.3s ease-in-out;
        cursor: pointer;
        background-color: #FFF159 !important; /* Amarillo tipo ML */
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
        box-shadow: #33333399 2px 2px 0 1px !important;
    }

    .img-producto {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }
</style>

<svg style="position: absolute; width: 0; height: 0;">
  <filter id="handDrawnNoise">
    <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" result="noise" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="2" />
  </filter>
  <filter id="handDrawnNoise2">
    <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="3" result="noise" />
    <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" />
  </filter>
</svg>
""", unsafe_allow_html=True)

# 3. Datos y Lógica
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

productos = [
    {"id": 1, "nombre": "Pantalón Jean", "precio": 50.0, "url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400"},
    {"id": 2, "nombre": "Remera Blanca", "precio": 120.0, "url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=400"},
    {"id": 3, "nombre": "Buzo Hoodie", "precio": 25.0, "url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400"}
]

# 4. Interfaz Principal
st.title("🎨 Boutique Mica (Custom UI)")

col_tienda, col_carrito = st.columns([2.5, 1])

with col_tienda:
    cols = st.columns(3)
    for i, p in enumerate(productos):
        with cols[i]:
            st.markdown(f"""
                <div class="producto-card">
                    <img src="{p['url']}" class="img-producto">
                    <h3 style="margin:0;">{p['nombre']}</h3>
                    <p style="font-size: 1.2rem;"><b>USD {p['precio']}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            # El botón de Streamlit ahora hereda el CSS del estilo "dibujado"
            if st.button(f"✨ AÑADIR", key=f"btn_{p['id']}"):
                st.session_state.carrito.append(p)
                st.toast(f"Añadiste {p['nombre']}")

with col_carrito:
    st.markdown("### 🛒 Carrito")
    for item in st.session_state.carrito:
        st.write(f"· {item['nombre']} ($ {item['precio']})")
    
    total = sum(item['precio'] for item in st.session_state.carrito)
    st.subheader(f"Total: USD {total}")
    
    if st.button("VACIAR CARRITO"):
        st.session_state.carrito = []
        st.rerun()
