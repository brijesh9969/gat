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
time_final=[]
ex_final=[]
ey_final=[]
ez_final=[]
accx_final=[]
accy_final=[]
accz_final=[]
j=1
for i in range(len(data)):
    if data[i][17]==j:
        # q=j+1
        if(j==8):
            break
        elif data[i][17]==j and data[i+1][17]==j+1:

            time_final.append(time)
            ex_final.append(ex)
            ey_final.append(ey)
            ez_final.append(ez)
            accx_final.append(accx)
            accy_final.append(accy)
            accz_final.append(accz)
            time=[]
            ex=[]
            ey=[]
            ez=[]
            accx=[]
            accy=[]
            accz=[]
            print("j:")
            print(j)
            j+=1
        # a2=data[i][0]
        # b2=len(data)
        time.append((data[i][0]))
        ex.append(data[i][1])
        ey.append(data[i][2])
        ez.append(data[i][3])
        accx.append(data[i][4])
        accy.append(data[i][5])
        accz.append(data[i][6])
    # elif data[i][17]==1 and data[i+1][17]==2:
    #     da
print("########")
# print(time_final)
# x=[]
time_final3=[]
print(range(len(time_final)))

for i in range(len(time_final)):
    print(i)
    time_final2=[]
    for j in range(len(time_final[i])):
        print(j)
        # print("Okkkkkkkkkkkkk")
        time_final2.append((j/len(time_final[i]))*100)
    time_final3.append(time_final2)

print("@@@@@@@@@@@@@@@@@@####################")
# print(time_final2)
# for i in time_final3:
print(time_final3)

# for i in time_final2:
#     print(i)


k=1
for i in range(6):
    # x=str(32)+str(k)
    # q='#'+str(i+2)*6
    # print(q)
    # print(ex_final[i])
    # print(len(ex_final[i]))
    plt.plot(time_final3[i], ex_final[i], '.-')

    plt.title('time (s)')
    plt.ylabel('ex')
    k+=1
plt.show()
#print("time",time,"ex",ex,"ey",ey,"ez",ez,"accx",accx,"accy",accy,"accz",accz)
# length=mean(time)*len(time)-5000
# # l=0.6*length
# print(length)
# print(time[len(time)-1])
# print("$$$$$$$$$$$44")
# print(time[0])
#
# length=(0.6*(time[len(time)-1]-time[0])+time[0])
# print(length)
# print("$$$$$$$$$$$44")
# print(mean(time))
#
# # x=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
# # y=[1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18]
#
# x=[]
# y=[]
#
# for i in range(100):
#     x.append(length)
#     y.append(i)
