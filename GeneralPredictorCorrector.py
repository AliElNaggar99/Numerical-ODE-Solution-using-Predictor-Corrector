import math



EquationY = input("Enter y': ")
finalX = input("Enter X final: ")
Iterations = input("Enter the Iterations: ")
x = input("Enter X array: ")
y = input("Enter Y array: ")
predictor = input("Enter the Predict Equation: ")
Corrector = input("Enter the Corrector Equation: ")
fix = input("Enter fix: ")
#replace the withspace in x and w to no space
x = x.split()
y = y.split()

#step size is equal to different between any two elements in x array
h = float(x[1]) - float(x[0])


#functions to make x and y return floats
def xf(n):
    return float(x[n])

def yf(n):
    return float(y[n])

#Defining sqrt to use it in eval directly
def sqrt(x):
 return math.sqrt(x)

#Define Exp to use it in eval directly
def e(x):
  return math.exp(x)

#To solve the give Function from the User in Eval
def Function(x,y):
 Func= EquationY.replace("x" ,str(x))
 Func = Func.replace("e^","e")
 Func= Func.replace("y" ,str(y))
 Func = Func.replace("^","**")
 return eval(Func)

#Make the Function take the index of x ,y in the array 
def FunctionTaketakesN(n):
 return round(Function(x[n],y[n]),int(fix))


#Predict Function
def predict():
#change n or i with right number
 predict = predictor.replace("n",str(len(y)-1))
 predict = predict.replace("i",str(len(y)-1))
 predict =predict.replace("h" , str(h))
 predict =predict.replace("f","FunctionTaketakesN")
 predict = predict.replace("y" , "yf")

 return predict


#Corrector Function
def correct():
 correct = Corrector.replace("n",str(len(y)-2))
 correct = correct.replace("i",str(len(y)-2))
 correct = correct.replace("h" , str(h))
 correct = correct.replace("f","FunctionTaketakesN")
 correct = correct.replace("y" , "yf")
 return correct


#main function
#calling predict
P1 = eval(predict())
#adding x(n+1) and y(n+1) in the last of the array 
x.append(finalX)
y.append(P1)
C1 = eval(correct())
y[-1] = C1
#make the iterations of Correct Function
for l in range(int(Iterations)):
    C1 = eval(correct())
    y[-1] = C1

final = round(y[-1],int(fix))

print("y(n+1) is: " + str(final))
