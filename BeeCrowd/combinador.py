# https://judge.beecrowd.com/pt/runs/code/46532822
N = int(input())
for _ in range(N):
    ans = ""
    strings = input().split()
    primeiraString = strings[0]
    SegundaString = strings[1]
    for i in range(len(primeiraString)):
        if len(SegundaString) <= i:
            ans = ans + primeiraString[i:]
            break
        ans = ans + primeiraString[i] + SegundaString[i]
    else:
        ans = ans + SegundaString[i+1:]
    print(ans)
