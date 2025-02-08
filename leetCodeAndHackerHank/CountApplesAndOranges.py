# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

# Main function
def countApplesAndOranges(s, t, a, b, apples, oranges):
  house = range(s, t+1)
  num_of_apples = sum([True for apple in apples if apple + a in house])
  
  num_of_oranges = sum([True for orange in oranges if orange + b in house])
  
  print(num_of_apples)
  print(num_of_oranges)
  
  
# Test function
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
