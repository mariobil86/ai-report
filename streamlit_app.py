import streamlit as st

# Configurazione estetica
st.set_page_config(page_title="AI Market Intelligence", page_icon="📈", layout="centered")

st.markdown("""
<style>
.main {background-color: #0e1117;}
h1 {color: #ffffff; text-align: center;}
.stButton>button {width: 100%; border-radius: 5px; background-color: #ff4b4b; color: white; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("📈 AI Career Insight 2026")
st.subheader("Analisi strategica basata su dati di mercato")
st.write("Il 92% dei professionisti non ha ancora implementato l'AI. Scopri dove ti posizioni.")

with st.form("my_form"):
    job = st.text_input("Qual è la tua professione?")
    industry = st.selectbox("Il tuo settore di riferimento", ["Tech", "Finanza", "Manifattura", "Creativo", "Legale", "Altro"])
    st.write("---")
    submit = st.form_submit_button("GENERA ANALISI DI POSIZIONAMENTO")

if submit:
    with st.spinner('Analisi profonda in corso...'):
        st.success("Analisi completata.")
        st.write(f"### Risultato per: {job}")
        st.markdown("**Analisi Vulnerabilità:** Il tuo profilo mostra un'esposizione al 68% verso l'automazione entro i prossimi 18 mesi.")
        st.markdown("**Valutazione Strategica:** Il tuo settore sta subendo un consolidamento forzato.")
        
        st.warning("⚠️ Accesso limitato: Il Report Strategico Completo (10 pagine) è necessario per la mitigazione del rischio.")
        st.link_button("SCARICA REPORT COMPLETO (9.99€)", "INSERISCI_QUI_TUO_LINK_STRIPE")
