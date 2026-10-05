import streamlit as st

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO CSS
# ==========================================
st.set_page_config(
    page_title="SpotiClone | Panel de Control",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inyección de estilos CSS para apariencia moderna estilo Spotify
st.markdown("""
<style>
    /* Fondo principal y textos */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    /* Contenedores de métricas */
    div[data-testid="stMetricValue"] {
        color: #1DB954 !important;
        font-weight: 700;
    }
    
    div[data-testid="stMetric"] {
        background-color: #181818;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #282828;
    }

    /* Botones primarios */
    .stButton>button {
        background-color: #1DB954;
        color: #FFFFFF;
        border-radius: 20px;
        border: none;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        background-color: #1ed760;
        color: #FFFFFF;
        transform: scale(1.03);
    }

    /* Estilo de pestañas */
    button[data-baseweb="tab"] {
        color: #B3B3B3;
        font-weight: 600;
    }
    
    button[aria-selected="true"] {
        color: #1DB954 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INICIALIZACIÓN DEL ESTADO (session_state)
# ==========================================
if "biblioteca_canciones" not in st.session_state:
    st.session_state.biblioteca_canciones = {
        "Viva la Vida": {"artista": "Coldplay", "reproducciones": 1500},
        "Shape of You": {"artista": "Ed Sheeran", "reproducciones": 2300},
        "Bohemian Rhapsody": {"artista": "Queen", "reproducciones": 850},
        "Blinding Lights": {"artista": "The Weeknd", "reproducciones": 3100},
        "De Música Ligera": {"artista": "Soda Stereo", "reproducciones": 1850},
        "Hotel California": {"artista": "Eagles", "reproducciones": 920},
        "As It Was": {"artista": "Harry Styles", "reproducciones": 2100},
        "Smooth Criminal": {"artista": "Michael Jackson", "reproducciones": 1400},
        "Lamento Boliviano": {"artista": "Los Enanitos Verdes", "reproducciones": 980},
        "Flowers": {"artista": "Miley Cyrus", "reproducciones": 1950},
        "Smells Like Teen Spirit": {"artista": "Nirvana", "reproducciones": 1750},
        "Matador": {"artista": "Los Fabulosos Cadillacs", "reproducciones": 1200},
        "Starboy": {"artista": "The Weeknd", "reproducciones": 1600},
        "Sweet Child O' Mine": {"artista": "Guns N' Roses", "reproducciones": 1150},
        "Rayando el Sol": {"artista": "Maná", "reproducciones": 640},
        "Stay": {"artista": "The Kid LAROI & Justin Bieber", "reproducciones": 1320},
        "Crimen": {"artista": "Gustavo Cerati", "reproducciones": 790},
        "Bad Guy": {"artista": "Billie Eilish", "reproducciones": 1450}
    }

if "cola_reproduccion" not in st.session_state:
    st.session_state.cola_reproduccion = []

if "reproduciendo_actual" not in st.session_state:
    st.session_state.reproduciendo_actual = None

# ==========================================
# 3. ENCABEZADO Y MÉTRICAS SUPERIORES (KPIs)
# ==========================================
st.title("🎵 SpotiClone: El Algoritmo")
st.caption("Sistema de gestión musical sin bibliotecas externas de datos")

# Banner del reproductor actual
if st.session_state.reproduciendo_actual:
    st.info(f"▶️ **Sonando ahora:** {st.session_state.reproduciendo_actual}")

# Cálculo de estadísticas nativas (sin numpy/pandas)
total_canciones = len(st.session_state.biblioteca_canciones)
total_reps = sum(c["reproducciones"] for c in st.session_state.biblioteca_canciones.values())

hit_top = ("N/A", {"reproducciones": 0})
if total_canciones > 0:
    hit_top = max(st.session_state.biblioteca_canciones.items(), key=lambda x: x[1]["reproducciones"])

# Tarjetas de impacto visual
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("📚 Canciones Registradas", total_canciones)
kpi2.metric("▶️ Reproducciones Totales", f"{total_reps:,}")
kpi3.metric("🔥 Hit #1 del Momento", hit_top[0], f"{hit_top[1]['reproducciones']} reps")
kpi4.metric("🎧 Canciones en Cola", len(st.session_state.cola_reproduccion))

st.divider()

# ==========================================
# 4. NAV NAVEGACIÓN Y SECCIONES
# ==========================================
tab_biblio, tab_hits, tab_cola, tab_gestion = st.tabs([
    "📚 Biblioteca de Canciones", 
    "🔥 Reporte de Hits (>1000)", 
    "🎧 Cola de Reproducción", 
    "⚙️ Gestión de Canciones"
])

# ------------------------------------------
# TAB 1: BIBLIOTECA DE CANCIONES
# ------------------------------------------
with tab_biblio:
    st.subheader("Catálogo Principal")
    
    # Buscador interactivo
    busqueda = st.text_input("🔍 Buscar por título o artista:", "").strip().lower()
    st.write("")
    
    if total_canciones == 0:
        st.warning("⚠️ La biblioteca de canciones se encuentra vacía.")
    else:
        # Calcular máxima cantidad de reproducciones para barras relativas
        max_reps = max([c["reproducciones"] for c in st.session_state.biblioteca_canciones.values()], default=1)
        
        canciones_filtradas = {
            t: info for t, info in st.session_state.biblioteca_canciones.items()
            if busqueda in t.lower() or busqueda in info["artista"].lower()
        }

        if not canciones_filtradas:
            st.info("No se encontraron canciones que coincidan con la búsqueda.")
        else:
            for titulo, info in canciones_filtradas.items():
                col_info, col_bar, col_btn = st.columns([3, 4, 2])
                
                with col_info:
                    st.markdown(f"**🎵 {titulo}**")
                    st.caption(f"👤 {info['artista']}")
                
                with col_bar:
                    porcentaje = min(info["reproducciones"] / max(max_reps, 1), 1.0)
                    st.progress(porcentaje, text=f"{info['reproducciones']} reproducciones")
                
                with col_btn:
                    if st.button("➕ Agregar a la lista", key=f"add_queue_{titulo}", use_container_width=True):
                        st.session_state.cola_reproduccion.append(titulo)
                        st.toast(f"✅ '{titulo}' agregada a la cola.", icon="🎵")
                        st.rerun()
                st.divider()

# ------------------------------------------
# TAB 2: REPORTE DE HITS
# ------------------------------------------
with tab_hits:
    st.subheader("🔥 Canciones Destacadas (> 1000 reproducciones)")
    
    hits = {t: info for t, info in st.session_state.biblioteca_canciones.items() if info["reproducciones"] > 1000}
    
    if not hits:
        st.info("Actualmente ninguna canción supera las 1000 reproducciones.")
    else:
        for titulo, info in hits.items():
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"⭐ **{titulo}** — *{info['artista']}*")
            with c2:
                st.metric(label="Popularidad", value=info["reproducciones"])
            st.divider()

# ------------------------------------------
# TAB 3: COLA DE REPRODUCCIÓN
# ------------------------------------------
with tab_cola:
    st.subheader("🎧 Cola de Reproducción")
    
    col_play, _ = st.columns([2, 2])
    with col_play:
        if st.button("▶️ Reproducir siguiente canción", use_container_width=True):
            if len(st.session_state.cola_reproduccion) == 0:
                st.warning("⚠️ La cola de reproducción está vacía.")
            else:
                siguiente = st.session_state.cola_reproduccion.pop(0)
                st.session_state.reproduciendo_actual = siguiente
                st.toast(f"▶️ Sonando ahora: '{siguiente}'", icon="🎶")
                st.rerun()

    st.write("---")

    if len(st.session_state.cola_reproduccion) == 0:
        st.info("No hay canciones en la cola de reproducción.")
    else:
        st.write(f"**Próximas canciones ({len(st.session_state.cola_reproduccion)}):**")
        
        for idx, titulo in enumerate(st.session_state.cola_reproduccion):
            c_pos, c_title, c_act = st.columns([1, 4, 2])
            with c_pos:
                st.write(f"**#{idx + 1}**")
            with c_title:
                artista = st.session_state.biblioteca_canciones.get(titulo, {}).get("artista", "Desconocido")
                st.write(f"🎵 **{titulo}** — *{artista}*")
            with c_act:
                if st.button("🗑️ Remover", key=f"remove_queue_{idx}", use_container_width=True):
                    st.session_state.cola_reproduccion.pop(idx)
                    st.toast(f"🗑️ Canción removida de la cola.", icon="❌")
                    st.rerun()

# ------------------------------------------
# TAB 4: GESTIÓN DE CANCIONES
# ------------------------------------------
with tab_gestion:
    col_left, col_right = st.columns(2)
    
    # Formulario 1: Alta de canciones
    with col_left:
        st.subheader("➕ Registrar Nueva Canción")
        with st.form(key="form_agregar_cancion", clear_on_submit=True):
            nuevo_titulo = st.text_input("Título de la canción")
            nuevo_artista = st.text_input("Artista")
            submit_agregar = st.form_submit_button("Registrar Canción", use_container_width=True)
            
            if submit_agregar:
                t_clean = nuevo_titulo.strip()
                a_clean = nuevo_artista.strip()
                
                if not t_clean or not a_clean:
                    st.error("❌ Por favor completa ambos campos.")
                elif t_clean in st.session_state.biblioteca_canciones:
                    st.error(f"❌ La canción '{t_clean}' ya existe en la biblioteca.")
                else:
                    st.session_state.biblioteca_canciones[t_clean] = {
                        "artista": a_clean,
                        "reproducciones": 0
                    }
                    st.success(f"✅ '{t_clean}' de '{a_clean}' registrada con éxito.")
                    st.rerun()

    # Formulario 2: Sumar reproducciones
    with col_right:
        st.subheader("📈 Incrementar Reproducciones")
        if total_canciones > 0:
            with st.form(key="form_sumar_reps", clear_on_submit=True):
                cancion_sel = st.selectbox(
                    "Selecciona la canción", 
                    options=list(st.session_state.biblioteca_canciones.keys())
                )
                cantidad_sumar = st.number_input("Cantidad a sumar", min_value=1, value=100, step=10)
                submit_sumar = st.form_submit_button("Sumar Reproducciones", use_container_width=True)
                
                if submit_sumar:
                    st.session_state.biblioteca_canciones[cancion_sel]["reproducciones"] += cantidad_sumar
                    total = st.session_state.biblioteca_canciones[cancion_sel]["reproducciones"]
                    st.success(f"✅ Se sumaron {cantidad_sumar} reproducciones a '{cancion_sel}'. Total: {total}.")
                    st.rerun()
        else:
            st.info("No hay canciones disponibles para actualizar.")