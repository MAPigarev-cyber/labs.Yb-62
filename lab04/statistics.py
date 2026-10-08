n = int(input("Введите количество чисел n (n >= 1): "))
total = 0            
positive_count = 0   
maximum = None       
for i in range(n):
    x = int(input(f"Введите число {i + 1}: "))
    total += x
    if x > 0:
        positive_count += 1
    if maximum is None:
        maximum = x
    elif x > maximum:
        maximum = x
print(f"Сумма: {total}")
print(f"Положительных значений: {positive_count}")
print(f"Максимум: {maximum}")
