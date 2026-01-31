import streamlit as st
from extractor import extract_text
from clause_splitter import split_clauses
from risk_engine import assess_risk
from llm_reasoner import explain_clause

st.set_page_config(page_title="GenAI Legal Assistant")

st.title("GenAI-Powered Legal Assistant for SMEs")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    clauses = split_clauses(text)
    risky = assess_risk(clauses)

    st.subheader("Overall Risk")
    st.write("HIGH" if risky else "LOW")

    st.subheader("Risky Clauses")

    for clause in risky:
        st.markdown(f"### {clause['id']} ({clause['risk']})")
        st.write(clause["text"])

        if st.button(f"Explain {clause['id']}"):
            explanation = explain_clause(clause["text"])
            st.info(explanation)
