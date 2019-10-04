from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm



data=read_csv("records1.csv").values.tolist()
counter=0
# print(data)
print("%%%%%%%%%")
for i in range(len(data)):
    data[i][17]=counter
    if data[i][16]==3 and data[i+1][16]==0:
        counter=counter+1
        print("KKKKKKKKKK")
        print(counter)
#taking the fifteen and sixteen column
# print(data)

# for i in range(len(data)):
#     print(len(data[i]))


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
# j=1

print("XXXXXXXXXXXXXXXXXXXXX")
max2=[]
for i in range(len(data)):
    max2.append(data[i][-1])
# print(max(max2))
max3=max(max2)
sixty_percent=[]
