s = input().strip()
if not s:
    nums = []
else:
    nums = list(map(int, s.split()))
negatives = [x for x in nums if x < 0]
total = sum(negatives)
sorted_negatives = sorted(negatives)
print(negatives)
print(len(negatives))
print(total)
print(sorted_negatives)
