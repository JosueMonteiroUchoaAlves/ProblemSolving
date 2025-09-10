N = int(input())
j = ""
for _ in range(N):
  s = input().split()

  for i in range(len(s[0])):
    j = j+s[0][i]+s[1][i]
  j = j+s[1][i+1:]
  print(j)
  j = ""
