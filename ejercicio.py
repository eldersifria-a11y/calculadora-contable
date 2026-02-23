import streamlit as st
import pandas as pd

# 1. Configuración profesional
st.set_page_config(page_title="Gestión Contable Pro", page_icon="📈", layout="wide")

st.title("📊 Dashboard de Proyecciones Contables")
st.markdown("---")

# 2. Sidebar organizada
st.sidebar.header("⚙️ Configuración de Datos")
v_enero = st.sidebar.number_input("Ventas Enero ($)", value=5000.0, step=500.0)
crecimiento = st.sidebar.number_input("Crecimiento Mensual ($)", value=200.0, step=50.0)

# 3. Lógica de cálculo (Matriz de datos)
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [v_enero, v_enero + crecimiento, v_enero + (2*crecimiento), v_enero + (3*crecimiento)]

# Cálculos de saldos
saldo_mar = (ventas[2] * 0.60) + (ventas[1] * 0.30)
saldo_abr = (ventas[3] * 0.60) + (ventas[2] * 0.30)

# 4. Visualización de Métricas Principales (Tarjetas)
col1, col2, col3 = st.columns(3)
col1.metric("Venta Total Proyectada", f"${sum(ventas):,.2f}")
col2.metric("Saldo Clientes (Marzo)", f"${saldo_mar:,.2f}")
col3.metric("Saldo Clientes (Abril)", f"${saldo_abr:,.2f}", delta=f"{((saldo_abr/saldo_mar)-1)*100:.1f}%")

st.markdown("---")

# 5. Gráfico y Tabla lado a lado
col_izq, col_der = st.columns([2, 1])

with col_izq:
    st.subheader("📈 Evolución de Ventas")
    df = pd.DataFrame({"Mes": meses, "Ventas": ventas})
    st.line_chart(df.set_index("Mes"))

with col_der:
    st.subheader("📋 Detalle Mensual")
    st.dataframe(df, hide_index=True, use_container_width=True)

# 6. Pie de página informativo
st.success(f"Proyección finalizada con éxito para el mes de {meses[-1]}")import streamlit as st

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
