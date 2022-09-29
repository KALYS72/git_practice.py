CEND = '\033[0m'
CBLUE = '\33[34m'
CRED = '\033[31m'
CGREEN = '\33[32m'
total = (input(CBLUE + 'Введите свои баллы по математике,\nанглийскому языку и литературе через запятую: ' + CEND))
num1 = int(total[0:2])
num2 = int(total[4:6])
num3 = int(total[8:10])
total1 = (num1 + num2 + num3) // 3
if total1 >= 69:
  print(CGREEN + f'Вы допущены к экзаменам. Ваш средний балл составляет {total1}' + CEND)
else:
  print(CRED + f'Вы не допущены к экзаменам. Ваш средний балл составляет {total1}' + CEND)