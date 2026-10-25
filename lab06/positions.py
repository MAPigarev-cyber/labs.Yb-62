s= input().strip()
if not s:
    print("Нет данных")
else:
    nums = list(map(int, s.split()))
    mx = max(nums)
    positions = [i for i, x in enumerate(nums) if x == mx]
    print(positions)
