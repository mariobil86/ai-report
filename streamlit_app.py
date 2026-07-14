import streamlit as st

st.set_page_config(page_title="THE JUDGEMENT", layout="centered")

st.markdown("<h1 style='text-align: center; color: #ff3e3e;'>// THE JUDGEMENT ENGINE //</h1>", unsafe_allow_html=True)
st.write("---")
st.write("Rispondi. La tua onestà determinerà la tua sentenza.")

with st.form("risposte"):
    q1 = st.text_area("1. Se dovessi eliminare il 90% delle tue attività quotidiane perché inutili, cosa resterebbe? Sii onesto: quanto della tua giornata è solo una recita per sentirti impegnato?")
    q2 = st.text_area("2. Quale bugia racconti a te stesso ogni mattina per convincerti che sei sulla strada giusta, nonostante i risultati dicano l'esatto opposto?")
    q3 = st.text_area("3. Se il tuo lavoro venisse sostituito da un algoritmo entro 12 mesi, cosa ti mancherebbe davvero: il lavoro, o la scusa che ti dà per non affrontare chi sei?")
    q4 = st.text_area("4. Cosa ti spaventa di più: fallire miseramente o scoprire che, anche se ci provassi al massimo, rimarresti comunque mediocre?")
    q5 = st.text_area("5. Se sapessi che nessuno ti giudicherà più domani, cosa inizieresti subito a fare? E perché, invece di farlo, preferisci continuare a vivere una vita che ti fa schifo?")
    
    submit = st.form_submit_button("SOTTOPONITI AL GIUDIZIO")

if submit:
    # Qui salviamo le risposte in un blocco di testo pronto per il copia-incolla
    risposte_totali = f"Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nQ5: {q5}"
    st.text_area("COPIA LE RISPOSTE PER IL GIUDICE:", risposte_totali, height=300)
    st.warning("Copia il testo sopra e incollalo nel tuo prompt AI.")
