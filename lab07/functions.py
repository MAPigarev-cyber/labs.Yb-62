def sum_digits(number):
    """Сумма цифр модуля числа. Для нуля — 0."""
    n = abs(number)  
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
def average(numbers):
    """Среднее чисел. None, если список пуст. Исходный список не меняется."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return ' '.join(text.split()).lower()
