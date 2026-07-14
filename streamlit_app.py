import streamlit as st
import time

# Configurazione estetica stile Meta
st.set_page_config(page_title="Human Capital | Diagnostics", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    html, body, [class*="css"] {font-family: 'Inter', sans-serif;}
    .stApp {background-color: #000000;}
    h1 {color: #ffffff !important; font-weight: 600; text-align: center; margin-bottom: 2rem;}
    .stForm {background-color: #111111; padding: 2rem; border-radius: 12px; border: 1px solid #333;}
    .stButton>button {width: 100%; border-radius: 8px; background-color: #ffffff; color: #000; font-weight: 600; border: none; padding: 0.8rem;}
    .stMetric {background: #1a1a1a; padding: 1rem; border-radius: 8px;}
</style>
""", unsafe_allow_html=True)

st.title("Human Capital Engine")

with st.form("engine"):
    col1, col2 = st.columns(2)
    with col1:
        job = st.selectbox("Current Role", ["Software Engineer", "Operations", "Creative Director", "Operations Specialist", "Other"])
        remote = st.selectbox("Work Preference", ["In-Office", "Hybrid", "Remote"])
    with col2:
        ambition = st.select_slider("Ambition Level", options=["Steady", "Aggressive", "Hyper-Growth"])
        risk = st.radio("Financial Stability", ["High", "Medium", "Low"])
    
    submit = st.form_submit_button("RUN DIAGNOSTICS")

if submit:
    with st.spinner('Computing matrix...'):
        time.sleep(2)
        # Visualizzazione pulita
        c1, c2 = st.columns(2)
        c1.metric("Adaptability Score", "84%")
        c2.metric("Market Volatility", "Low")
        
        st.divider()
        st.markdown("### Executive Summary")
        st.write(f"Your profile as {job} shows high alignment with current market trends in the {remote} sector.")
        
        st.warning("To unlock the full technical diagnostic and the custom mitigation roadmap:")
        st.link_button("ACCESS FULL REPORT (9.99€)", "INSERISCI_TUA_URL_STRIPE")
