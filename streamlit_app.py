import streamlit as st
import time

st.set_page_config(page_title="AI Human Capital Engine", layout="wide")

# Styling Premium
st.markdown("""<style>
    .stButton>button {width: 100%; border-radius: 0px; background-color: #000; color: #fff;}
    .css-1544g2n {padding: 2rem; border: 1px solid #333;}
</style>""", unsafe_allow_html=True)

st.title("🌐 AI Human Capital Engine")
st.subheader("Analisi diagnostica profonda del posizionamento professionale 2026")

# Database Professioni esaustivo
professioni = [
    "Operaio Specializzato", "Operaio Generico", "Impiegato Amministrativo", 
    "Programmatore / Software Engineer", "Marketing Manager", "Commercialista", 
    "Avvocato", "HR Specialist", "Graphic Designer", "Project Manager", 
    "Data Analyst", "Venditore / Sales", "Cuoco / Chef", "Autista", 
    "Logistica", "Ingegnere", "Libero Professionista", "Altro"
]

with st.form("analisi_profonda"):
    col1, col2 = st.columns(2)
    with col1:
        job = st.selectbox("Professione:", professioni)
        remote = st.radio("Preferenza operativa:", ["Lavoro in Sede", "Smart Working", "Ibrido"])
    with col2:
        mobility = st.radio("Disponibilità al trasferimento:", ["Radicato nel territorio", "Disposto a trasferta", "Disponibile a relocate estero"])
        ambition = st.select_slider("Livello di ambizione (1-10):", options=[1,2,3,4,5,6,7,8,9,10])
    
    submit = st.form_submit_button("GENERA DIAGNOSI PSICO-PROFESSIONALE")

if submit:
    with st.spinner('Scansione neuro-lavorativa in corso...'):
        time.sleep(3)
        
        # Logica di "Cervello" avanzata
        st.write("---")
        st.write(f"### Analisi di Profilo: {job}")
        
        # Simulazione di profondità
        st.metric("Indice di Adattabilità", f"{70 + ambition}%")
        
        st.info(f"Il tuo profilo ('{remote}' + '{mobility}') indica una curva di apprendimento accelerata rispetto alla media di settore.")
        
        st.markdown("""
        **Analisi Psicografica:**
        La tua propensione alla mobilità ed il livello di ambizione indicato (livello {0}/10) ci permettono di mappare un rischio di obsolescenza professionale estremamente ridotto, a patto di una riconversione verso sistemi ibridi uomo-macchina.
        """.format(ambition))
        
        st.warning("⚠️ ATTENZIONE: Il tuo potenziale è attualmente sotto-utilizzato. Per sbloccare la strategia di carriera personalizzata basata sui tuoi dati:")
        st.link_button("OTTENERE PIANO DI MITIGAZIONE RISCHI (9.99€)", "INSERISCI_TUO_LINK_STRIPE")
