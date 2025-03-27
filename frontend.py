import streamlit as st
import requests

# Streamlit UI
st.title("📊 ReMach - LLM Report Generator")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    st.write("📤 Uploading file...")

    # Send file to FastAPI backend
    files = {"file": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:8000/process-excel/", files=files)

    if response.status_code == 200:
        report = response.json()["report"]
        st.success("✅ Report Generated!")
        
        # Display Report
        for item in report:
            st.subheader(f"❓ {item['question']}")
            st.write(f"💡 **Answer:** {item['answer']}")
    else:
        st.error("❌ Failed to process the file. Check backend logs.")
