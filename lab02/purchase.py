price = int(input("Введите цену одной тетради (в рублях): "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму (в рублях): "))
total_cost = price * count
change = paid - total_cost
print(f"Стоимость: {total_cost}")
print(f"Сдача: {change}")
