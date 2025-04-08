import os
import pandas as pd
import sqlite3
from db_utils import table_exists, get_table_schema

def load_csv_to_sqlite(csv_path, table_name, db_path):
    try:
        # Show a quick preview of the file
        print(f"🧾 Previewing first few lines of {csv_path}...")
        with open(csv_path, 'r', encoding='latin1') as f:
            for _ in range(5):
                print(f.readline().strip())

        # Try reading CSV with default comma delimiter
        df = pd.read_csv(csv_path, encoding='latin1')  # You can add `delimiter=';'` if needed

        with sqlite3.connect(db_path) as conn:
            if table_exists(conn, table_name):
                existing_schema = get_table_schema(conn, table_name)
                print(f"⚠️ Table '{table_name}' already exists with schema: {existing_schema}")
                choice = input("Overwrite (o), Rename (r), or Skip (s)? ").lower()
                if choice == 's':
                    return
                elif choice == 'r':
                    table_name += "_new"
            df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"✅ Loaded {len(df)} records into '{table_name}'")

    except pd.errors.ParserError as pe:
        print("❌ CSV formatting issue:", pe)
        log_error(pe)

    except Exception as e:
        print("❌ Error loading CSV:", e)
        log_error(e)

def log_error(error):
    os.makedirs("logs", exist_ok=True)
    with open("logs/error_log.txt", "a") as f:
        f.write(str(error) + "\n")