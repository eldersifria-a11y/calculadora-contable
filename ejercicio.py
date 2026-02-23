import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Tienda jony", layout="wide")

# --- CABECERA CON LOGO ---
col_logo, col_espacio = st.columns([1, 8])
with col_logo:
    # Logo de ejemplo (podés cambiar el URL)
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=80) 

# 2. Estilo CSS
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; color: white; }
    .producto-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }
    .producto-card h3, .producto-card p { color: #333 !important; margin: 5px 0; }
    .img-producto {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 8px;
    }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Inicializar el Carrito
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# 4. Datos de los productos (LISTA CORREGIDA)
productos = [
    {
        "id": 1, 
        "nombre": "Pantalón Jean", 
        "precio": 50.0, 
        "url": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=500"
    },
    {
        "id": 2, 
        "nombre": "Remera Algodón", 
        "precio": 120.0, 
        "url": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500"
    },
    {
        "id": 3, 
        "nombre": "Buzo con Capucha", 
        "precio": 25.0, 
        "url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500"
    }
]

st.title("🛍️ Mi Tienda MiCA")

# 5. Layout de la Tienda
col_tienda, col_carrito = st.columns([2, 1])

with col_tienda:
    cols = st.columns(3)
    for i, producto in enumerate(productos):
        with cols[i]:
            st.markdown(f"""
                <div class="producto-card">
                    <img src="{producto['url']}" class="img-producto">
                    <h3>{producto['nombre']}</h3>
                    <p><b>USD {producto['precio']}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Añadir {producto['nombre']}", key=f"btn_{producto['id']}"):
                st.session_state.carrito.append(producto)
                st.toast(f"✅ {producto['nombre']} añadido")

# 6. Carrito
with col_carrito:
    st.subheader("🛒 Tu Carrito")
    if not st.session_state.carrito:
        st.write("Está vacío.")
    else:
        total = 0
        for item in st.session_state.carrito:
            st.write(f"• {item['nombre']} - ${item['precio']}")
            total += item['precio']
        
        st.divider()
        st.header(f"Total: ${total}")
        
        if st.button("Vaciar"):
            st.session_state.carrito = []
            st.rerun()













