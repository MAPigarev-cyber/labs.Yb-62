a=input("Название заказа: ")
b=input("Имя заказчика: ")

name1=input("Название первой позиции: ")
qolvo1=int(input("Количество первой позиции: "))
cenna1=float(input("Цена первой позиции в рублях: ").replace(",", "."))

name2=input("Название второй позиции: ")
qolvo2=int(input("Количество второй позиции: "))
cenna2=float(input("Цена второй позиции в рублях: ").replace(",", "."))

dost=float(input("Стоимость доставки в рублях: ").replace(",","."))
skid= float(input("Скидка на товары (%): ").replace(",", "."))
cymma=float(input("Внесённая сумма в рублях: ").replace(",", "."))

stm1= qolvo1*cenna1          
stm2= qolvo2*cenna2          
c=stm1+stm2         
        
skidrub=c*skid/100   
dskid=c-skidrub         
gskid=dskid+dost             
qolvo=qolvo1+qolvo2           
sdacha=cymma-gskid                 

print("Заказ:",a)
print("Заказчик:",b)

print(name1, "|", qolvo1, "|",f"{cenna1:.2f}", "|", f"{stm1:.2f}")
print(name2, "|", qolvo2, "|",f"{cenna2:.2f}", "|", f"{stm2:.2f}")

print("Товары без доставки:",f"{c:.2f}")
print("Скидка (%):", f"{skid:.2f}")
print("Скидка (руб.):", f"{skidrub:.2f}")
print("Товары со скидкой:", f"{dskid:.2f}")
print("Доставка:",f"{dost:.2f}")
print("Итог с доставкой:",f"{gskid:.2f}")
print("Общее количество единиц:",qolvo)
print("Сдача:",f"{sdacha:.2f}")
