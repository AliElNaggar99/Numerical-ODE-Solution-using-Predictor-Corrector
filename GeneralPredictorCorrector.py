import math
from math import sqrt 
from math import exp as e


class GeneralPredictorCorrector:
    def __init__(self,EquationY,finalx,x,y,predictor,corrector,fix, Iterations):
        self.EquationY= EquationY
        self.finalX = finalx
        self.x = x.split()
        self.y = y.split()
        self.Iterations = Iterations
        self.predictor = predictor
        self.corrector = corrector
        self.h = float(self.x[1]) - float(self.x[0])
        self.fix = fix
    
    #functions to make x and y return floats
    def xf(self, n):
        return float(self.x[n])

    def yf(self,n):
        return float(self.y[n])
    
    #To solve the give Function from the User in Eval
    def Function(self,x,y):
        Func = self.EquationY.replace("x" , str(x))
        Func = Func.replace("e^","e")
        Func = Func.replace("y",str(y))
        Func = Func.replace("^","**")
        return eval(Func)
        
    #Make the Function take the index of x ,y in the array 
    def FunctionThattakesN(self,n):
        return round(self.Function(self.x[n],self.y[n]),int(self.fix))
    
    #Predict Function
    def Predicat(self):
        #change n or i with right number
        predicat = self.predictor.replace("n",str(len(self.y)-1))
        predicat = predicat.replace("i" , str(len(self.y)-1))
        predicat = predicat.replace("h",str(self.h))
        predicat = predicat.replace("f","self.FunctionThattakesN")
        predicat = predicat.replace("y","self.yf")
        return predicat
    
    #corrector Function
    def Correct(self):
        correct = self.corrector.replace("n",str(len(self.y)-2))
        correct = correct.replace("i",str(len(self.y)-2))
        correct = correct.replace("h" , str(self.h))
        correct = correct.replace("f","self.FunctionThattakesN")
        correct = correct.replace("y" , "self.yf")
        return correct

    #Main Function
    def FindFinalY(self):
        #calling predict
        y1 = eval(self.Predicat())
        #adding x(n+1) and y(n+1) in the last of the array 
        self.x.append(self.finalX)
        self.y.append(y1)
        C1 = eval(self.Correct())
        self.y[-1] = C1
        #make the iterations of Correct Function
        for i in range(int(self.Iterations)):
            C1 = eval(self.Correct())
            self.y[-1] = C1
        self.y[-1] = round(self.y[-1],int(self.fix))


#Main Function
EquationY = input("Enter y': ")
finalX = input("Enter X final: ")
Iterations = input("Enter the Iterations: ")
x = input("Enter X array: ")
y = input("Enter Y array: ")
predictor = input("Enter the Predict Equation: ")
Corrector = input("Enter the Corrector Equation: ")
fix = input("Enter fix: ")

#Make an Object from it
Equation1 = GeneralPredictorCorrector(EquationY,finalX,x,y,predictor,Corrector,fix,Iterations)

#calculate the final Y
Equation1.FindFinalY()

print("y(n+1) is : " + str(Equation1.y[-1]))
