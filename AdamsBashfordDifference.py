import math



z = input("Enter Equation: ")
f = input("X final: ")
i = input("Enter the Iterations: ")
x= input("Enter X: ")
y= input("Enter Y: ")
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


def predictAdams():
#Predict Function
 

 return L



def correctAdams():
#Corrector Function
 
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