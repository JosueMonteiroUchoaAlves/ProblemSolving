import itertools as it

trash = input()
array = input().split()
elements = int(input())

combinations = list(it.combinations(array, elements))

answer = 0
for c in combinations:
    if 'a' in c:
      answer += 1

print(f"{answer/len(combinations):.4f}")
