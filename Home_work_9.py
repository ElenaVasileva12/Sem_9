# Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой 
# чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import random
from typing import Callable
import json


#записываем в csv файл по 3 числа в 100-1000 строк
def python_to_csv (csv_file):
    my_gen=[[random.randint(0,50) for _ in range(3)] for _ in range(random.randint(100,1001))] #генерируем 3 случайных числа из 100-1000 строк

    with open(csv_file,'w',encoding='UTF-8') as file:
        write = csv.writer(file,delimiter = ' ',lineterminator='\r')  
        write.writerows(my_gen)


#декоратор берет данные из CSV файла
def decor_import_csv(func:Callable):
    def wrapper(*args,**kwargs):
        a,b,c=args
        data=[]
        with open('namber_three.csv','r',newline='',encoding='UTF-8') as f:
            for line in f:
                data.append([float(x) for x in line.split()])
            for thr_num in data:   
                a,b,c=thr_num[0],thr_num[1],thr_num[2]
                func(a,b,c,**kwargs)
                
                #print(func(a,b,c))
            return func(a,b,c)
    return wrapper

#декоратор скидывает данные в json
def decor_to_json(func:Callable):
    open('namber_three.json',"w").close()
    def wrapper(*args,**kwargs):
        data={}
        file_name='namber_three.json'
        result=func(*args,**kwargs)
        data[(args.__repr__())]=result

        with open(file_name,'a',encoding='UTF-8') as file:
            json.dump(data,file,indent=4,ensure_ascii=False )
            print(data)
            
        return data
    return wrapper


# квадратное уравнение
@decor_import_csv
@decor_to_json
def quadratic_equation(a:float,b:float,c:float):
    discriminant=b*2-4*a*c
    if discriminant>0:
        x1=(-b+discriminant**0.5)/2*a
        x2=(-b-discriminant**0.5)/2*a
        s=(f'Уравнение имеет 2 корня {x1} и {x2}')
    elif discriminant==0:
        x1=(-b+discriminant**0.5)/2*a
        x2=None
        s=(f'Уравнение имеет 1 корень {x1}')
    else:
        x1=x2=None
        s=(f'Уравнение не имеет корней')
    #print(s)
    return s

python_to_csv('namber_three.csv')
quadratic_equation(1,-2,-3)





