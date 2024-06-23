student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62  
}

student_grade = {}

def do_grading(student):
  score = student_scores[student]
  if score > 90:
    student_grade[student] = "Outstanding"     
  elif score > 80:
    student_grade[student] = "Exceed Expectations"     
  elif score > 70:
    student_grade[student] = "Acceptable"
  else:
    student_grade[student] = "Fail"

for student in student_scores:
  do_grading(student)

print(student_grade)