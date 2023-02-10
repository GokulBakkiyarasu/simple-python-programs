total_even=0
total_odd=0
for i in range(1,101):
  if i%2==0:
    total_even+=i
  else:
    total_odd+=i
print(f"Sum of even numbers from 1 to 100 is: {total_even}")
print(f"Sum of odd numbers from 1 to 100 is: {total_odd}")
print(f"Sum of all numbers from 1 to 100 is: {total_even+total_odd}")
