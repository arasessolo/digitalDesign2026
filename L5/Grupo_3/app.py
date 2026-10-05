import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS VINTAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Refugio de Mascotas - Cuidado Animal",
    page_icon="🐾",
    layout="wide"
)

# Estilos CSS personalizados (Paleta Vintage: #622B14, #995F2F, #978F66, #E4D6A9)
st.markdown("""
    <style>
        /* Fondo general de la app */
        .stApp {
            background-color: #E4D6A9;
            color: #622B14;
            font-family: 'Georgia', serif;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #978F66;
            color: #622B14;
        }
        
        /* Títulos y Encabezados */
        h1, h2, h3, h4 {
            color: #622B14 !important;
            font-family: 'Georgia', serif;
        }
        
        /* Botones generales */
        .stButton>button {
            background-color: #995F2F;
            color: #E4D6A9;
            border-radius: 8px;
            border: 1px solid #622B14;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #622B14;
            color: #E4D6A9;
            border-color: #995F2F;
        }

        /* Tarjetas de métricas */
        [data-testid="stMetricValue"] {
            color: #622B14 !important;
        }
        [data-testid="stMetricLabel"] {
            color: #995F2F !important;
        }

        /* Divisores */
        hr {
            border-top: 2px solid #995F2F;
        }
    </style>
""", unsafe_allow_allow_html=True)

# ---------------------------------------------------------
# INICIALIZACIÓN DEL ESTADO DE SESIÓN (st.session_state)
# ---------------------------------------------------------
if "padron_mascotas" not in st.session_state:
    st.session_state.padron_mascotas = {
        "Luna": {"especie": "labrador", "edad": 5, "vacunas_cant": 3},
        "Aurora": {"especie": "golden", "edad": 7, "vacunas_cant": 5},
        "Estrellita": {"especie": "pomeraña", "edad": 3, "vacunas_cant": 1},
    }

if "lista_adoptante" not in st.session_state:
    st.session_state.lista_adoptante = []

# ---------------------------------------------------------
# LÓGICA DE NEGOCIO Y FUNCIONES DE SOPORTE
# ---------------------------------------------------------
def registrar_mascota(nombre_mascota, especie):
    st.session_state.padron_mascotas[nombre_mascota] = {
        "especie": especie,
        "vacunas_cant": 0
    }

def aplicar_vacuna(nombre_mascota, vacunas_cant):
    if nombre_mascota in st.session_state.padron_mascotas:
        st.session_state.padron_mascotas[nombre_mascota]["vacunas_cant"] += vacunas_cant
        return True
    return False

def agregar_a_espera_adopcion(nombre_adoptante):
    if nombre_adoptante in st.session_state.lista_adoptante:
        return False, "Ya estás registrado"
    else:
        st.session_state.lista_adoptante.append(nombre_adoptante)
        orden_numero = st.session_state.lista_adoptante.index(nombre_adoptante) + 1
        return True, f"Tu número de orden es {orden_numero}"

def atender_siguiente_adoptante():
    if not st.session_state.lista_adoptante:
        return None
    else:
        adoptante = st.session_state.lista_adoptante.pop(0)
        return adoptante

def remover_de_espera_adopcion(nombre_adoptante):
    if nombre_adoptante in st.session_state.lista_adoptante:
        st.session_state.lista_adoptante.remove(nombre_adoptante)
        return True
    return False

# ---------------------------------------------------------
# BARRA LATERAL (st.sidebar): INFORMACIÓN Y MÉTRICAS
# ---------------------------------------------------------
with st.sidebar:
    st.title("🐾 Refugio Vintage")
    st.markdown("**Cliente 10 - Cuidado Animal**")
    st.write("---")
    
    # Métricas del sistema
    st.subheader("Estado del Refugio")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("Mascotas", len(st.session_state.padron_mascotas))
    with col_m2:
        st.metric("En Espera", len(st.session_state.lista_adoptante))
    
    st.write("---")
    st.markdown("### 📞 Contacto")
    st.caption("📧 contacto@refugiovintage.org")
    st.caption("📞 +54 11 4433-2211")
    st.caption("📍 Av. Pet Friendly 1812")

# ---------------------------------------------------------
# ENCABEZADO SUPERIOR Y MENÚ DE NAVEGACIÓN HORIZONTAL
# ---------------------------------------------------------
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    st.markdown("### 🐶🐱")
with col_titulo:
    st.title("Sistema de Gestión del Refugio")

# Menú horizontal principal usando st.tabs
menu_opciones = [
    "📜 Padrón Completo",
    "✨ Aptos para Adopción",
    "➕ Registrar Mascota",
    "💉 Aplicar Vacunas",
    "👥 Gestión de Adoptantes",
    "📞 Contacto"
]

tabs = st.tabs(menu_opciones)

# ---------------------------------------------------------
# OPCIÓN 1: VER PADRÓN COMPLETO
# ---------------------------------------------------------
with tabs[0]:
    st.header("Padrón de Mascotas")
    if not st.session_state.padron_mascotas:
        st.info("El padrón del refugio se encuentra actualmente vacío.")
    else:
        st.markdown("---")
        # Mostramos como tabla estructurada sin usar pandas
        encabezado_col1, encabezado_col2, encabezado_col3 = st.columns(3)
        encabezado_col1.markdown("**Nombre**")
        encabezado_col2.markdown("**Especie**")
        encabezado_col3.markdown("**Vacunas Aplicadas**")
        st.divider()

        for mascota, datos in st.session_state.padron_mascotas.items():
            c1, c2, c3 = st.columns(3)
            c1.write(mascota)
            c2.write(datos["especie"].capitalize())
            c3.write(str(datos["vacunas_cant"]))

