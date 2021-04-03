from typing import Dict

n = int(input())
from random import randint

list = []
list1 = []
for i in range(0, n):
    list.append({'x': randint(-100, 100), 'y': randint(-100, 100)})
print(list)
import math

for i in range(len(list)):
    x = list[i].get('x')
    y = list[i].get('y')
    list[i]['a'] = abs(math.degrees(math.atan(y/x)))


for i in range(len(list)):

    if list[i]['x'] > 0 and list[i]['y'] > 0:
        g = list[i]['a']
        list[i]['b'] = g
    elif list[i]['x'] < 0 and list[i]['y'] > 0:
        g = 180- list[i]['a']
        list[i]['b'] = g
    elif list[i]['x'] < 0 and list[i]['y'] < 0:
        g = 180 + list[i]['a']
        list[i]['b'] = g
    elif list[i]['x'] > 0 and list[i]['y'] < 0:
        g =  360- list[i]['a']
        list[i]['b'] = g


print(list)
print(sorted(list, key=lambda x: x['b'])) #выводим сортированный список против часовой стрелки начиная с первой четверти
for i in range(len(list)):
    list1.append(math.hypot(list[i]['x'],list[i]['y']))
m = max(list1) # максимальное расстояние от начала координат до точки
k = min(list1) # минимаьлное расстояние от начала координат до точки
s = sum(list1)/len(list1) #среднее расстояние от начала координат до точки
print(m,k,s)

    