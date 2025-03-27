from fastapi import FastAPI, UploadFile, File
import pandas as pd
import ollama
import io

app = FastAPI()

@app.post("/process-excel/")
async def process_excel(file: UploadFile = File(...)):
    try:
        # Read the uploaded Excel file
        contents = await file.read()
        excel_data = pd.ExcelFile(io.BytesIO(contents))

        # Assuming first sheet contains tables, second contains questions
        table_df = excel_data.parse(sheet_name=excel_data.sheet_names[0])  
        questions_df = excel_data.parse(sheet_name=excel_data.sheet_names[1])

        # Convert table data to a string format for LLM
        table_text = table_df.to_string(index=False)
        
        # Process each question
        report = []
        for question in questions_df.iloc[:, 0]:  # Assuming questions are in first column
            prompt = f"Given the following table:\n\n{table_text}\n\nAnswer the question: {question}"
            
            # Query DeepSeek model via Ollama
            response = ollama.chat(model="deepseek-r1", messages=[{"role": "user", "content": prompt}])

            # Handle response properly
            answer = response.get("message", {}).get("content", "No response generated.")
            report.append({"question": question, "answer": answer})
        
        return {"report": report}

    except Exception as e:
        return {"error": str(e)}