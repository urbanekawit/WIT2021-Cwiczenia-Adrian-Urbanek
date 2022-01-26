users = {'Admin':'1234'}
user_authenticated = False
while not user_authenticated:
    login = input('Podaj login: ')
    password = input('Podaj haslo: ')
    if users.get(login):
        if users[login]==password:
            user_authenticated=True
            print("Logowanie poprawne")
        else:
            print("Logowanie niepoprawne")