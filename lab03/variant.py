value = int(input("Введите заполненность хранилища (0-100): "))
if value < 0 or value > 100:
    print("Ошибка диапазона")
else:
    if value <= 49:
        print("свободно")
    elif value <= 89:
        print("Мало места")
    else:  
        print("Почти заполнено")
