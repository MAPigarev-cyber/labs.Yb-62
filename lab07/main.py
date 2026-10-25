import functions
def main():
    print("--- 1. Сумма цифр ---")
    num_str = input("Введите целое число: ").strip()
    if num_str:
        try:
            number = int(num_str)
            print(f"Сумма цифр: {functions.sum_digits(number)}")
        except ValueError:
            print("Некорректный ввод числа.")

    print("\n--- 2. Среднее ---")
    nums_str = input("Введите строку чисел (через пробел): ").strip()
    numbers_list = []
    if nums_str:
        try:
            numbers_list = list(map(int, nums_str.split()))
        except ValueError:
            print("Некорректный ввод чисел.")
    
    avg = functions.average(numbers_list)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg}")

    print("\n--- 3. Нормализация текста ---")
    text = input("Введите произвольный текст: ")
    print(f"Нормализованный текст: {functions.normalize_text(text)}")

    print("\n--- 4. Индивидуальный вариант 2 (Меньше порога) ---")
    threshold_str = input("Введите порог (целое неотрицательное число): ").strip()
    if threshold_str:
        try:
            threshold = int(threshold_str)
            if threshold >= 0:
                filtered = functions.select_numbers(numbers_list, threshold)
                print(f"Отфильтрованный список: {filtered}")
            else:
                print("Порог должен быть неотрицательным.")
        except ValueError:
            print("Некорректный ввод порога.")

if __name__ == '__main__':
    main()
