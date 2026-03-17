def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False


def validate_password(password):
    if len(password) >= 8:
        return True
    return False

def validate_username(username):
    if len(username) > 3:
        return True
    return False


    