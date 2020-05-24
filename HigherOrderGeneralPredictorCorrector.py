import math



EquationY = input("Enter y': ")
EquationZ = input("Enter Z': ")
finalX = input("Enter X final: ")
Iterations = input("Enter the Iterations: ")
x = input("Enter X array: ")
y = input("Enter Y array: ")
z = input("Enter Z array: ")
predictor = input("Enter the Predict Equation: ")
Corrector = input("Enter the Corrector Equation: ")
fix = input("Enter fix: ")
#replace the withspace in x and w to no space
x = x.split()
y = y.split()
z=z.split()

#step size is equal to different between any two elements in x array
h = float(x[1]) - float(x[0])


#functions to make x and y return floats
def xf(n):
    return float(x[n])

def yf(n):
    return float(y[n])

def zf(n):
    return float(z[n])

#Defining sqrt to use it in eval directly
def sqrt(x):
 return math.sqrt(x)

#Define Exp to use it in eval directly
def e(x):
  return math.exp(x)

#To solve the give Function from the User in Eval
def Function(x,y,z,flag):
 if flag == "y":
  Func= EquationY.replace("x" ,str(x))
 elif flag =="z":
  Func= EquationZ.replace("x" ,str(x))
 Func = Func.replace("e^","e")
 Func= Func.replace("y" ,str(y))
 Func = Func.replace("^","**")
 Func = Func.replace("z" ,str(z))
 return eval(Func)

#Make the Function take the index of x ,y in the array and call the function for z or y
def FunctionTaketakesNForY(n):
 return round(Function(x[n],y[n],z[n],"y"),int(fix))


def FunctionTaketakesNForZ(n):
    return round(Function(x[n],y[n],z[n],"z"),int(fix))


#Predict Function
def predict(Symbol):

 predict = predictor.replace("n",str(len(y)-1))
 predict = predict.replace("i",str(len(y)-1))
 predict =predict.replace("h" , str(h))
 if Symbol == "y":
   predict =predict.replace("f","FunctionTaketakesNForY")
   predict = predict.replace("y" , "yf")
 elif Symbol =="z":
   predict =predict.replace("f","FunctionTaketakesNForZ")
   predict = predict.replace("y" , "zf")
 return predict


#Corrector Function
def correct(Symbol):
 correct = Corrector.replace("n",str(len(y)-2))
 correct = correct.replace("i",str(len(y)-2))
 correct = correct.replace("h" , str(h))
 if Symbol == "y":
       correct = correct.replace("f","FunctionTaketakesNForY")
       correct = correct.replace("y" , "yf")
 elif Symbol =="z":
   correct = correct.replace("f","FunctionTaketakesNForZ")
   correct = correct.replace("y" , "zf")
 return correct


#main function
#calling predict
YPredict = eval(predict("y"))
ZPredict = eval(predict("z"))
#adding x(n+1) and y(n+1) in the last of the array 
x.append(finalX)
y.append(YPredict)
z.append(ZPredict)
YCorrect = eval(correct("y"))
ZCorrect = eval(correct("z"))
y[-1] = YCorrect
z[-1]= ZCorrect
#make the iterations of Correct Function
for l in range(int(Iterations)):
    YCorrect = eval(correct("y"))
    ZCorrect = eval(correct("z"))
    y[-1] = YCorrect
    z[-1]= ZCorrect


finaly = round(y[-1],int(fix))
finalz = round(z[-1],int(fix))

print("y(n+1) is: " + str(finaly))
print("z(n+1) is: " +str(finalz))
