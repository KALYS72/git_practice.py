x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# ладья
if x1 == x2 or y1 == y2:
  print(True)
else:
  print(False) 

# слон
if abs(x1 - x2) == abs(y1 - y2):
  print(True)
else:
  print(False)  

# король
if (x1 == x2 + 1 or x1 == x2 - 1 or x1 == x2) and (y1 == y2 + 1 or y1 == y2 - 1 or y1 == y2):
    print(True)
else:
    print(False)
