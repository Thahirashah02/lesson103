#Take input from user
print("Check your is between 20 to 30 years or not")
x = int(input("enter your age: "))


if x > 20: #condition 1
  print("Your age is more than 20 years")
  if x > 30: #nested condition
    print("And it is more than 30 as well")
  else:
    print("But it is less not more than 30")