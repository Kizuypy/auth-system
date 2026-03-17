from database.db import Database
from models.user import User
from services.auth_service import AuthService
from utils.validators import validate_email, validate_password, validate_username
from datetime import datetime


class UserService:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.auth = AuthService()

    def register(self, username, email, password):
        if not validate_username(username):
            print("Username inválido! Mínimo 3 caracteres.")
            return False
        if not validate_email(email):
            print("Email inválido!")
            return False
        if not validate_password(password):
            print("Senha inválida! Mínimo 8 caracteres.")
            return False

        password_hash, salt = self.auth.hash_password(password)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO users(username, email, password_hash, salt, created_at)
                VALUES(?,?,?,?,?)
                """,
                (username, email, password_hash, salt, created_at),
            )
            self.conn.commit()
            print(f"Usuário '{username}' cadastrado com sucesso!")
            return True
        except Exception as e:
            print(f"erro ao cadastrar: {e}")
            return False

    def get_user_by_email(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()

        if row:
            return User(
                id=row[0],
                username=row[1],
                email=row[2],
                password_hash=row[3],
                salt=row[4],
                created_at=row[5],
            )
        return None
