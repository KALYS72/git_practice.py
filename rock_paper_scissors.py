import random

while True:
  print('\n') 
  CRED = '\033[31m'
  CEND = '\033[0m'
  CGREEN = '\33[32m'
  CBLUE = '\33[34m'
  CVIOLET = '\33[35m'
  CYELLOW = '\33[93m'
  comp = random.randint(1, 3)
  player = int(input(CBLUE + "1 - камень, 2 - ножницы, 3 - бумага. " + CEND))
  print('\n')
  if int(player) < 4 and int(player) > 0:
    
    if player == 1:
        print(CBLUE + 'Вы выбрали камень' + CEND)
    elif player == 2:
        print(CBLUE + "Вы выбрали ножницы" + CEND)
    elif player == 3:
        print(CBLUE + "Вы выбрали бумагу" + CEND)
    if comp == 1:
        print(CYELLOW + 'Компьютер выбрал камень' + CEND)
    elif comp == 2:
        print(CYELLOW + "Компьютер выбрал ножницы." + CEND)
    elif comp == 3:
        print(CYELLOW + "Компьютер выбрал бумагу." + CEND)
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1
    if player == 1 and comp == 3:
        win = 2
    if player == 2 and comp == 1:
        win = 2
    if player == 2 and comp == 3:
        win = 1
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2  
    if win == 0:
        print(CVIOLET + 'Ничья!' + CEND)
    if win == 1:
        print(CGREEN + 'Вы победили!' + CEND)
    if win == 2:
        print(CRED + 'Компьютер победил!' + CEND)
  else:
    print(CRED + 'Вы ввели неправильный символ!' + CEND)