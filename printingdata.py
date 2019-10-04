from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm



data=read_csv("records (3).csv").values.tolist()
data2=read_csv("records (3).csv").values.tolist()

print(data2)
print("########")
counter=0
for i in range(len(data)):
    data[i][17]=counter
    if data[i][16]==3 and data[i+1][16]==0:
        counter=counter+1
        print(counter)
#taking the fifteen and sixteen column
print(data)
