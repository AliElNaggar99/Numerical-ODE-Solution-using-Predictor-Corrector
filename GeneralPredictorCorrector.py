import math



z = input("Enter Equation: ")
f = input("X final: ")
i = input("Enter the Iterations: ")
x= input("Enter X array: ")
y= input("Enter Y array: ")
predictor = input("Enter the Predict Equation: ")
Corrector = input("Enter the Corrector Equation: ")
B = input("Enter fix: ")
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

#To solve the give Function from the User in Eval
def Function(x,y):
 w= z.replace("x" ,str(x))
 w= w.replace("y" ,str(y))
 w = w.replace("^","**")
 return eval(w)

#Make the Function take the index of x ,y in the array 
def FunctionTaketakesN(n):
 return round(Function(x[n],y[n]),int(B))

#Predict Function
def predict():

 L = predictor.replace("n",str(len(y)-1))
 L = L.replace("h" , str(h))
 L = L.replace("f","FunctionTaketakesN")
 L = L.replace("y" , "yf")

 return L


#Corrector Function
def correctF():
 L = Corrector.replace("n",str(len(y)-2))
 L = L.replace("h" , str(h))
 L = L.replace("f","FunctionTaketakesN")
 L = L.replace("y" , "yf")
 return L


#main function
#calling predict
P1 = eval(predict())
#adding x(n+1) and y(n+1) in the last of the array 
x.append(f)
y.append(P1)
C1 = eval(correctF())
y[-1] = C1
#make the iterations of Correct Function
for l in range(int(i)):
    C1 = eval(correctF())
    y[-1] = C1

final = round(y[-1],int(B))

print("y(n+1) is: " + str(final))
