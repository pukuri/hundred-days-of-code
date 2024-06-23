student_heights = input("Input a list of student heights: ").split()
total_heights = 0
student_count = 0

for n in student_heights:
  total_heights += int(n)     
  student_count += 1

print(f"Average height is {total_heights / student_count}")