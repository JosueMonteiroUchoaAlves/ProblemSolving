# https://judge.beecrowd.com/pt/runs/code/46532822
N = int(input())
for _ in range(N):
    ans = []
    strings = input().split()
    primeiraString = strings[0]
    SegundaString = strings[1]
    for i in range(len(primeiraString)):
        if len(SegundaString) <= i:
            ans.append(primeiraString[i:])
            break   
        ans.append(primeiraString[i])
        ans.append(SegundaString[i])
    else:
        ans.append(SegundaString[i+1:])
    print("".join(ans))
