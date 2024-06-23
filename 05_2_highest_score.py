student_scores = input("Input a list of student scores: ").split()
max_score = 0

for n in student_scores:
  if max_score < int(n):
    max_score = int(n)

print(f"The highest score is: {max_score}")
