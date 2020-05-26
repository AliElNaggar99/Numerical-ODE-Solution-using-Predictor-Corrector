import math
from math import sqrt 
from math import exp as e


class AdamsBashFord:
    def __init__(self, EquaY, FX, I , X,Y , FIX):
        self.EquationY = EquaY 
        self.finalX = FX 
        self.Iterations = I  
        self.x = X.split()
        self.y = Y.split()
        self.h = float(self.x[1]) - float(self.x[0])
        self.fix = FIX

    def Function(self,x,y):
        Func= self.EquationY.replace("x" ,str(x))
        Func = Func.replace("e^","e")
        Func= Func.replace("y" ,str(y))
        Func = Func.replace("^","**")
        return eval(Func)
    
    def FunctionTaketakesN(self,n):
     return round(self.Function(self.x[n],self.y[n]),int(self.fix))

    def Predicat(self): 
        #calculating array that contain the function in all x and y
        self.FuncArray=[]
        for i in range(len(self.x)):
            self.FuncArray.append(self.FunctionTaketakesN(i)) 

        #Calculating The Deltas ex: delta^1 f , delta^2 f ...etc
        #we will loop on array with i where I is not last element in array
        self.DeltaFunc1 = []
        for i in range(len(self.FuncArray) -1):
            self.DeltaFunc1.append(round(self.FuncArray[i+1] - self.FuncArray[i],int(self.fix)))


        #Doing the Sample but for Delta^2 and ...etc with same Idea
        self.DeltaFunc2 = []
        for i in range(len(self.DeltaFunc1) -1):
            self.DeltaFunc2.append(round(self.DeltaFunc1[i+1] - self.DeltaFunc1[i],int(self.fix)))

        self.DeltaFunc3 = []
        for i in range(len(self.DeltaFunc2) -1):
            self.DeltaFunc3.append(round(self.DeltaFunc2[i+1] - self.DeltaFunc2[i],int(self.fix)))

        self.DeltaFunc4 = []
        for i in range(len(self.DeltaFunc3) -1):
            self.DeltaFunc4.append(round(self.DeltaFunc3[i+1] - self.DeltaFunc3[i],int(self.fix)))

        #Calculating The Predicat Value
        self.predicat =round(float(self.y[-1])+self.h*(self.FuncArray[-1]+0.5*self.DeltaFunc1[-1]+5/12*self.DeltaFunc2[-1] +3/8*self.DeltaFunc3[-1]+251/720*self.DeltaFunc4[-1]) , int(self.fix))

        #adding it in Last of x and y arrays
        self.x.append(self.finalX)
        self.y.append(self.predicat)
        #calculate the Function of new x and y
        self.FuncArray.append(self.FunctionTaketakesN(len(self.x)-1))
        #add this to all the Deltas
        self.DeltaFunc1.append(self.FuncArray[-1]-self.FuncArray[-2])
        self.DeltaFunc2.append(self.DeltaFunc1[-1]-self.DeltaFunc1[-2])
        self.DeltaFunc3.append(self.DeltaFunc2[-1]-self.DeltaFunc2[-2])
        self.DeltaFunc4.append(self.DeltaFunc3[-1]-self.DeltaFunc3[-2])
    #Corrector Function
    def correctAdams(self):
        #calculate the new correct value
        self.correct = round(float(self.y[-2])+self.h*(self.FuncArray[-1]-0.5*self.DeltaFunc1[-1]-1/12*self.DeltaFunc2[-1] -1/24*self.DeltaFunc3[-1]-19/720*self.DeltaFunc4[-1]),int(self.fix))
        #update the y
        self.y[-1] = self.correct 
        #calculate the Function of new x and y
        self.FuncArray[-1] = self.FunctionTaketakesN(len(self.x)-1)
        #update all the Deltas
        self.DeltaFunc1[-1]= self.FuncArray[-1]-self.FuncArray[-2]
        self.DeltaFunc2[-1]= self.DeltaFunc1[-1]-self.DeltaFunc1[-2]
        self.DeltaFunc3[-1]= self.DeltaFunc2[-1]-self.DeltaFunc2[-2]
        self.DeltaFunc4[-1]= self.DeltaFunc3[-1]-self.DeltaFunc3[-2]
   
    #Do the Iterations to get Y final
    def FindFinalY(self):
        self.Predicat()
        for i in range(int(self.Iterations)):
           self.correctAdams()

    
        


    

#Main Function
EquationY = input("Enter y': ")
finalX = input("Enter X final: ")
Iterations = input("Enter the Iterations: ")
x = input("Enter X array: ")
y = input("Enter Y array: ")
fix = input("Enter Fix: ")

#Make an Object from it
Equation1 = AdamsBashFord(EquationY,finalX,Iterations,x,y,fix)

#calculate the Predicat
Equation1.FindFinalY()

print("y(n+1) is : " + str(Equation1.y[-1]))