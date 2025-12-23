def gradingStudents(grades):
  for i in range(len(grades)):
    if grades[i] < 38:
      continue
    if grades[i] % 5 >= 3:
      grades[i] = grades[i] + 5 - (grades[i] % 5)
  return grades
print(gradingStudents([4,78,67,38,33]))
