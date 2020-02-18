
# number = int(input("Enter number: "))
# print(number)
# print("asdasdasdasd")


while True:

  try:
    number = int(input("Enter number: "))
    
    result = 20 / number
    print(number)
    break
  except ValueError as e :
    print("Error: input wasn't present as number")
  except ZeroDivisionError as zer :
      print("Error: zero divison error")
# print("asdasdasdasd")