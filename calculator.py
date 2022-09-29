"1"

# eval - функция, которая  принимает строку и выполняет её как код
code = input("Введите вычисление: ").replace(' ', '')






"my"

while True:
    CRED = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CEND = '\033[0m'
    s = input(CBLUE + '\nВыберите операцию из следующих: + - * / % ** //:  ' + CEND)
    if s in ('+', '-', '*', '/', '%', '**', '//'):
        x = float(input(CYELLOW + 'Введите первое число: '+ CEND))
        y = float(input(CYELLOW + 'Введите второе число: '+ CEND))
        if s == '+':
            print(CGREEN + f'{x}  +  {y}  =  {x + y}' + CEND)
        elif s == '-':
            print(CGREEN + f'{x}  -  {y}  =  {x - y}'  + CEND)
        elif s == '*':
            print(CGREEN + f'{x} *  {y}  =  {x * y}' + CEND)
        elif s == '**':
            print(CGREEN + f'{x}  **  {y}  =  {x ** y}' + CEND)
        elif s == '/' or s == '//' or s == '%':
            if y != 0 and s == '/':
                print(CGREEN + f'{x}  /  {y}  =  {x / y}' + CEND)
            elif y != 0 and s == '//':
                print(CGREEN + f'{x}  //  {y}  =  {x // y}'+ CEND)
            elif y != 0 and s == '%':
                print(CGREEN + f'{x}  %  {y}  =  {x % y}' + CEND)
            else:
                print(CRED + 'Ответ : Деление на ноль невозможно !!!'+ CEND)
    else:
        print(CRED + 'Ответ: Данной операции нет в системе !!!' + CEND)
