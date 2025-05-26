# database_tight.py (150 lines)
import psycopg2

class UserService:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="mydb", user="postgres", password="password", host="localhost"
        )

    def get_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()

    def create_user(self, name, email):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        self.connection.commit()

# Tight Coupling: Direct dependency on psycopg2 and hardcoded DB config.
# Vendor lock-in (PostgreSQL). Changes require modifying this class.

class OrderService:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="mydb", user="postgres", password="password", host="localhost"
        )

    def create_order(self, user_id, product):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO orders (user_id, product) VALUES (%s, %s)", (user_id, product))
        self.connection.commit()

# Duplicate DB connection logic. Tight coupling to PostgreSQL.
