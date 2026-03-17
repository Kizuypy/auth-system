class User:
    def __init__(self, username, email, password_hash, salt, created_at, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.salt = salt
        self.created_at = created_at

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"
