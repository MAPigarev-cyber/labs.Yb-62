s = input()
raw_words = s.split()
cleaned_words = [w.strip('.,!?:;').lower() for w in raw_words]
cleaned_words = [w for w in cleaned_words if w]
matched = [w for w in cleaned_words if w.endswith('я')]
if not matched:
    print("Нет совпадений")
    print(0)
else:
    for w in matched:
        print(w)
    print(len(matched))
