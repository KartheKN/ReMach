Automated Report Generation using an In-House LLM

Overview
ReMach is a locally hosted Large Language Model (LLM)-powered report generator that processes Excel files to extract insights. It is designed for organizations that require AI-driven data analysis without relying on external APIs, ensuring data privacy and security.

Features
✅ In-House LLM – Runs on Ollama, eliminating cloud dependency
✅ FastAPI Backend – Efficient API for processing user queries
✅ Streamlit UI – Simple web-based interface for file uploads & reports
✅ Excel Processing – Uses Pandas & OpenPyXL for handling structured data
✅ Lightweight & Scalable – Works on minimal computational resources

How It Works
Upload an Excel File 📂 (Containing structured data & questions)

FastAPI processes the file 📊 (Extracts tabular data & queries)

Ollama LLM generates insights 💡 (Based on the extracted data)

Download the generated report 📜 (With AI-driven answers)

Tech Stack
Backend: FastAPI

Frontend: Streamlit

LLM Framework: Ollama (Locally hosted DeepSeek model)

Data Processing: Pandas, OpenPyXL

Deployment: Self-hosted on internal infrastructure

Installation & Setup
Prerequisites
Ensure you have the following installed:
🔹 Python 3.9+
🔹 Ollama (for local LLM hosting) – Install from Ollama’s official site
🔹 Virtual Environment (Recommended)
