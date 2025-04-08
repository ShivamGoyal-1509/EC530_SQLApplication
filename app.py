import sqlite3
from csv_loader import load_csv_to_sqlite
from db_utils import list_tables, get_table_schema
from llm_sql_agent import generate_sql
from config import DB_PATH

def print_menu():
    print("\nOptions:")
    print("1. Load CSV")
    print("2. List Tables")
    print("3. Ask a Question (chat)")
    print("4. Exit")

def main():
    print("📊 ChatSheet — Talk to Your Data")
    while True:
        print_menu()
        choice = input("Choose: ").strip()
        if choice == '1':
            path = input("Path to CSV: ")
            table = input("Table name: ")
            load_csv_to_sqlite(path, table, DB_PATH)
        elif choice == '2':
            with sqlite3.connect(DB_PATH) as conn:
                tables = list_tables(conn)
                print("📋 Tables:", tables)
        elif choice == '3':
            question = input("🧠 Your question: ")
            with sqlite3.connect(DB_PATH) as conn:
                schema = ""
                for table in list_tables(conn):
                    cols = get_table_schema(conn, table)
                    schema += f"- {table} (" + ", ".join(f"{c[0]} {c[1]}" for c in cols) + ")\n"
                sql, full_response = generate_sql(schema, question)
                print("📄 SQL Generated:\n", sql)
                try:
                    result = conn.execute(sql).fetchall()
                    print("📊 Result:", result)
                except Exception as e:
                    print("❌ Error running SQL:", e)
        elif choice == '4':
            break

if __name__ == "__main__":
    main()