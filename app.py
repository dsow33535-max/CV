import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV Diarry SOW", layout="wide")

# Application du style CSS pour le fond beige et la mise en forme
st.markdown("""
    <style>
    .main {
        background-color: #F5F5DC; /* Couleur Beige */
    }
    .sidebar .sidebar-content {
        background-color: #2C3E50;
        color: white;
    }
    h1, h2, h3 {
        color: #2C3E50;
    }
    .stProgress > div > div > div > div {
        background-color: #2C3E50;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150) # Remplacez par le chemin de votre photo
    st.title("DIARRY SOW")
    st.markdown("---")
    
    st.subheader("Informations personnelles")
    st.write("📧 diarrysow748@gmail.com")
    st.write("📞 +221 77 748 22 75")
    st.write("📍 MARISTE 2, 22234 DAKAR")
    st.write("🎂 7 Mars 2002")
    st.write("🇸🇳 Sénégalaise")
    st.write("💍 Mariée")

    st.markdown("---")
    st.subheader("Langues")
    st.write("Français")
    st.progress(0.9)
    st.write("Anglais")
    st.progress(0.4)

# --- COLONNE PRINCIPALE ---
st.title("Curriculum Vitae")

# Section Formation
st.header("🎓 Formation")
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("**DIPLÔMÉE EN SECRÉTARIAT BUREAUTIQUE**")
    st.caption("CENTRE DIAPALATE, KAOLACK")
    
    st.markdown("**LICENCE 1 BIOLOGIE**")
    st.caption("UCAD, DAKAR")
    
    st.markdown("**BAC**")
    st.caption("LYCÉE MIXTE NGANE SAER, KAOLACK")
with col2:
    st.write("juil. 2023 - déc. 2023")
    st.write("janv. 2023 - juin 2023")
    st.write("oct. 2021 - juil. 2022")

st.markdown("---")

# Section Expérience Professionnelle
st.header("💼 Expérience professionnelle")

exp1_col1, exp1_col2 = st.columns([3, 1])
with exp1_col1:
    st.markdown("**AGENT DACS**")
    st.write("COUD, DAKAR")
with exp1_col2:
    st.write("nov. 2024 - à ce jour")

exp2_col1, exp2_col2 = st.columns([3, 1])
with exp2_col1:
    st.markdown("**RESPONSABLE COMMERCIALE**")
    st.write("DIAMONO GAZ, KAOLACK")
with exp2_col2:
    st.write("févr. 2023 - oct. 2024")

st.markdown("---")

# Section Compétences
st.header("🛠️ Compétences")
c1, c2 = st.columns(2)
with c1:
    st.write("Tenue des dossiers administratifs")
    st.write("Préparation des entretiens")
with c2:
    st.write("Gestion du personnel")
    st.write("Élaborer le planning du personnel")

st.markdown("---")

# Section Activités Extra-scolaires
st.header("🌟 Activités extra-scolaires")
st.markdown("- **Membre de l'Amicale des élèves et étudiants ressortissants de Kaolack** (Depuis 2022)")
st.markdown("- **Secrétaire Générale de MEEF** (Depuis 2024)")
