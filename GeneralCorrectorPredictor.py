import math



z = input("Enter Equation: ")
f = input("X final: ")
i = input("Enter the Iterations: ")
x= input("Enter X: ")
y= input("Enter Y: ")
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

def sqrt(x):
 return math.sqrt(x)

def Function(f,p):
 w= z.replace("x" ,str(f))
 w= w.replace("y" ,str(p))
 w = w.replace("^","**")
 return eval(w)


def FunctionTaketakesN(n):
 return round(Function(x[n],y[n]),int(B))


def predict():
#Predict Function
 
 L = predictor.replace("n",str(len(y)-1))
 L = L.replace("h" , str(h))
 L = L.replace("f","FunctionTaketakesN")
 L = L.replace("y" , "yf")

 return L



def correctF():
#Corrector Function
 L = Corrector.replace("n",str(len(y)-2))
 L = L.replace("h" , str(h))
 L = L.replace("f","FunctionTaketakesN")
 L = L.replace("y" , "yf")
 return L


#main function
#calling predict
P1 = eval(predict())
x.append(f)
y.append(P1)
C1 = eval(correctF())
print(correctF())
y[-1] = C1

for l in range(int(i)):
    C1 = eval(correctF())
    y[-1] = C1

final = round(y[-1],int(B))
print(final)