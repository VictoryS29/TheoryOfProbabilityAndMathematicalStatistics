######################1
f = open("input1.txt", "rt")
o=open("output1.txt", "w")
arrdata = []
n = 11
for i in range(n):
     x = f.readline()
     arrdata.append(x)
     arrdata[i] = int(arrdata[i].split("\n")[0])

arrdata.remove(arrdata[0])


Cfrequency = []
for i in range(n-1): 
    if i == 0:             
      x = arrdata[i]
      Cfrequency.append(x)
    else:
     x = Cfrequency[i-1]+arrdata[i]
     Cfrequency.append(x)
     
print(Cfrequency)
print()
print("----------------------------------------------------------")
print("Завдання 1")
print("----------------------------------------------------------")
print("Кількість переглядів фільмів || Сукупні частоти ")
for i in range(n-1):
    print(arrdata[i] , "\t\t\t\t\t\t\t\t\t" , Cfrequency[i])

print("---------------")
print("Фільм, який переглядають найчастіше")
print("---------------")
max1=arrdata[0]
moda = 0
f = 0
for i in range(n-1): 
  if arrdata[i]>max1:
      max1=arrdata[i]
      f=i
      moda = i
print(f+1)
o.write("Файл на 10 елементів, фільм, який переглядають найчастіше: " + str(moda+1)+ '\n') # Записати рядок
print("----------------------------------------------------------")
print("Завдання 2")	
print("----------------------------------------------------------")
print("Мода: ", moda+1)
print()

sum2 = 0
sum1 = 0
res = 0
        
for i in range(n-1): 
   sum1 = sum1 + arrdata[i]
   
if (sum1 % 2 == 0):
    el1=sum1/2
    el2=el1+1
    res=(el1+el2)/2   
else: res = sum1/2

for i in range(n-1): 
   if ((res>sum2)) & (res<(sum2+arrdata[i])):
        print("Медіана: ", i+1)
        o.write("Файл на 10 елементів, медіана: " + str(i+1)+ '\n') # Записати рядок    
        break
   sum2=sum2+arrdata[i]
o.write("Файл на 10 елементів, мода: " + str(moda+1)+ '\n') # Записати рядок
   
print("----------------------------------------------------------")
print("Завдання 3")	
print("----------------------------------------------------------")
mean = 0
denominator = 0
numeral = 0
for i in range(n-1): 
   mean += (i+1)*arrdata[i]
   denominator+=arrdata[i]
   numeral += arrdata[i]*(i+1)*(i+1)
 
disp=numeral/denominator
mean /=denominator
mean *= mean
disp -= mean
print("Дисперсія", disp)	
print("Середнє квадратичне відхилення розподілу: ", disp**0.5)	
o.write("Файл на 10 елементів, Дисперсія: " + str(disp)+ '\n') # Записати рядок    
o.write("Файл на 10 елементів, Середнє квадратичне відхилення розподілу: " + str(disp**0.5)+ '\n') # Записати рядок    
print("----------------------------------------------------------")
print("Завдання 4")	
print("----------------------------------------------------------")
 

import matplotlib.pyplot as plt

fig, image = plt.subplots()
imageFilm = []
for i in range(n-1): 
    imageFilm.append(i+1)
    
Imagefrequency = []
for i in range(n-1): 
    Imagefrequency.append(arrdata[i])

bar_colors = ['tab:blue']

image.bar(imageFilm, Imagefrequency, color=bar_colors) 
image.set_ylabel('Frequency')
image.set_xlabel('Movie number')
image.set_title('histogram of frequencies')

plt.show()








