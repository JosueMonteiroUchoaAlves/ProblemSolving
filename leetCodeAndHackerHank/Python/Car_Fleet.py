# https://leetcode.com/problems/car-fleet/description/
# 853. Car Fleet

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
  cars = [[p, s] for p, s in zip(position, speed)]
  cars.sort(key=lambda x: x[0], reverse=True)
  stack = []
  for car in range(len(cars)):
    time = (target-cars[car][0])/cars[car][1]
    if stack and time <= stack[-1]:
      continue
    stack.append(time)
  return len(stack)   