# ---------------------------------------------------------
# OPCIÓN 2: REPORTE DE APTOS PARA ADOPCIÓN
# ---------------------------------------------------------
with tabs[1]:
    st.header("Mascotas Aptas para Adopción Inmediata")
    if not st.session_state.padron_mascotas:
        st.info("El padrón se encuentra actualmente vacío.")
    else:
        aptos_encontrados = 0
        st.markdown("---")
        
        for mascota, datos in st.session_state.padron_mascotas.items():
            vacunas = datos["vacunas_cant"]
            if vacunas >= 3:
                especie = datos["especie"]
                st.success(f"🐾 **Apto:** {mascota} | **Especie:** {especie.capitalize()} | **Vacunas:** {vacunas}")
                aptos_encontrados += 1

        if aptos_encontrados == 0:
            st.warning("Actualmente no hay mascotas en el refugio con 3 o más vacunas aplicadas.")

# ---------------------------------------------------------
# OPCIÓN 3: REGISTRAR NUEVA MASCOTA
# ---------------------------------------------------------
with tabs[2]:
    st.header("Registrar Nueva Mascota")
    with st.form("form_registro_mascota"):
        nombre_mascota = st.text_input("Nombre de la mascota:")
        especie = st.text_input("Especie de la mascota:")
        submit_registro = st.form_submit_button("Registrar Mascota")

    if submit_registro:
        if nombre_mascota.strip() and especie.strip():
            registrar_mascota(nombre_mascota.strip(), especie.strip())
            st.success(f"¡Mascota **{nombre_mascota}** registrada con éxito!")
            st.rerun()
        else:
            st.error("Por favor, completa todos los campos antes de registrar.")

# ---------------------------------------------------------
# OPCIÓN 4: APLICAR VACUNA A MASCOTA
# ---------------------------------------------------------
with tabs[3]:
    st.header("Aplicar Vacunas")
    if not st.session_state.padron_mascotas:
        st.info("No hay mascotas registradas para vacunar.")
    else:
        lista_nombres = list(st.session_state.padron_mascotas.keys())
        nombre_mascota = st.selectbox("Seleccione la mascota a vacunar:", lista_nombres)
        vacunas_cant = st.number_input("¿Cuántas vacunas tiene/se aplican a la mascota?", min_value=1, step=1, value=1)
        
        if st.button("Aplicar Vacuna"):
            if aplicar_vacuna(nombre_mascota, int(vacunas_cant)):
                st.success(f"Se agregaron {vacunas_cant} vacuna(s) a **{nombre_mascota}**.")
                st.rerun()

# ---------------------------------------------------------
# OPCIÓN 5: GESTIÓN DE ADOPTANTES (Agregar, Atender, Remover)
# ---------------------------------------------------------
with tabs[4]:
    st.header("Gestión de Lista de Espera de Adoptantes")
    
    col_izq, col_der = st.columns(2)
    
    # Agregar adoptante
    with col_izq:
        st.subheader("1. Agregar a Lista de Espera")
        nombre_adoptante = st.text_input("Nombre del adoptante:")
        if st.button("Agregar a Espera"):
            if nombre_adoptante.strip():
                exito, mensaje = agregar_a_espera_adopcion(nombre_adoptante.strip())
                if exito:
                    st.success(mensaje)
                    st.rerun()
                else:
                    st.warning(mensaje)
            else:
                st.error("Por favor ingrese un nombre válido.")

    # Atender o remover adoptantes
    with col_der:
        st.subheader("2. Atender Siguiente Adoptante")
        if st.button("Atender Siguiente"):
            adoptante_atendido = atender_siguiente_adoptante()
            if adoptante_atendido:
                st.success(f"Atendiendo a **{adoptante_atendido}**")
                st.info("Se realizará la entrevista y la asignación al adoptante.")
                st.rerun()
            else:
                st.info("La lista de espera se encuentra vacía.")

        st.write("---")
        st.subheader("3. Remover de Lista de Espera")
        nombre_remover = st.text_input("Nombre del adoptante a remover:")
        if st.button("Remover Adoptante"):
            if remover_de_espera_adopcion(nombre_remover.strip()):
                st.success("El adoptante fue eliminado de la lista de espera.")
                st.rerun()
            else:
                st.error("El adoptante no se encuentra en la lista de espera.")

    # Mostrar cola actual
    st.write("---")
    st.subheader("📋 Lista de Espera Actual")
    if st.session_state.lista_adoptante:
        for idx, nombre in enumerate(st.session_state.lista_adoptante, start=1):
            st.write(f"**{idx}.** {nombre}")
    else:
        st.caption("No hay adoptantes en espera actualmente.")

# ---------------------------------------------------------
# OPCIÓN 6: CONTACTO
# ---------------------------------------------------------
with tabs[5]:
    st.header("Información de Contacto")
    st.markdown("""
    * **Organización:** Cuidado Animal & Mascotas - Refugio Vintage
    * **Teléfono:** +54 11 4433-2211
    * **Email:** contacto@refugiovintage.org
    * **Horario de Atención:** Lunes a Sábados de 09:00 a 18:00 hs.
    """)