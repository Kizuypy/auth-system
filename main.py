from services.user_service import UserService
from services.auth_service import AuthService


def logged_area(user):
    while True:
        print(f"\n=== Área Logada - Olá, {user.username}! ===")
        print("[1] Ver meus dados")
        print("[2] Sair")

        option = input("Escolha: ")

        if option == "1":
            print(f"\nUsername: {user.username}")
            print(f"Email: {user.email}")
            print(f"Conta criada em: {user.created_at}")

        elif option == "2":
            print("Saindo da conta...")
            break


def main():
    user_service = UserService()
    auth_service = AuthService()

    while True:
        print("\n=== Sistema de Login ===")
        print("[1] Cadastrar")
        print("[2] Login")
        print("[3] Sair")

        option = input("Escolha: ")

        if option == "1":
            username = input("Username: ")
            email = input("Email: ")
            senha = input("Senha: ")
            user_service.register(username, email, senha)

        elif option == "2":
            for tentativa in range(3):
                email = input("Email: ")
                senha = input("Senha: ")
                user = auth_service.login(email, senha, user_service)

                if user:
                    logged_area(user)
                    break
                else:
                    restante = 2 - tentativa
                    if restante > 0:
                        print(f"Tentativas restantes: {restante}")
            else:
                print("Conta bloqueada! Muitas tentativas.")

        elif option == "3":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()
