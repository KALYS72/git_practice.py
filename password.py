CEND = '\033[0m'
CBLUE = '\33[34m'
CRED = '\033[31m'
CGREEN = '\33[32m'

password = ''

while len(password) < 8 or not password.isdigit():
    password = input(CBLUE + 'Введите ваш пароль: ' + CEND)
    
    if len(password) < 8:
        print(CRED + 'Ваш пароль должен содержать не менее 8 символов' + CEND)
    if not password.isdigit():
        print(CRED + 'Ваш пароль должен хранить только числа' + CEND)

print(CGREEN + 'Ваш пароль сохранен' + CEND)