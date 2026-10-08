attempts = 0  
number = int(input("Введите положительное целое число: "))
while number <= 0:
    attempts += 1
    number = int(input("Число должно быть положительным. Попробуйте ещё раз: "))
print(f"Квадрат числа: {number ** 2}")
print(f"Отклонённых попыток: {attempts}")
