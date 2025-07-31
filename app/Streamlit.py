import streamlit as st

st.set_page_config(
    page_title="StudyCode",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<div style="
    max-width: 600px;
    margin: 40px auto;
    background: rgba(255, 255, 255, 0.9);
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    color: #000;
">
    <p style="font-size: 22px; font-weight: bold; margin-bottom: 10px;">
        🐍 <strong>StudyCode</strong> - Desenvolvido pelo Thiago Ferreira
    </p>
    <p style="font-size: 16px;">
        Organize seus estudos, acompanhe seu progresso e alcance seus objetivos!
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader("✏️ O que você quer estudar hoje?")
estudo = st.text_input("Digite sua meta de estudo:")

if estudo:
    st.success(f"📚 Boa! Sua meta de hoje é: **{estudo}**")
