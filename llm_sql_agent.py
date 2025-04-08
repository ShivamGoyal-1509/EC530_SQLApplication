import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_sql(schema_text, user_query):
    prompt = f"""
You are an AI assistant that converts user questions into SQL for a SQLite database.

Schema:
{schema_text}

User Query: "{user_query}"

Respond with:
SQL Query:
Explanation:
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    text = response['choices'][0]['message']['content']
    sql = None
    if "SQL Query:" in text:
        sql = text.split("SQL Query:")[1].split("Explanation:")[0].strip()
    return sql, text