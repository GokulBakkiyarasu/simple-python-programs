def format_names(f_name,l_name):
  """This function takes the frist and last names and returns your full name in title case verision of the name"""
  if f_name=="" or l_name=="":
    return "Enter a valid input"
  formated_f_name=f_name.title()
  formated_l_name=l_name.title()
  return f"Your full name is {formated_f_name} {formated_l_name}"

print(format_names(input("Enter your Frist Name: "),input("Enter your Second Name: ")))
