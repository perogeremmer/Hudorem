import mysql.connector

class Migration:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def run_migration(self):
        print("Running migration for database at", self.connection.database)

    def create_table(self, table_name, columns):
        create_table_query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Table", table_name, "created successfully")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
