# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input()
height = input()

weight = int(weight)
height = int(height)


print("Your BMI is {:.2f}".format(10000*weight/(height*height)))
print(f"Your BMI is {10000*weight/(height*height):.2f}")