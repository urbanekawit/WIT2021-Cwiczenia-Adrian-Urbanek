user_authenticated = False
while not user_authenticated:
    login = input("Podaj login: ")
    password = input("Podaj hasło: ")
    if login == "Admin" and password == "1234":
        user_authenticated = True
print("Zalogowano")