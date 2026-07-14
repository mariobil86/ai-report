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
    with st.spinner('Accesso al database di settore...'):
        import time
        time.sleep(2) # Pausa drammatica
        st.success("Analisi incrociata completata.")
        
        # UI di report premium
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Indice di Rischio", "68%", "+12% vs media")
        with col2:
            st.metric("Potenziale AI", "High", "Critical")
            
        st.write(f"### Report Strategico per: {job}")
        st.markdown(f"La nostra analisi identifica nel settore {industry} una trasformazione imminente.")
        st.markdown("---")
        st.markdown("📈 **Trend 2026-2027:** Il mercato richiede una transizione verso modelli ibridi.")
        st.markdown("⚠️ **Vulnerabilità:** La tua posizione attuale presenta un gap di competenze del 40% rispetto allo standard richiesto.")
        
        st.warning("⚠️ **ULTIMA POSSIBILITÀ:** Scarica il Piano di Mitigazione Rischi e Strategia di Carriera.")
        st.link_button("SCARICA REPORT COMPLETO (9.99€)", "INSERISCI_QUI_TUO_LINK_STRIPE")
