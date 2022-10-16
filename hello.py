import math

try:
    a = int(input("Введите 1 катет: "))
    b = int(input("Введите 2 катет: "))
    c = math.sqrt(math.pow(a,2)+math.pow(b,2))
except:
    print("Error")

def Perim(a,b,c):
    p = a+b+c
    return p

def Square(a, b):
    s = (a+b)/2
    return s

print("Периметр: ",Perim(a,b,c),"см")
print("Квадрат: ",Square(a,b),"см^2")