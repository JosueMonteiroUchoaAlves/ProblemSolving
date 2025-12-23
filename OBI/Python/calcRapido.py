s = int(input())
a = int(input())
b = int(input())

resultado = 0
for i in range(a,b+1):
  j = i
  sominha = 0
  while j > 0:
    sominha += j%10
    j = j//10
  if sominha == s:
    resultado+= 1
print(resultado)
