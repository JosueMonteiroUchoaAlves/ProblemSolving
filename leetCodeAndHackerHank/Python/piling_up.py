T = int(input())

for i in range(T):
  trash = input()
  cubes = list(map(int, input().split()))
  lastCubeOfPile = float("inf")
  while cubes:
    lastCube = cubes[-1]
    firstCube = cubes[0]
    if lastCube >= firstCube:
      if lastCube <= lastCubeOfPile:
        lastCubeOfPile = cubes.pop()
        continue
    if firstCube >= lastCube:
      if firstCube <= lastCubeOfPile:
        lastCubeOfPile = cubes.pop(0)
        continue
    print("No")
    break
  else:
    print("Yes")
