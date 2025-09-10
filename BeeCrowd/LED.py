LED = {"0":6,
       "1":2,
       "2":5,
       "3":5,
       "4":4,
       "5":5,
       "6":6,
       "7":3,
       "8":7,
       "9":6,}

N = int(input())
total = 0
for _ in range(N):
  numero = list(input())
  for num in numero:
    total += LED[num]
  print(total, "leds")
  total=0

