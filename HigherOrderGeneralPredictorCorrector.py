import math
from math import sqrt 
from math import exp as e



class HigherOrderGeneralPredictorCorrector:
  def __init__(self, EquationY,EquationZ,finalx,Iterations,x,y,z,predictor,Corrector,fix):
    self.EquationY = EquationY
    self.EquationZ = EquationZ
    self.finalx = finalX
    self.Iterations = Iterations
    self.x = x.split()
    self.y = y.split()
    self.z = z.split()
    self.predictor = predictor
    self.Corrector = Corrector
    self.fix = fix
    #step size is equal to different between any two elements in x array
    self.h = float(self.x[1])-float(self.x[0])
  
  #functions to make x and y return floats
  def xf(self,n):
      return float(self.x[n])
  
  def yf(self,n):
      return float(self.y[n])
  
  def zf(self,n):
      return float(self.z[n])

  #To solve the give Function from the User in Eval
  def Function(self,x,y,z,flag):
    if flag == "y":
          Func = self.EquationY.replace("x" , str(x))
    elif flag == "z":
          Func = self.EquationZ.replace("x" , str(x))
    Func = Func.replace("e^","e")
    Func = Func.replace("y" , str(y))
    Func = Func.replace("^","**")
    Func = Func.replace("z", str(z))
    return eval(Func)

  #Make the Function take the index of x ,y in the array and call the function for z or y
  def FunctionThatTakesNForY(self,n):
    return round(self.Function(self.x[n],self.y[n],self.z[n],"y"),int(self.fix))
        
  def FunctionThatTakesNForZ(self,n):
    return round(self.Function(self.x[n],self.y[n],self.z[n],"z"),int(self.fix))
  
  #Predict Function
  def Predict(self,Symbol):
    predict = self.predictor.replace("n", str(len(self.y)-1))
    predict = predict.replace("i", str(len(self.y)-1))
    predict = predict.replace("h",str(self.h))
    if Symbol == "y":
      predict =predict.replace("f","self.FunctionThatTakesNForY")
      predict = predict.replace("y" , "self.yf")
    elif Symbol =="z":
      predict =predict.replace("f","self.FunctionThatTakesNForZ")
      predict = predict.replace("y" , "self.zf")
    return predict

  #Corrector Function
  def correct(self,Symbol):
    correct = self.Corrector.replace("n",str(len(self.y)-2))
    correct = correct.replace("i",str(len(self.y)-2))
    correct = correct.replace("h" , str(self.h))
    if Symbol == "y":
      correct = correct.replace("f","self.FunctionThatTakesNForY")
      correct = correct.replace("y" , "self.yf")
    elif Symbol =="z":
      correct = correct.replace("f","self.FunctionThatTakesNForZ")
      correct = correct.replace("y" , "self.zf")
    return correct

  #Main Function
  def FindFinalY(self):
    #calling predict
    YPredict = eval(self.Predict("y"))
    ZPredict = eval(self.Predict("z"))
    #adding x(n+1) and y(n+1) in the last of the array 
    self.x.append(self.finalx)
    self.y.append(YPredict)
    self.z.append(ZPredict)
    YCorrect = eval(self.correct("y"))
    ZCorrect = eval(self.correct("z"))
    self.y[-1] = YCorrect
    self.z[-1] = ZCorrect
    #make the iterations of Correct Function
    for l in range(int(Iterations)):
      YCorrect = eval(self.correct("y"))
      ZCorrect = eval(self.correct("z"))
      self.y[-1] = YCorrect
      self.z[-1]= ZCorrect
    self.y[-1] = round(self.y[-1],int(self.fix))
    self.z[-1] = round(self.z[-1],int(self.fix))

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

#Make an Object from it
Equation1 = HigherOrderGeneralPredictorCorrector(EquationY,EquationZ,finalX,Iterations,x,y,z,predictor,Corrector,fix)

#calculate the final Y
Equation1.FindFinalY()

print("y(n+1) is: " + str(Equation1.y[-1]))
print("z(n+1) is: " +str(Equation1.z[-1]))

