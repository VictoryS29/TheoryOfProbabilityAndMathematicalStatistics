import math
 
res=open("output4.txt", "w") 
  
def CountC(m,n):
    first=math.factorial(n)
    b=n-m
    second= math.factorial(m)*math.factorial(b)
    C=first/second
    return(C)
    
def FindProb(first,second):
    return first/second;

def Task1():
    res.write("===================================================\n") 
    res.write("Завдання 1\n")
    res.write("ймовірність того, що навмання взята коробка виявиться із взуттям червоного або синього кольору\n")
    res.write("=========== \n") 
    black=40
    brown=26
    red=22
    blue=12
    summa=black+brown+red+blue
    result=round(FindProb(red + blue, summa),2)
    res.write(str(result)+"\n") 
    

def Task2():
    res.write("===================================================\n") 
    res.write("Завдання 2\n")
    res.write("ймовірність того, що серед навмання вибраних двох співробітників, хоча б один буде консультантом\n")
    res.write("=========== \n") 
    numb_of_emploees=10
    numb_of_c=8
    first=CountC(2,numb_of_c)*CountC(0,numb_of_emploees-numb_of_c) + CountC(1,numb_of_c)*CountC(1,numb_of_emploees-numb_of_c)
    second=CountC(2,numb_of_emploees)      
    result=round(FindProb(first, second) ,2)
    res.write(str(result)+"\n")                                
 
def Task3():
    res.write("===================================================\n") 
    res.write("Завдання 3\n")
    res.write("ймовірність того, що серед вибраних фахівців буде принаймні один із родичів\n")
    res.write("=========== \n") 
    numb_of_managers=10
    numb_of_f=8
    numb_of_choose = 3
    
    first=CountC(numb_of_choose,numb_of_f) 
    second=CountC(numb_of_choose,numb_of_managers)      
    result= 1 - round(FindProb(first, second) ,2)
 
    res.write(str(result)+"\n")  
 
def Task4():
    res.write("===================================================\n") 
    res.write("Завдання 4\n")
    res.write("ймовірність р5 того, що цей товар призначений для п’ятого відділу\n")
    res.write("=========== \n") 
    p1=0.15
    p2=0.25
    p3=0.2
    p4=0.1
    summa=p1+p2+p3+p4
    result= round(1 - summa,2)
    res.write(str(result)+"\n")  

def Task5():
    res.write("===================================================\n") 
    res.write("Завдання 5\n")
    res.write("ймовірність прибуття двох розбіркових потягів по двох сусідніх коліях\n")
    res.write("=========== \n") 
    numb_of_t=80
    numb_of_k=120
    first=CountC(2,numb_of_t) 
    second=CountC(2,numb_of_k)      
    result= round(FindProb(first, second),2)
    res.write(str(result)+"\n")  
   
def ProbByM(x1,x1prob,x2,x2prob,x3,x3prob):
    return(x1*x1prob+x2*x2prob+x3*x3prob)

def Task6():
     res.write("===================================================\n") 
     res.write("Завдання 6\n")
     res.write("ймовірність виготовлення виробу першого ґатунку станком\n")
     res.write("=========== \n") 
     standart=0.9
     best=0.8
     result= round(ProbByM(standart,best,0,0,0,0),2)
     res.write(str(result)+"\n")  

def Task7():
     res.write("===================================================\n") 
     res.write("Завдання 7\n")
     res.write("ймовірність того, що цей студент підготовлений\n")
     res.write("а)відмінно; б) погано.\n")
     res.write("=========== \n") 
     
     great=3
     good=4
     middle=2
     bad=1
     students=10
     
     greatA=20
     goodA=16
     middleA=10
     badA=5
     studentsA=20
     
     first= (great/students)  * ((greatA)/studentsA) * ((greatA-1)/(studentsA- 1))  *((greatA-1-1)/(studentsA-1-1))
     second=(good/students)   * ((goodA)/studentsA)  * ((goodA-1)/(studentsA- 1))   *((goodA-1-1)/(studentsA-1-1))
     third= (middle/students) * ((middleA)/studentsA)* ((middleA-1)/(studentsA- 1)) *((middleA-1-1)/(studentsA-1-1))
     fourth=(bad/students)    * ((badA)/studentsA)   * ((badA-1)/(studentsA- 1) )   *((badA-1-1)/(studentsA-1-1))
     
     summa=first + second + third + fourth
 
     result= round(FindProb(first, summa),2)
     result2= round(FindProb(fourth, summa),3)
     res.write("a) "+ str(result)+"\n")    
     res.write("б) "+str(result2)+"\n")    
       
def Task8():
    res.write("===================================================\n") 
    res.write("Завдання 8\n")
    res.write("ймовірність того, що навмання взята деталь стандартна\n")
    res.write("=========== \n") 
    
    first=0.4
    second=0.3
    third=0.3
    Sfirst=0.9
    Ssecond=0.25
    Sthird=0.25
    
    result= round(ProbByM(first, Sfirst, second, Ssecond, third, Sthird) ,2)
    res.write(str(result)+"\n")       
     
def Task9():
    res.write("===================================================\n") 
    res.write("Завдання 9\n")
    res.write("ймовірність того, що пацієнт був хворий на перитоніт\n")
    res.write("=========== \n") 
    
    first=0.4
    second=0.3
    third=0.3
    Sfirst=0.8
    Ssecond=0.7
    Sthird=0.85
    summa= ProbByM(first, Sfirst, second, Ssecond, third, Sthird) 
    ch=ProbByM(0, 0, second, Ssecond, 0, 0) 
    result= round(FindProb(ch,summa),2)
    res.write(str(result)+"\n")               
 
def Task10():
    res.write("===================================================\n") 
    res.write("Завдання 10\n")
    res.write("ймовірність того, що він зібраний фахівцем високої кваліфікації\n")
    res.write("=========== \n") 
    
    first=0.3
    second=0.7
 
    Sfirst=0.9
    Ssecond=0.8
 
    summa= ProbByM(first, Sfirst, second, Ssecond,0,0) 
    ch=ProbByM(first, Sfirst, 0, 0,0,0) 
    result= round(FindProb(ch,summa),2)
    res.write(str(result)+"\n")        
    res.write("===================================================\n")  
 
     
Task1()
Task2()
Task3()
Task4()
Task5()
Task6()
Task7()
Task8()
Task9()
Task10()
res.close()

