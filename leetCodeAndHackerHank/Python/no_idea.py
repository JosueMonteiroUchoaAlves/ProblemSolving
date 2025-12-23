trash = input()
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for item in array:
    if item in A:
        happiness += 1
    elif item in B:
        happiness -= 1
print(happiness)
