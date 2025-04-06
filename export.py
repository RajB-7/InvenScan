from io import StringIO
import app
import google.generativeai as genai
import pandas as pd
import sqlite3

genai.configure(api_key="AIzaSyBKk-KmNIc4TARf-ttK8AnHWY1FenxQ-P0")

prompt = f"""
Extract a table of items from this receipt. Include SKUID, product name, quantity, unit price, and total.

Receipt:
{app.ocr_text}
"""
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(prompt)

print("=== RAW GEMINI RESPONSE ===")
print(response.text)
print("===========================")

lines = response.text.strip().split("\n")
data = []

for line in lines:
    if set(line.strip()) <= {"|", "-", " "}:
        continue
    row = [cell.strip() for cell in line.strip().split("|") if cell.strip()]
    if len(row) == 5:
        data.append(row)

df = pd.DataFrame(data[1:], columns=data[0])

conn = sqlite3.connect("products.db")
df.to_sql("products", conn, if_exists="append", index=False)
conn.close()
print("Data saved to database.")
