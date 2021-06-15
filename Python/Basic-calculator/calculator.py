 #Basic Calculator Using Python Programming Language

input1 = float(input("Enter First Number : ")) 
try:
    
   val = float(input1)
except ValueError:
   print("That's not an float or int!")
operator =  input("Enter Arithmetic Operator : ")

input2 = float(input("Enter Another Number : "))
try:
   val = float(input2)
except ValueError:
   print("That's not an float or int!")
if operator == "+":
    print("Sum of %.2f and %.2f Will be :"%(input1,input2),input1 + input2)
elif operator == "-":
    print("Diffrence of %.2f and %.2f Will be :"%(input1,input2),input1 - input2)
elif operator == "*":
    print("Multiplication of %.2f and %.2f Will be :"%(input1,input2),input1 * input2)
elif operator == "/":
    print("Division of %.2f and %.2f Will be : %.2f"%(input1,input2,(input1 / input2)))
elif operator == "%":
    print("Modulus of %.2f and %.2f Will be :"%(input1,input2),input1 % input2)
else:
    print("Please enter correct operator only")


