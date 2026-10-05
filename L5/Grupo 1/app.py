import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE PÁGINA Y ESTILOS (CSS PERSONALIZADO)
# ==============================================================================
st.set_page_config(
    page_title="Fantasía FC - Sistema DT",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #f4f6fa;
        color: #121358;
    }
    [data-testid="stSidebar"] {
        background-color: #121358;
        color: #ffffff;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    h1, h2, h3 {
        color: #121358 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
    }
    .tabla-futbol {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 1rem;
        background-color: #ffffff;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    .tabla-futbol th {
        background-color: #232F72;
        color: #ffffff;
        text-align: left;
        padding: 12px 15px;
        font-weight: bold;
    }
    .tabla-futbol td {
        padding: 10px 15px;
        border-bottom: 1px solid #e2e8f0;
        color: #121358;
    }
    .tabla-futbol tr:hover {
        background-color: #f1f5f9;
    }
    .stButton>button {
        background-color: #36ADA3;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2F578A;
        color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# INICIALIZACIÓN DE VARIABLES EN SESSION STATE
# ==============================================================================
if "plantel_jugadores" not in st.session_state:
    st.session_state.plantel_jugadores = {
        "Lionel_Messi": {"posicion": "Delantero", "puntos": 0},
        "Rodrigo_De_Paul": {"posicion": "Mediocampista", "puntos": 0},
        "Lisandro_Martinez": {"posicion": "Defensa", "puntos": 0},
        "Emiliano_Martinez": {"posicion": "Arquero", "puntos": 0},
    }

if "lista_fichajes" not in st.session_state:
    st.session_state.lista_fichajes = [
        "Julian_Alvarez",
        "Cristian_Romero",
        "Lautaro_Martinez",
        "Enzo_Fernandez",
        "Alexis_Mac_Allister",
        "Facundo_Medina"
    ]

# ==============================================================================
# LÓGICA DE NEGOCIO
# ==============================================================================
def registrar_jugador(nombre_jugador, posicion):
    if nombre_jugador in st.session_state.plantel_jugadores:
        st.warning(f"⚠️ ¡Atención Ref! El jugador {nombre_jugador} ya fue agregado previamente.")
    else:
        st.session_state.plantel_jugadores[nombre_jugador] = {
            "posicion": posicion,
            "puntos": 0
        }
        st.toast(f"⚽ ¡GOLAZO! {nombre_jugador} fue agregado al plantel ({posicion}).", icon="✅")
        st.rerun()

def cargar_puntos(nombre_jugador, cantidad):
    if cantidad > 3:
        st.error("❌ **¡Límite superado!** Solo puedes asignar hasta 3 puntos por carga.")
        return
        
    if nombre_jugador in st.session_state.plantel_jugadores:
        st.session_state.plantel_jugadores[nombre_jugador]["puntos"] += cantidad
        total_puntos = st.session_state.plantel_jugadores[nombre_jugador]["puntos"]
        st.toast(f"🔥 +{cantidad} pts a {nombre_jugador}. Total: {total_puntos} pts.", icon="🌟")
        st.rerun()
    else:
        st.error("❌ El jugador ingresado no figura en el plantel.")

def reportar_destacados():
    if not st.session_state.plantel_jugadores:
        st.warning("⚠️ El plantel se encuentra actualmente vacío.")
    else:
        encontrados = False
        st.subheader("⭐ Jugadores Destacados (Más de 10 Puntos)")
        for jugador, datos in st.session_state.plantel_jugadores.items():
            puntos = datos["puntos"]
            if puntos > 10:
                posicion = datos["posicion"]
                st.balloons()
                st.success(f"🏆 **¡CRACK TOTAL!** {jugador} ({posicion}) es figura con **{puntos}** puntos.")
                encontrados = True
        if not encontrados:
            st.info("ℹ️ Ningún jugador ha superado los **10 puntos** en el torneo.")

def agregar_a_fichajes(nombre_jugador):
    if nombre_jugador in st.session_state.plantel_jugadores:
        st.session_state.lista_fichajes.append(nombre_jugador)
        posicion = len(st.session_state.lista_fichajes)
        st.toast(f"📋 {nombre_jugador} agregado a fichajes en posición #{posicion}.", icon="📝")
        st.rerun()
    else:
        st.error("🚨 El jugador ingresado no pertenece al plantel.")

def llamar_siguiente_fichaje():
    if not st.session_state.lista_fichajes:
        st.warning("⚠️ No hay jugadores en la lista de espera de fichajes.")
    else:
        siguiente_jugador = st.session_state.lista_fichajes.pop(0)
        # Añadir automáticamente al plantel al ser contratado
        st.session_state.plantel_jugadores[siguiente_jugador] = {
            "posicion": "Fichaje",
            "puntos": 0
        }
        st.toast(f"🎉 ¡CONTRATACIÓN OFICIAL! {siguiente_jugador} sumado al plantel.", icon="⚽")
        st.rerun()

def remover_de_fichajes(nombre_jugador):
    if nombre_jugador in st.session_state.lista_fichajes:
        st.session_state.lista_fichajes.remove(nombre_jugador)
        st.toast(f"🗑️ {nombre_jugador} removido de la lista de fichajes.", icon="ℹ️")
        st.rerun()
    else:
        st.error("❌ El jugador ingresado no figura en la lista de fichajes.")

# ==============================================================================
# DASHBOARD PRINCIPAL
# ==============================================================================
st.title("⚽ FANTASÍA FC - SISTEMA DT 🏆")
st.markdown("### *Panel de Control Táctico y Gestión de Plantel Profesional* 📊")

st.divider()

col1, col2, col3, col4 = st.columns(4)

total_plantel = len(st.session_state.plantel_jugadores)
total_fichajes = len(st.session_state.lista_fichajes)
max_puntos = max([j["puntos"] for j in st.session_state.plantel_jugadores.values()], default=0)
figuras_count = sum(1 for j in st.session_state.plantel_jugadores.values() if j["puntos"] > 10)

with col1:
    st.metric(label="👕 Total Plantel", value=f"{total_plantel} Jugadores", delta="Plantel Oficial")

with col2:
    st.metric(label="📋 En Espera de Fichaje", value=f"{total_fichajes} Jugadores", delta="Transferencias")

with col3:
    st.metric(label="🟨 Top Puntos", value=f"{max_puntos} Pts", delta="Máximo Puntaje")

with col4:
    st.metric(label="🟥 Figuras (>10 pts)", value=f"{figuras_count} Jugadores", delta="Destacados")

st.divider()

# ==============================================================================
# MENÚ LATERAL
# ==============================================================================
st.sidebar.title("🎛️ MENÚ DE OPCIONES DT")
st.sidebar.markdown("---")

opcion = st.sidebar.radio(
    "Selecciona una opción táctica:",
    [
        "1. ➕ Registrar jugador",
        "2. 🏅 Cargar puntos",
        "3. 📋 Ver plantel y fichajes",
        "4. ⭐ Reportar destacados",
        "5. 📥 Agregar a fichajes",
        "6. 📢 Llamar siguiente fichaje",
        "7. 🗑️ Remover de fichajes",
        "8. 🏁 Salir del torneo"
    ]
)

# ==============================================================================
# NAVEGACIÓN
# ==============================================================================
if "1. ➕ Registrar jugador" in opcion:
    st.header("➕ Registrar Jugador en Plantel")
    with st.form("form_registrar"):
        col_nom, col_pos = st.columns(2)
        with col_nom:
            nombre = st.text_input("👤 Nombre del Jugador:")
        with col_pos:
            posicion = st.selectbox("🏃‍♂️ Posición:", ["Delantero", "Mediocampista", "Defensa", "Arquero"])
        
        btn_registrar = st.form_submit_button("⚽ Registrar Jugador")
        if btn_registrar:
            if nombre.strip():
                registrar_jugador(nombre.strip().replace(" ", "_"), posicion)
            else:
                st.warning("⚠️ Ingresa un nombre válido.")

elif "2. 🏅 Cargar puntos" in opcion:
    st.header("🏅 Cargar Puntos a Jugador")
    st.info("ℹ️ **Regla de puntuación:** Puedes asignar como máximo **3 puntos** por operación.")
    
    if not st.session_state.plantel_jugadores:
        st.warning("⚠️ No hay jugadores en el plantel para asignar puntos.")
    else:
        with st.form("form_puntos"):
            jugador_sel = st.selectbox("👤 Selecciona el Jugador:", list(st.session_state.plantel_jugadores.keys()))
            puntos_num = st.number_input("🎯 Cuántos puntos deseas cargar (Máximo 3):", min_value=1, max_value=3, value=1)
            btn_puntos = st.form_submit_button("🔥 Cargar Puntos")
            
            if btn_puntos:
                cargar_puntos(jugador_sel, puntos_num)

elif "3. 📋 Ver plantel y fichajes" in opcion:
    st.header("📋 Vista General de Plantel y Lista de Fichajes")
    col_plantel, col_fichajes = st.columns(2)
    
    with col_plantel:
        st.subheader("👕 Plantel Oficial")
        if st.session_state.plantel_jugadores:
            html_plantel = "<table class='tabla-futbol'>"
            html_plantel += "<thead><tr><th>Jugador 🏃‍♂️</th><th>Posición 📍</th><th>Puntos ⚽</th></tr></thead><tbody>"
            for jug, datos in st.session_state.plantel_jugadores.items():
                nombre_clean = jug.replace("_", " ")
                html_plantel += f"<tr><td><b>{nombre_clean}</b></td><td>{datos['posicion']}</td><td><b>{datos['puntos']} pts</b></td></tr>"
            html_plantel += "</tbody></table>"
            st.markdown(html_plantel, unsafe_allow_html=True)
        else:
            st.info("El plantel se encuentra vacío.")
            
    with col_fichajes:
        st.subheader("📝 Lista de Espera (Fichajes)")
        if st.session_state.lista_fichajes:
            html_fichajes = "<table class='tabla-futbol'>"
            html_fichajes += "<thead><tr><th>Orden 🔢</th><th>Jugador ⚽</th></tr></thead><tbody>"
            for idx, jug in enumerate(st.session_state.lista_fichajes):
                nombre_clean = jug.replace("_", " ")
                html_fichajes += f"<tr><td><b>#{idx + 1}</b></td><td>{nombre_clean}</td></tr>"
            html_fichajes += "</tbody></table>"
            st.markdown(html_fichajes, unsafe_allow_html=True)
        else:
            st.info("No hay jugadores en la lista de espera.")

elif "4. ⭐ Reportar destacados" in opcion:
    st.header("⭐ Reporte de Figuras del Torneo")
    reportar_destacados()

elif "5. 📥 Agregar a fichajes" in opcion:
    st.header("📥 Agregar Jugador a la Lista de Fichajes")
    if not st.session_state.plantel_jugadores:
        st.warning("⚠️ No hay jugadores disponibles en el plantel.")
    else:
        with st.form("form_agregar_fichaje"):
            jugador_fich = st.selectbox("👤 Selecciona el Jugador:", list(st.session_state.plantel_jugadores.keys()))
            btn_add_fich = st.form_submit_button("📝 Agregar a Fichajes")
            if btn_add_fich:
                agregar_a_fichajes(jugador_fich)

elif "6. 📢 Llamar siguiente fichaje" in opcion:
    st.header("📢 Llamar Siguiente Fichaje en Cola")
    st.markdown("Al presionar el botón, el primer jugador en lista de espera pasará directamente al plantel oficial.")
    if st.button("🚀 Fichar Siguiente Jugador"):
        llamar_siguiente_fichaje()

elif "7. 🗑️ Remover de fichajes" in opcion:
    st.header("🗑️ Remover Jugador de la Lista de Fichajes")
    if not st.session_state.lista_fichajes:
        st.warning("⚠️ La lista de fichajes está vacía.")
    else:
        with st.form("form_remover"):
            jugador_rem = st.selectbox("👤 Selecciona el Jugador a Sacar:", st.session_state.lista_fichajes)
            btn_rem = st.form_submit_button("❌ Remover de Fichajes")
            if btn_rem:
                remover_de_fichajes(jugador_rem)

elif "8. 🏁 Salir del torneo" in opcion:
    st.header("🏁 Cierre de Torneo")
    st.balloons()
    st.success("🏆 **Querida organización del torneo, el torneo ha llegado a su fin. Muchas gracias por jugar.** ⚽🎉")

