class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if other.b == 0:
            f3 = [self.a, "/", self.b]
            return f3
        elif self.b == 0:
            f3 = [-other.a, "/", other.b]
            return f3
        f = 1
        if self.b != other.b:
            for i in range(min(self.b, other.b), self.b * other.b + 1):
                if i % self.b == 0 and i % other.b == 0:
                    self.a = int(self.a * i / self.b)
                    self.b == i
                    other.a = int(other.a * i / other.b)
                    other.b == i
                    f = i
                    break
        f3 = [self.a + other.a, "/", f]
        return f3

    def __sub__(self, other):
        if other.b == 0:
            f3 = [self.a, "/", self.b]
            return f3
        elif self.b == 0:
            f3 = [-other.a, "/", other.b]
            return f3

        if self.b != other.b:
            for i in range(min(self.b, other.b), self.b * other.b + 1):
                if i % self.b == 0 and i % other.b == 0:
                    self.a = int(self.a * i / self.b)
                    self.b == i
                    other.a = int(other.a * i / other.b)
                    other.b == i
                    f = i
                    break
        f3 = [self.a - other.a, "/", f]
        return f3

    def __mul__(self, other):
        if self.a % self.b == 0:
            self.a = self.b
            self.b = 1
        if other.a % other.b == 0:
            other.a = other.b
            other.b = 1
        f3 = [self.a * other.a, "/", self.b * other.b]
        return f3

    def __int__(self):
        return int(self.a / self.b)

    def __float__(self):
        return float(self.a / self.b)


class OperationsOnFraction(Fraction):

    def getint(self):
        return print(int(self.a / self.b))

    def getfloat(self):
        return print(float(self.a / self.b))


print("Добро пожаловать в программу, которая совершает операции с целыми и дробынми числами!")
print("Если число целое, то просто введите число")
print("Если число дробное, то введите число в формате a/b")
f1 = input("Введите первое число: ")
op = input("Выберите операцию('+','-','*'): ")
f2 = input("Введите второе число: ")
# if ("/" not in f1) and ("/" not in f2):
#     f111 = Fraction(f1,f1)
#     f211 = Fraction(f2,f2)
#
# else:
if "/" in f1:
    f11 = list(map(int, f1.split('/')))
    f111 = Fraction(f11[0], f11[1])
if "/" in f2:
    f21 = list(map(int, f2.split('/')))
    f211 = Fraction(f21[0], f21[1])
if '/' not in f1:
    f111 = Fraction(int(f1) * int(f1), int(f1))
if '/' not in f2:
    f211 = Fraction(int(f2) * int(f2), int(f2))

if op == "+":
    f3 = f111 + f211
    print("Результат выбранной операции = ", *f3, sep="")
elif op == "-":
    f3 = f111 - f211
    print("Результат выбранной операции = ", *f3, sep="")
elif op == "*":
    f3 = f111 * f211
    print("Результат выбранной операции = ", *f3, sep="")

f31 = OperationsOnFraction(f3[0], f3[2])
print("Хотите увидеть результат в виде целого числа или десятичной дроби c помощью функции внутри класса?")

while True:
    IntOrFloat = input("Выберете int/float/нет: ")
    if IntOrFloat == "float":
        print(float(f31))
    elif IntOrFloat == "int":
        print(int(f31))
    else:
        break

f32 = OperationsOnFraction(f3[0], f3[2])

print("Хотите увидеть результат в виде целого числа или десятичной дроби c помощью дочернего класса?")

while True:
    IntOrFloat = input("Выберете int/float/нет: ")
    if IntOrFloat == "float":
        f32.getfloat()
    elif IntOrFloat == "int":
        f32.getfloat()
    else:
        break
