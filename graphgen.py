from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


data=read_csv("records (2).csv").values.tolist()
counter=0
for i in range(len(data)):
    data[i][17]=counter
    if data[i][16]==3 and data[i+1][16]==0:
        counter=counter+1
        print(counter)
#taking the fifteen and sixteen column
# print(data)

fifteen_col=[]
sixteen_col=[]

for i in range(len(data)):
    fifteen_col.append(data[i][15])
    sixteen_col.append(data[i][16])

#taking the fifteen and sixteen column

final_list_ten = []

for i in range(0, 10):
    max1 = 0

    for j in range(len(fifteen_col)):
        if fifteen_col[j] > max1:
            max1 = fifteen_col[j];

    fifteen_col.remove(max1);
    final_list_ten.append(max1)

#print(final_list_ten)
#print(mean(final_list_ten))


##################################

time=[]
ex=[]
ey=[]
ez=[]
accx=[]
accy=[]
accz=[]

for i in range(len(data)):
    if data[i][17]==1:
        time.append(data[i][0])
        ex.append(data[i][1])
        ey.append(data[i][2])
        ez.append(data[i][3])
        accx.append(data[i][4])
        accy.append(data[i][5])
        accz.append(data[i][6])

#print("time",time,"ex",ex,"ey",ey,"ez",ez,"accx",accx,"accy",accy,"accz",accz)
# length=mean(time)*len(time)-5000
# # l=0.6*length
# print(length)
print(time[len(time)-1])
print("$$$$$$$$$$$44")
print(time[0])

length=(0.6*(time[len(time)-1]-time[0])+time[0])
print(length)
print("$$$$$$$$$$$44")
print(mean(time))

# x=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
# y=[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18]

x=[]
y=[]

for i in range(100):
    x.append(length)
    y.append(i)


##########################################################################################  graph
plt.subplot(321)
plt.plot(time, ex, '.-')
plt.plot(x, y, '-')
plt.title('time (s)')
plt.ylabel('ex')

plt.subplot(322)
plt.plot(time, ey, '.-')
plt.plot(x, y, '-')
plt.xlabel('time (s)')
plt.ylabel('ey')

plt.subplot(323)
plt.plot(time, ez, '.-')
plt.plot(x, y, '-')
plt.xlabel('time (s)')
plt.ylabel('ez')

plt.subplot(324)
plt.plot(time, accx, '.-')
plt.plot(x, y, '-')
plt.xlabel('time (s)')
plt.ylabel('accx')

plt.subplot(325)
plt.plot(time, accy, '.-')
plt.plot(x, y, '-')
plt.xlabel('time (s)')
plt.ylabel('accy')

plt.subplot(326)
plt.plot(time, accz, '.-')
plt.plot(x, y, '-')
plt.xlabel('time (s)')
plt.ylabel('accz')


plt.show()

# print(data)
