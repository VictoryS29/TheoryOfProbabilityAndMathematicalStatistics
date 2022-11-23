import numpy as np
import math
import matplotlib.pyplot as plt

data =[]
price=[]
time=[]
lenght=0
b=int(0)
name=input("Введіть назву файла: ") #input_10.txt input_100.txt
with open(name, "r") as file:
     NewData=file.read().replace("\t"," ").replace("\n"," ").replace(",",".").split(" ")
     
     NewData.remove(NewData[0])
     
     if NewData[len(NewData)-1]=='':
         NewData.remove(NewData[len(NewData)-1])
         
     lenght=len(NewData)    
     
     for i in range(lenght):
         if i%2==1:
             time.append(float(NewData[i]))
         else:
             price.append(float(NewData[i]))
             
lenght =int(lenght/2)           
          
data=[ [], [] ]
for i in range(0,lenght):
    data[0].append(price[i] )
    data[1].append(time[i] )
print(data)
res=open("output.txt", "w")
res.write("===================================================\n") 
res.write("Ціна      Час\n")
res.write("===================================================\n") 
for i in range(0,lenght):
     data[0].append(price[i] )
     data[1].append(time[i] )
     res.write(str(price[i])+"       "+str(time[i]) + "\n")

res.write("===================================================\n") 


def meanX():  
    meanPrice=0
    for i in range(0,lenght):
        meanPrice+=price[i]
    meanPrice /=len(price)
    return meanPrice
def meanY():
    meanTime=0
    for i in range(0,lenght):
        meanTime+=time[i]
    meanTime /=len(time)
    return meanTime

def TrendLine():
    first=0
    second=0
    for i in range(0,lenght):
        first+=(price[i]-meanX())*(time[i]-meanY())
        second+=(price[i]-meanX())**2
    m=first/second
    return m

def Covariation():
    summ=0
    for i in range(0,lenght):
        summ+=price[i]*time[i]
    nsumm=(1/lenght)*summ
    cov=nsumm-meanX()*meanY()
    return round(cov,2)

    
def Dispersion():
    summa=0
    for i in range(0,lenght):
        summa+=price[i]**2
    summa=(1/lenght)*summa    
    dispersion=summa-meanX()**2
    return round(dispersion,2)

def DispersionY():
    summa=0
    for i in range(0,lenght):
        summa+=time[i]**2
    summa=(1/lenght)*summa    
    dispersion=summa-meanY()**2
    return round(dispersion,2)

def Corelation():
    summ=0
    first=0
    second=0
    for i in range(0,lenght):
     first=(price[i]-meanX())/math.sqrt(Dispersion())
     second=(time[i]-meanY())/math.sqrt(DispersionY())
     summ+=first*second
     cor=(1/(lenght-1))*summ
    return round(cor,2)





def Task1():
    res.write("Завдання 1\n")
    res.write("=========== \n") 
    plt.scatter(data[0],data[1],color="maroon"  )
 
    plt.title('Діаграма розсіювання')    
    plt.xlabel('ціна')
    plt.ylabel('час')
    
    b=meanY()-TrendLine()*meanX()
    
    x = np.linspace (1, 10)
    y = TrendLine()*x+b
    plt.plot (x, y, linewidth = 2, c="k");
   
    if y[8]>y[0]:
        plt.text(5,10,'Тренд позитивний')
        res.write("Тренд позитивний\n") 
        b=1
    else: 
        plt.text(5,10,'Тренд негативний')
        res.write("Тренд негативний\n") 
        b=2
    plt.show()
    
def Task2():
    res.write("===================================================\n") 
    res.write("Завдання 2\n")
    res.write("=========== \n") 
    WeightX=meanX()
    WeightY=meanY()
    WeightX=round(WeightX,2)
    res.write("Точка ваги:("+str(WeightX)+";"+str(WeightY)+")\n") 
    res.write("Коваріація: "+str(Covariation())+"\n") 

def Task3():
    res.write("===================================================\n") 
    res.write("Завдання 3\n")
    res.write("=========== \n") 
    b1=round(Covariation()/Dispersion(),2)
    b0=round(meanY()-b1*meanX(),2)
    res.write("Рівняння регресії: y=" + str(b1)+"*x"+str(b0)+"=0\n") 

def Task4():
    res.write("===================================================\n") 
    res.write("Завдання 4\n")
    res.write("=========== \n") 
    res.write("Коефіцієнт кореляції:"+str(Corelation())+"\n" ) 

def Task5():
    res.write("===================================================\n") 
    res.write("Завдання 5\n")
    res.write("=========== \n") 
    res.write("Коефіцієнт кореляції:"+str(Corelation())+"\n" ) 
    if b==1:
      res.write("Тренд позитивний\n") 
    else: 
      res.write("Тренд негативний\n") 
      
      
    if (Corelation()> 0.5) & (Corelation()<1):
       res.write("Коефіцієнт кореляції наближається до 1, значить дані майже співпадають з лінією регресії \n") 
    elif Corelation()==1  :
        res.write("Коефіцієнт кореляції дорівнює 1, значить дані співпадають з лінією регресії \n") 
    elif  Corelation()==0:
        res.write("Коефіцієнт кореляції дорівнює 0, значить дані незалежні лінійно \n") 
    elif  Corelation()==-1 :
        res.write("Коефіцієнт кореляції дорівнює -1, значить дані лінійно залежні або існує сильний лінійний зв’язок між ними\n") 
    elif  (Corelation()>0) & (Corelation()<=0.5):
        res.write("Коефіцієнт кореляції наближається до 0, значить зв’язок між даними слабкий \n") 
    elif  (Corelation()>-1) & (Corelation()<=-0.5):
        res.write("Коефіцієнт кореляції наближається до -1, значить існує сильний лінійний зв’язок між даними \n") 
    elif  (Corelation()>-0.5) & (Corelation()<=0.0):
        res.write("Коефіцієнт кореляції наближається до 0, значить зв’язок між даними слабкий \n") 
    res.write("===================================================\n") 


Task1()
Task2()
Task3()
Task4()
Task5()

res.close()