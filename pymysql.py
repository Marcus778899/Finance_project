import pymysql
from packages import secret

class mysql_import():
    def __init__(self,database) -> None:
        self.user = secret.user
        self.password = secret.password
        self.host = secret.host
        self.database = database

    def create_database(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            charset='utf8mb4'
        )
        
        try:
            with connection.cursor() as cursor:

                create_database_sql = f"CREATE DATABASE IF NOT EXISTS {self.database}"

                cursor.execute(create_database_sql)

                connection.commit()

                print("Database created successfully.")

        except Exception as e:
            print(f"Error creating database: {e}")

        finally:
            connection.close()

    def import_data(self,table):
        connection = pymysql.connect(
            host=secret.host,
            user=secret.user,
            password=secret.password,
            database=f'{self.database}',
            charset='utf8mb4'
        )

        try:
            with connection.cursor() as cursor:
                sql = f'CREATE TABLE IF NOT EXISTS {table}'   

        except Exception as e:
            print(f"Error importing data: {e}")

        finally:
            connection.close()

