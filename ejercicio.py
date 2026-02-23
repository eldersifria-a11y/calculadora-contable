import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Tienda Mica", layout="wide")

# Estilo para que se vea profesional (Azul Marino)
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; color: white; }
    .producto-card {
        background-color: #003366;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #00509d;
        text-align: center;
        margin-bottom: 20px;
    }
    h1, h2, h3, p { color: white !important; }
    .stButton>button { background-color: #ff4b4b; color: white; width: 100%; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Inicializar el Carrito en la memoria (Session State)
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# 3. Datos de los productos (Podés cambiar los nombres y precios)
productos = [
    {"id": 1, "nombre": "Pantalones", "precio": 50.0,50, "imag:"👖"with st.sidebar:
    {"id": 2, "nombre": "Remeras", "precio": 120.0, "img": "👕"},
    {"id": 3, "nombre": "Buzos", "precio": 25.0, "img": "🧥"}
]

st.title("🛍️ Mi Tienda MiCA")
st.write("Seleccioná los productos que desees contratar.")

# 4. Layout de la Tienda (3 columnas para los productos)
col_tienda, col_carrito = st.columns([2, 1])

with col_tienda:
    cols = st.columns(3)
    for i, producto in enumerate(productos):
        with cols[i]:
            st.markdown(f"""
                <div class="producto-card">
                    <div style="font-size: 50px;">{producto['img']}</div>
                    <h3>{producto['nombre']}</h3>
                    <p>Precio: <b>USD {producto['precio']}</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Añadir {producto['nombre']}", key=f"btn_{producto['id']}"):
                st.session_state.carrito.append(producto)
                st.toast(f"✅ {producto['nombre']} añadido")

# 5. Barra Lateral / Columna Derecha: El Carrito
with col_carrito:
    st.subheader("🛒 Tu Carrito")
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        total = 0
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']}: **USD {item['precio']}**")
            total += item['precio']
        
        st.divider()
        st.header(f"Total: USD {total}")
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()
            
        if st.button("🔥 Finalizar Compra"):
            st.success("¡Pedido enviado! Redirigiendo a pago...")
            # Aquí es donde en el futuro pondríamos el link de Mercado Pago o PayPal











