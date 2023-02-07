student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count=n+1
total_height=0
for height in student_heights:
    total_height+=height
avg_height=round(total_height/count)
print(avg_height)
