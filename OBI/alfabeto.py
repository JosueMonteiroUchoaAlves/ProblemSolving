# OBI 2024
# SEGUNDA ETAPA | SECOND PHASE
# 100% correct

K , N = input().split()
AlienAlf = input()
setAlien = {letter for letter in AlienAlf}

message = input()

for letter in message:
  if letter not in setAlien:
    print("N")
    break
else:
  print("S")
