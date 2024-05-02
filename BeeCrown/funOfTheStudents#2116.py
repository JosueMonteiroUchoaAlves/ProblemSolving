# -*- coding: utf-8 -*-

"""
Juilherme and Jogerio really like mathematical games. Juilherme just created another mathematical game for them to have fun while watching this online competition.

The game consists of the following steps:

1) Juilherme chooses a number N and Jogério chooses a number M.
2) Juilherme and Jogério must then find two prime numbers P1 and P2, in such a way that they are as close as possible to the numbers N and M, respectively. Furthermore P1 must be less than or equal to N and P2 must be less than or equal to M.
3) The final answer to the challenge is to find the multiplication of P1 and P2. Whoever finds the answer first is the winner.

Since they will try to find an answer as quickly as possible, sometimes arriving at incorrect results, they need a game that delivered the final answer so that it can be compared with the answer they found.

Using the information from the game, make a program that gives the numbers N and M and prints the final result.
"""


## not an ideal solution but its working ##

N,M = map(int, input().split())
p1=0
p2=0

for i in range(N, 1,-1):
  if len([j for j in range(2, i//2) if i%j == 0]) == 0 or i == 2:
    p1=i
    break

for i in range(M ,1 ,-1):
  if len([j for j in range(2, i//2) if i%j == 0]) == 0 or i == 2:
    p2=i
    break

print(p2*p1)
