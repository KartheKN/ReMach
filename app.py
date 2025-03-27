import streamlit as st
import requests
import pandas as pd

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/process-excel/"

st.title("📊 LLM-Powered Report Generator")

# File Upload
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    st.write("✅ File uploaded successfully!")

    # Send file to FastAPI backend
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(BACKEND_URL, files=files)
    
    if response.status_code == 200:
        report_data = response.json()["report"]
        
        # Convert to DataFrame for better visualization
        report_df = pd.DataFrame(report_data)
        st.write("### 📝 Generated Report")
        st.dataframe(report_df)

        # Download button for report
        csv = report_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download Report as CSV", data=csv, file_name="report.csv", mime="text/csv")

    else:
        st.error("❌ Error processing the file!")