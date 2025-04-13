import streamlit as st
import json
import os

st.set_page_config(page_title="Code Quality Report", layout="wide")
st.title("📊 Python Code Quality Report Viewer")

uploaded_file = st.file_uploader("Upload report.json", type="json")

if uploaded_file:
    report = json.load(uploaded_file)

    st.subheader("📌 Summary")
    summary = report["summary"]
    st.metric(label="Files Analyzed", value=summary["files_analyzed"])
    st.metric(label="Overall Score", value=summary["overall_score"])

    st.divider()

    st.subheader("📄 File-wise Details")
    for detail in report["details"]:
        with st.expander(detail["filename"]):
            col1, col2, col3 = st.columns(3)
            col1.metric("Linter Issues", detail["linter_issues"])
            col2.metric("Complexity Score", round(detail["complexity_score"], 2))
            col3.metric("Total Score", round(detail["total_score"], 2))

            if detail["suggestions"]:
                st.markdown("**💡 Suggestions:**")
                for s in detail["suggestions"]:
                    st.markdown(f"- {s}")
