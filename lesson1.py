#Take input for the student that he can attend the exam or not
eligibility=input("did you have a eligibility Y or N: ")
#Take input of the attendance
atten = int(input("enter the attendance of the student: "))

#checking the user input predicting output accordingly

if eligibility == 'Y': #checking the condition 1
  print ("You are allowed")
else:
  if atten>=75:  #checking the condition 2
    print ("Allowed")
  else:
    print ("Not allowed")