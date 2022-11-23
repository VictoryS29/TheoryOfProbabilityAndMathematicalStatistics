import math
import sympy as sp
 
res=open("output5.txt", "w") 
  
 
def CountC(m,n):
    first=math.factorial(n)
    b=n-m
    second= math.factorial(m)*math.factorial(b)
    C=first/second
    return(C)
    
def integral(t):
    x = sp.Symbol('x')
    expr = sp.exp(-x**2 / 2)
    return sp.integrate(expr, (x, 0, t))

def Bernulli(p,q,m,n):
    result=CountC(m,n)*(p**m)*(q**(n-m))
    return result

#Локальна теорема Муавра-Лапласа
def Local_Muavr_Laplas(n,k,p,q):
    X=(k-n*p)/(math.sqrt(n*p*q))
    F = (1/math.sqrt(2*math.pi))*math.exp(X**2/2)
    result =(1/math.sqrt(n*p*q))*F
    return result

#Теорема Пуассона
def Puasson(n,p,m):
    L=n*p
    result=((L**m)/math.factorial(m)) * math.exp(-L)
    return result

#Інтегральна теорема Муавра-Лапласа
def Integral_Muavr_Laplas(n,p,q,m1,m2):
    X1=(m1-n*p)/math.sqrt(n*p*q)
    X2=(m2-n*p)/math.sqrt(n*p*q)
    if (abs(X1)<5) &  (abs(X2)<5):
        F1=float(integral(X1)/math.sqrt(2*math.pi))
        F2=float(integral(X2)/math.sqrt(2*math.pi))
    else:
        F2=float(integral(X1)/math.sqrt(2*math.pi))
        F1=-0.5
    result= F2-F1
    return result

def Task1():
    res.write("===================================================\n") 
    res.write("Завдання 1\n")
    res.write("ймовірність того, що в трьох із п’яти потягів, які прибувають протягом однієї години, будуть вагони на дане призначення\n")
    res.write("=========== \n") 

    p=0.2
    q=1-p
    m=3
    n=5
    result=round(Bernulli(p,q,m,n),3)
    res.write(str(result)+"\n") 

def Task2():
    res.write("===================================================\n") 
    res.write("Завдання 2\n")
    res.write("Знайти ймовірність того, що в п’яти незалежних випробуваннях подія А відбудеться:\n")
    res.write("а)рівно 4 рази; б)не менше 4 разів \n")
    res.write("=========== \n") 
 
    p=0.8
    q=1-p
    m=4
    n=5

    result=round(Bernulli(p,q,m,n),3)
    result2=result+round(Bernulli(p,q,m+1,n),3) 
    res.write(str(result)+"\n") 
    res.write(str(result2)+"\n") 
 
def Task3():
    res.write("===================================================\n") 
    res.write("Завдання 3\n")
    res.write("ймовірність того, що серед 400 вибраних навмання цукерок буде рівно 80 льодяників\n")
    res.write("=========== \n") 
    
    n=400
    k=80
    p=0.2
    q=1-p

    result =round(Local_Muavr_Laplas(n,k,p,q),5)
    
    res.write(str(result)+"\n") 
 
def Task4():
    res.write("===================================================\n") 
    res.write("Завдання 4\n")
    res.write("ймовірність того, що з конвеєра зійшло 5 бракованих автомобілів\n")
    res.write("=========== \n") 
    n=100000
    p=0.0001
    m=5
    result= round(Puasson(n,p,m),3)
    res.write(str(result)+"\n")  
 
def Task5():
    res.write("===================================================\n") 
    res.write("Завдання 5\n")
    res.write("ймовірність того, що серед 600 пар, які поступили на контроль, виявиться від\n")
    res.write("228 до 252 пар взуття вищого ґатунку \n")
    res.write("=========== \n") 
    
    n=600
    p=0.4
    q=1-p
    m1=228
    m2=252
  
    result= round(Integral_Muavr_Laplas(n,p,q,m1,m2) ,4)
    res.write(str(result)+"\n")  


def Task6():
     res.write("===================================================\n") 
     res.write("Завдання 6\n")
     res.write("найімовірніше число вимог клієнтів кожного дня, та його ймовірність\n")
     res.write("=========== \n") 
     
     clients=100
     p=0.4
     q=1-p
     number=clients*p
     res.write("1)"+ str(number) + " \n") 

     n=clients
     k=number
     X=(k-(n*p))/math.sqrt(n*p*q)
     F = (1/math.sqrt(2*math.pi))*math.exp(X**2/2)
 
     Pres=round(F/math.sqrt(n*p*q),3)
     
     res.write("2)"+ str(Pres) + " \n") 
  
def Task7():
     res.write("===================================================\n") 
     res.write("Завдання 7\n")
     res.write("ймовірність того, що число нестандартних виробів у партії з 4000 штук не більше 170\n")
     res.write("=========== \n") 
     
     n=4000
     p=0.04
     q=1-p
     m1=170
     m2=0
 
     result= round(Integral_Muavr_Laplas(n,p,q,m1,m2),3)   
     res.write(str(result)+"\n")    
 
def Task8():
    res.write("===================================================\n") 
    res.write("Завдання 8\n")
    res.write("ймовірність того, що при 10000 незалежних киданнях монети герб випаде 5000 разів\n")
    res.write("=========== \n") 
    
    n=10000
    p=0.5
    q=1-p
    k =5000
    
    result= round(Local_Muavr_Laplas(n,k,p,q),5)
 
    res.write(str(result)+"\n")       
 
def Task9():
    res.write("===================================================\n") 
    res.write("Завдання 9\n")
    res.write("ймовірність того, що на базу прибуде 5 пошкоджених виробів\n")
    res.write("=========== \n") 
    
    n=1000
    p=0.002
    m=5
    
    result= round(Puasson(n,p,m),3)
    res.write(str(result)+"\n")        
     
def Task10():
    res.write("===================================================\n") 
    res.write("Завдання 10\n")
    res.write("найімовірніше число випадків правильної роботи автомату, якщо буде кинуто 150 монет\n")
    res.write("=========== \n") 
    
    n=150
    q=0.03
    p=1-q
    k1= n*p-q
    k2= n*p+p
    if (k1>k2):
        t=k1
        k1=k2
        k2=t
    result= math.ceil(k1)
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


