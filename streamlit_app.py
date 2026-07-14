import streamlit as st
import time

st.set_page_config(page_title="H.C.E. | Executive Audit 2026", layout="centered")

st.markdown("""
<style>
    .stApp {background: #050505; color: #e0e0e0; font-family: 'Helvetica Neue', sans-serif;}
    h1 {color: #ff3e3e; text-transform: uppercase; letter-spacing: -2px;}
    .stForm {background: #0a0a0a; border: 1px solid #333; padding: 2.5rem; border-radius: 0px;}
    .stButton>button {background: #fff; color: #000; width: 100%; border-radius: 0px; font-weight: 900;}
</style>
""", unsafe_allow_html=True)

st.title("// EXECUTIVE ASSET AUDIT")
st.markdown("---")

with st.form("audit_avanzato"):
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Ruolo:", ["Operaio", "Programmatore", "Manager", "Venditore", "Creativo", "Consulente", "Altro"])
        income = st.select_slider("Reddito Annuo (k€):", options=[15, 25, 40, 60, 90, 150, 250])
        stability = st.slider("Stabilità Finanziaria (1-10):", 1, 10)
        ai_dep = st.slider("Dipendenza da AI (1-10):", 1, 10)
    with col2:
        ambition = st.slider("Ambizione (1-10):", 1, 10)
        replaceable = st.slider("Indice di Insostituibilità (1-10):", 1, 10)
        upskilling = st.slider("Investimento in Formazione (€/anno):", 0, 5000, 500)
        work_pace = st.select_slider("Ritmo di Lavoro:", ["Burocratico", "Sostenibile", "Competitivo"])

    submit = st.form_submit_button("GENERA PROIEZIONE DI VALORE")

if submit:
    with st.spinner('Calcolo del decadimento del capitale umano...'):
        time.sleep(3)
        
        # Logica "spietata"
        risk = (11 - replaceable) * 7 + (ai_dep * 5) - (upskilling / 1000)
        future_val = income * (1 + (ambition/20)) * (1 - (risk/200))
        
        st.metric("Indice di Rischio Sistemic", f"{int(risk)}%")
        st.metric("Proiezione Valore a 5 anni", f"{int(future_val * 5)}k€")
        
        st.write("---")
        st.markdown(f"**Analisi:** Il tuo profilo come {role} mostra un segnale di allerta.")
        st.error("Il tuo attuale investimento in upskilling ({upskilling}€) è insufficiente rispetto al tuo indice di sostituibilità.")
        
        st.link_button("SCARICA IL PIANO DI RIFORMA E MITIGAZIONE (9.99€)", "LINK_STRIPE")
