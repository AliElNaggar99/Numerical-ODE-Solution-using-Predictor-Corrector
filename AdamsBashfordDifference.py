import math



EquationY = input("Enter y': ")
finalX = input("Enter X final: ")
Iterations = input("Enter the Iterations: ")
x = input("Enter X array: ")
y = input("Enter Y array: ")
fix = input("Enter fix: ")
#replace the withspace in x and w to no space
x = x.split()
y = y.split()

#step size is equal to different between any two elements in x array
h = float(x[1]) - float(x[0])

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

#calculating array that contain the function in all x and y
FuncArray=[]
for i in range(len(x)):
    FuncArray.append(FunctionTaketakesN(i)) 

#Calculating The Deltas ex: delta^1 f , delta^2 f ...etc
#we will loop on array with i where I is not last element in array
DeltaFunc1 = []
for i in range(len(FuncArray) -1):
    DeltaFunc1.append(round(FuncArray[i+1] - FuncArray[i],int(fix)))


#Doing the Sample but for Delta^2 and ...etc with same Idea
DeltaFunc2 = []
for i in range(len(DeltaFunc1) -1):
    DeltaFunc2.append(round(DeltaFunc1[i+1] - DeltaFunc1[i],int(fix)))

DeltaFunc3 = []
for i in range(len(DeltaFunc2) -1):
    DeltaFunc3.append(round(DeltaFunc2[i+1] - DeltaFunc2[i],int(fix)))

DeltaFunc4 = []
for i in range(len(DeltaFunc3) -1):
    DeltaFunc4.append(round(DeltaFunc3[i+1] - DeltaFunc3[i],int(fix)))




#Calculating The Predicat Value
predicat =round(float(y[-1])+h*(FuncArray[-1]+0.5*DeltaFunc1[-1]+5/12*DeltaFunc2[-1] +3/8*DeltaFunc3[-1]+251/720*DeltaFunc4[-1]),int(fix))



#adding it in Last of x and y arrays
x.append(finalX)
y.append(predicat)
#calculate the Function of new x and y
FuncArray.append(FunctionTaketakesN(len(x)-1))
#add this to all the Deltas
DeltaFunc1.append(FuncArray[-1]-FuncArray[-2])
DeltaFunc2.append(DeltaFunc1[-1]-DeltaFunc1[-2])
DeltaFunc3.append(DeltaFunc2[-1]-DeltaFunc2[-2])
DeltaFunc4.append(DeltaFunc3[-1]-DeltaFunc3[-2])

#Corrector Function
def correctAdams():
 #calculate the new correct value
 correct = round(float(y[-2])+h*(FuncArray[-1]-0.5*DeltaFunc1[-1]-1/12*DeltaFunc2[-1] -1/24*DeltaFunc3[-1]-19/720*DeltaFunc4[-1]),int(fix))
 #update the y
 y[-1] = correct 
 #calculate the Function of new x and y
 FuncArray[-1] = FunctionTaketakesN(len(x)-1)
 #update all the Deltas
 DeltaFunc1[-1]= FuncArray[-1]-FuncArray[-2]
 DeltaFunc2[-1]= DeltaFunc1[-1]-DeltaFunc1[-2]
 DeltaFunc3[-1]= DeltaFunc2[-1]-DeltaFunc2[-2]
 DeltaFunc4[-1]= DeltaFunc3[-1]-DeltaFunc3[-2]
  

#calling the Corrector as many Times as the User wanted
for i in range(int(Iterations)):
   correctAdams()

print("y(n+1) is : " + str(y[-1]))