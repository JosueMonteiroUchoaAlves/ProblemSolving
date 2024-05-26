def possibleChanges(usernames):
  result= []
  for username in usernames:
    if sorted(username) == list(username):
      result.append("NO")
    else:
      result.append("YES")
      continue
  return result
print(possibleChanges(["foo"]))
