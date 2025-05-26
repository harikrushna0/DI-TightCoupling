# database_di.py (120 lines)
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def execute_query(self, query, params=None):
        pass

class PostgreSQLDatabase(Database):
    def __init__(self, dbname, user, password, host):
        import psycopg2
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        return cursor

# DI: Abstract class allows swapping databases (e.g., SQLite, MySQL).

class UserService:
    def __init__(self, db: Database):
        self.db = db

    def get_user(self, user_id):
        cursor = self.db.execute_query("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()

# Decoupled: DB implementation can change without modifying UserService.
