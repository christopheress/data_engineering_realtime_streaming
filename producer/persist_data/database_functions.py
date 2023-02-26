import psycopg2


class Database:
    def __init__(self, host, port, user, password, database):
        self.connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """
        Creates a table with the specified name and columns.
        Columns are expected to be a dictionary with the column name as the key and the column type as the value.
        """
        column_str = ", ".join(f"{name} {datatype}" for name, datatype in columns.items())
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str});"
        self.cursor.execute(sql)
        self.connection.commit()

    def insert(self, table_name, data):
        """
        Inserts a row into the specified table.
        """
        column_str = ", ".join(data.keys())
        value_str = ", ".join(f"'{value}'" for value in data.values())
        sql = f"INSERT INTO {table_name} ({column_str}) VALUES ({value_str});"
        self.cursor.execute(sql)
        self.connection.commit()

    def select(self, table_name, columns=None):
        """
        Selects rows from the specified table.
        """
        if columns:
            column_str = ", ".join(columns)
        else:
            column_str = "*"
        sql = f"SELECT {column_str} FROM {table_name};"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def update(self, table_name, data, conditions):
        """
        Updates rows in the specified table.
        Data is expected to be a dictionary with the column name as the key and the new value as the value.
        Conditions is expected to be a dictionary with the column name as the key and the condition as the value.
        """
        set_str = ", ".join(f"{key}='{value}'" for key, value in data.items())
        where_str = " AND ".join(f"{key}='{value}'" for key, value in conditions.items())
        sql = f"UPDATE {table_name} SET {set_str} WHERE {where_str};"
        self.cursor.execute(sql)
        self.connection.commit()
