# ChatSheet — Talk to Your Data via Chat

ChatSheet is a chat-based spreadsheet assistant built in Python.  
It lets you load CSV files, convert them into SQL tables, and ask natural language questions that get converted into SQL queries using OpenAI GPT.

---

##  Features

- Load CSV files into a local SQLite database
- Ask questions like “What are the top 5 cities?”
- Automatically generate SQL from plain English using GPT-3.5
- Preview CSVs before loading
- Stores results in a persistent database (`chatdata.db`)
- Error logging to `logs/error_log.txt`

---

##  Project Structure

project/
├── app.py                  # Main chat interface
├── csv_loader.py           # CSV-to-SQLite loader
├── db_utils.py             # Schema helpers
├── llm_sql_agent.py        # SQL generation via OpenAI
├── config.py               # API key & paths
├── requirements.txt
├── data/
│   └── sample.csv          # Example CSV
├── logs/
│   └── error_log.txt       # Runtime errors (auto-created)

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt

2. Set Your OpenAI API Key

Option A (recommended):

export OPENAI_API_KEY=your-api-key

Option B (quick test):
Edit config.py:

OPENAI_API_KEY = "your-api-key"

Get your key from: https://platform.openai.com/account/api-keys

⸻

How to Use

python app.py

You’ll see:

ChatSheet — Talk to Your Data

Options:
1. Load CSV
2. List Tables
3. Ask a Question (chat)
4. Exit



⸻

Sample Interaction

Step 1: Load a CSV

Choose: 1
Path to CSV: data/sample.csv
Table name: people

Step 2: Ask a question

Choose: 3
Your question: What are the cities with the most people?

You’ll see:
	•	Auto-generated SQL
	•	Query result from your SQLite DB

⸻

Sample CSV (data/sample.csv)

name,age,city
Alice,30,New York
Bob,25,Chicago
Charlie,35,Boston


⸻

Tips
	•	Supports multiple CSVs and tables
	•	Handles schema conflicts (rename/overwrite)
	•	Logs errors to logs/error_log.txt

⸻

Dependencies
	•	Python 3.8+
	•	openai
	•	pandas
	•	sqlite3 (standard lib)
	•	python-dotenv (optional)
