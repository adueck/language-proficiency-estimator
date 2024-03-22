from query import query_model

while True:
  age = int(input("what's your age? "))
  print("What's your education level?")
  print("0 - High School")
  print("1 - Professional Training")
  print("2 - University")
  print("3 - Postgraduate")
  education = int(input("? "))
  percent = int(input("what percent of your life is in english? "))
  result = query_model(age, education, percent)
  print(f'Your proficiency will probably be: {result}%')
  print("")

