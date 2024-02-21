import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def fetch_data(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

# Example usage:
if __name__ == "__main__":
    db_manager = DatabaseManager("example.db")
    db_manager.connect()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """
    db_manager.execute_query(create_table_query)

    insert_data_query = """
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com')
    """
    db_manager.execute_query(insert_data_query)

    select_data_query = "SELECT * FROM users"
    data = db_manager.fetch_data(select_data_query)
    print("Data from database:")
    for row in data:
        print(row)

    db_manager.disconnect()
