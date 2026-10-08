n = int(input("Введите количество чисел n (n >= 0): "))
count = 0
total = 0
for i in range(n):
    x = int(input(f"Введите число {i + 1}: "))
    if x < 0:
        count += 1
        total += x
print(f"Количество отрицательных чисел: {count}")
print(f"Сумма отрицательных чисел: {total}")
