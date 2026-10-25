s = input().strip()
if not s:
    nums = []
else:
    nums = list(map(int, s.split()))
new_nums = [abs(x) for x in nums]
print(nums)
print(new_nums)
