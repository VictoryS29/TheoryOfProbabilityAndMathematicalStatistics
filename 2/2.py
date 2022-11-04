import numpy as np
import math
import matplotlib.pyplot as plt
data=np.genfromtxt("input_10.txt") 
lenghtArray=data[0]
arrdata = np.delete(data,[0])

res=open("output2.txt", "w")
array=np.sort(arrdata);
def Task1():
    res.write("------------------------------\n")
    res.write("task1\n")
    res.write("------------------------------\n")
    elementFor1=float(0.25*(lenghtArray+1))
    numb=math.floor(elementFor1)
    coefFor1=elementFor1%1
    Q1=float(array[numb-1])+coefFor1*(array[numb]-array[numb-1])
    res.write("Q1: "+ str(Q1))
    res.write("\n")
    
    elementFor2=float(0.75*(lenghtArray+1))
    numb2=math.floor(elementFor2)
    coefFor2=elementFor2%1
    Q3=float(array[numb2-1])+coefFor2*(array[numb2]-array[numb2-1])
    res.write("Q3: "+ str(Q3))
    res.write("\n")
    
    elementFor3=float(0.9*(lenghtArray+1))
    numb3=math.floor(elementFor3)
    coefFor3=elementFor3%1
    P90=float(array[numb3-1])+coefFor3*(array[numb3]-array[numb3-1])
    res.write("P90: "+ str(P90))
    res.write("\n")
    
def Task2():
    res.write("------------------------------\n")
    res.write("task2\n")
    res.write("------------------------------\n")
    SumAll=0
    sumPOW=float(0)
    
    for i in range (0,int(lenghtArray-1)):
        SumAll+=array[i]
        
    middle=SumAll/lenghtArray   
    
    for i in range (0,int(lenghtArray-1)):
     sumPOW+=math.pow((array[i]-middle),2)
     
    d=math.sqrt(sumPOW/(lenghtArray-1))
    res.write("Standart deviation: "+ str(round(d,3)))
    res.write("\n")
    
def Task3():
    res.write("------------------------------\n")
    res.write("task3\n")
    res.write("------------------------------\n")
    sumgrades=0
    for i in range (0,int(lenghtArray)): 
        sumgrades+=array[i]
        
    midgrade=sumgrades/lenghtArray
    
    left=np.array([[midgrade,1],[100,1]])
    right=np.array([95,100])
    result=np.linalg.solve(left,right)
    a=float(result[0])
    b=float(result[1])
    
    arrayChanged=np.arange(lenghtArray, dtype=float)
    
    for i in range (int(lenghtArray)): 
       if(array[i]!=100):
           arrayChanged[i]=float(array[i]*a+b)
       else:
           arrayChanged[i]=array[i]
           
    res.write(str(arrayChanged))
    res.write("\n")
    
def Task4():
 res.write("------------------------------\n")
 res.write("task4\n")
 res.write("------------------------------\n")
 res.write(str(array))
 res.write("\n")
 res.write("------------------------------\n")
 steamMax=int(max(array)/10) 
 steamMin=int(min(array)/10) 
 
 for i in range(steamMin,steamMax):
     res.write(str(i) + "|") 
     for j in (array): 
         if (j<10*i): continue
         if (j>=10*(i+1)): break
         res.write(str(j%10)+"  ") 
     res.write("\n")     
def Task5():
 res.write("------------------------------\n")
 res.write("task5\n")
 res.write("------------------------------\n")
 plt.boxplot(array)
 plt.show()
 
Task1()
Task2()
Task3()
Task4()
Task5()
res.close()