logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


#calculator
#addtion 

def add(n1,n2):
  """This function is used for performing addition between two numbers"""
  return n1+n2
#subract
def subract(n1,n2):
  """This function is used for performing subraction between two numbers"""
  return n1-n2
#multiply
def multiply(n1,n2):
  """This function is used for performing multiplication between two numbers"""
  return n1*n2
#divide
def divide(n1,n2):
  """This function is used for performing division between two numbers"""
  return n1/n2
  
operations={
  "+":add,
  "-":subract,
  "*":multiply,
  "/":divide,
}
def calculator():
 print(logo)
 num1=float(input("Enter the frist number: "))
 should_continue=True
 while should_continue:
  for symbol in operations:
    print(symbol)
  operation=input("Please select an opeartor from the above list: ")
  num2=float(input("Enter the next number: "))
  result=operations[operation](n1=num1,n2=num2)
  print(f"{num1} {operation} {num2} = {result}")
  num1=result
  to_continue=input(f"Enter 'y' to continue {result} or 'n' for new calculation: ")
  if to_continue=="n":
    calculator()
    
    
calculator()   
  
  


