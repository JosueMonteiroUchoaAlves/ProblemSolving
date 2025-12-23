nums = [1,2,2,2,3,4,4,4,5,5,6,7,8,8,8,8,8,8,9,9,9,9,9,9]

cur = 0

last = None

for n in nums:

    if n == last: continue

    last = n

    nums[cur] = n

    cur += 1

print(cur)
