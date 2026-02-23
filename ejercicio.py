import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Contable", page_icon="📊")

st.title("📊 Mi Software de Gestión")
st.markdown("---")

# Barra lateral para ingresar datos
st.sidebar.header("Panel de Control")
v_enero = st.sidebar.number_input("Venta de Enero ($)", value=5000, step=100)
crecimiento = st.sidebar.number_input("Crecimiento Mensual ($)", value=100, step=10)

# Lógica de cálculo
v_feb = v_enero + crecimiento
v_mar = v_feb + crecimiento
v_abr = v_mar + crecimiento

# Fórmulas de Saldo de Clientes
saldo_mar = (v_mar * 0.60) + (v_feb * 0.30)
saldo_abr = (v_abr * 0.60) + (v_mar * 0.30)

# Diseño de la aplicación
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Ventas")
    st.write(f"**Febrero:** ${v_feb:,.2f}")
    st.write(f"**Marzo:** ${v_mar:,.2f}")
    st.write(f"**Abril:** ${v_abr:,.2f}")

with col2:
    st.subheader("💰 Saldo Clientes")
    st.metric(label="Saldo al 31/03", value=f"${saldo_mar:,.2f}")
    st.metric(label="Saldo al 30/04", value=f"${saldo_abr:,.2f}", delta=f"${saldo_abr - saldo_mar}")

st.markdown("---")
st.info("💡 Este software utiliza la política de cobranza: 40% contado, 30% a 30 días y 30% a 60 días.")