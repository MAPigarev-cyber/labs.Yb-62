s = input()
cleaned = ''.join(ch.lower() for ch in s if ch != ' ')
if not cleaned:
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
