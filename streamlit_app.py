import streamlit as st
from logic import calcola_audit

st.set_page_config(page_title="H.C.E. | System", layout="centered")

# Importiamo la logica separata
st.title("// EXECUTIVE ASSET AUDIT")

with st.form("main_form"):
    # Qui lasciamo il form, ma i dati andranno in un dizionario
    col1, col2 = st.columns(2)
    with col1:
        data = {}
        data['income'] = st.select_slider("Reddito (k€):", [15, 25, 40, 60, 90, 150])
        data['ai_dep'] = st.slider("Dipendenza AI (1-10):", 1, 10)
    with col2:
        data['replaceable'] = st.slider("Insostituibilità (1-10):", 1, 10)
        data['ambition'] = st.slider("Ambizione (1-10):", 1, 10)
        data['upskilling'] = st.slider("Investimento (€):", 0, 5000, 500)

    submit = st.form_submit_button("GENERA AUDIT")

if submit:
    risultati = calcola_audit(data)
    st.metric("Indice di Rischio", f"{risultati['rischio']}%")
    st.metric("Valore a 5 anni", f"{risultati['valore_futuro']}k€")
