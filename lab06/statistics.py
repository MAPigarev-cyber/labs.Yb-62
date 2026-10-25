s = input().strip()
if not s:
    print("Нет данных")
else:
    nums = list(map(int, s.split()))
    count = len(nums)
    total = sum(nums)
    mn = min(nums)
    mx = max(nums)
    avg = total / count
    print(count)
    print(total)
    print(mn)
    print(mx)
    print(f"{avg:.2f}")
