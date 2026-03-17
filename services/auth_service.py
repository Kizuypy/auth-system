import hashlib
import os


class AuthService:
    def hash_password(self, password):
        salt = os.urandom(32)  # 32 bytes aleatórios!
        pwd_hash = hashlib.sha256(salt + password.encode()).hexdigest()

        return pwd_hash, salt.hex()

    def verify_password(self, password, password_hash, salt):
        salt_bytes = bytes.fromhex(salt)
        pwd_hash = hashlib.sha256(salt_bytes + password.encode()).hexdigest()
        return pwd_hash == password_hash


    def login(self, email, password, user_service):
        user = user_service.get_user_by_email(email)

        if not user:
            print("Email não encontrado.")
            return None
        
        if self.verify_password(password, user.password_hash, user.salt):
            print(f"Bem-vindo, {user.username}!")
            return user
        
        print("Senha incorreta!")
        return None

# os.urandom (32) - gera 32 bytes completamentes aleatórios.
# .encode() - Converte a senha de string para bytes (sha256 só aceita bytes)
# salt - mistura o salt com a senha antes de fazer o hash (salt = sal)
# hexdigest() - converte o hash pra string legivel 
# hex - converte salt para string pra poder salvar no SQLite
# bytes.fromhex(salt) - na verificação, converte de volta pra bytes pra refazer o hash

