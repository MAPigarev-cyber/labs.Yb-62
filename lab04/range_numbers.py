a = int(input("Введите первое число a: "))
b = int(input("Введите второе число b: "))
if a < b:
    for i in range(a, b + 1):
        print(i)
elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    print(a)
