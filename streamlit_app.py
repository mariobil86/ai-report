import streamlit as st
import plotly.graph_objects as go
from logic import calcola_audit

# Configurazione Dashboard
st.set_page_config(page_title="H.C.E. | CORE", layout="wide")

st.markdown("""<style>.stApp {background: #000; color: #fff;} .css-1q8dd3e {background: #111;}</style>""", unsafe_allow_html=True)

st.title("// SYSTEM DIAGNOSTICS: RUNNING")

with st.sidebar:
    st.header("INPUT PARAMETERS")
    data = {
        'income': st.select_slider("Income (k€):", [15, 25, 40, 60, 90, 150, 250]),
        'ai_dep': st.slider("AI Dependency (1-10):", 1, 10),
        'replaceable': st.slider("Replaceability (1-10):", 1, 10),
        'ambition': st.slider("Ambition (1-10):", 1, 10),
        'upskilling': st.slider("Formazione (€):", 0, 5000, 500)
    }
    submit = st.button("EXECUTE AUDIT")

if submit:
    res = calcola_audit(data)
    
    # Visualizzazione "Radar" (Estrema precisione)
    fig = go.Figure(data=go.Scatterpolar(
      r=[data['ai_dep'], data['replaceable'], data['ambition'], (data['upskilling']/500)],
      theta=['AI DEP', 'REPLACE', 'AMBITION', 'UPKILL'],
      fill='toself', line_color='#ff3e3e'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False, paper_bgcolor='black', font_color='white')
    
    c1, c2 = st.columns(2)
    c1.plotly_chart(fig)
    c2.metric("SYSTEM STATUS", res['status'])
    c2.metric("RISK INDEX", f"{res['rischio']}%")
    
    st.write("---")
    st.warning("⚠️ PROFILO A RISCHIO DI OBSOLESCENZA. ACQUISISCI IL REPORT TECNICO PER LA MITIGAZIONE.")
    st.link_button("PURCHASE STRATEGIC REPORT (9.99€)", "INSERISCI_TUO_LINK_STRIPE")
