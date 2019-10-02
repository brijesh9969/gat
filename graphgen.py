from pandas import read_csv
from pandas import DataFrame
from statistics import mean
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm



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

def plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final):
    print("@@@@@@@@@@@@@@@@@@####################")

    plt.subplot(311)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(max3-2):
        c=next(color)
        plt.plot(time_final3[i], ex_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]
        for j in range(100):
            y_sixty.append(j)

        for j in range(100):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s)')
        plt.ylabel('ex')


    plt.subplot(312)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(max3-2):
        c=next(color)
        plt.plot(time_final3[i], ey_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]
        for j in range(100):
            y_sixty.append(j)

        for j in range(100):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s)')
        plt.ylabel('ey')

    plt.subplot(313)
    color=iter(cm.rainbow(np.linspace(0,1,10)))
    for i in range(max3-2):
        c=next(color)
        plt.plot(time_final3[i], ez_final[i],'.-',c=c,label="cycle"+str(i+1))
        # for()
        x=[]
        y_sixty=[]
        for j in range(100):
            y_sixty.append(j)

        for j in range(100):
            x.append(sixty_percent_final[i])

        plt.plot(x,y_sixty,':',c=c)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.title('time (s)')
        plt.ylabel('ez')





    # plt.subplot(312)
    # for i in range(max3-2):
    #     plt.plot(time_final3[i], ey_final[i], '.-')
    #     plt.title('time (s)')
    #     plt.ylabel('ey')
    #
    #
    # plt.subplot(313)
    # for i in range(max3-2):
    #     plt.plot(time_final3[i], ez_final[i], '.-')
    #     plt.title('time (s)')
    #     plt.ylabel('ez')

    plt.show()



print("XXXXXXXXXXXXXXXXXXXXX")
max2=[]
for i in range(len(data)):
    max2.append(data[i][-1])
# print(max(max2))
max3=max(max2)
sixty_percent=[]
for i in range(len(data)):
    if data[i][17]==j:
        if data[i][16]==2 and data[i+1][16]==3:
            ####finding a value of phase for 60%

            sixty_percent.append(data[i+1][0])

        if(j==max3-1):
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
            # print("j:")
            # print(j)
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



print("########")
##########converting time into percentage


time_final3=[]
print(range(len(time_final)))
sixty_percent_final=[]

for i in range(len(time_final)):
    print(i)
    time_final2=[]
    for j in range(len(time_final[i])):
        time_final2.append((j/len(time_final[i]))*100)
        for k in range(len(sixty_percent)):
            if(time_final[i][j]==sixty_percent[k]):
                # print("KKKKKKKKKKKKkk")
                # print(sixty_percent[k])
                sixty_percent_final.append((j/len(time_final[i]))*100)



    time_final3.append(time_final2)

print(sixty_percent_final)

plottingmap(time_final3,ex_final,ey_final,ez_final,accx_final,accy_final,accz_final,sixty_percent_final)
# plottingmap(time_final3,ey_final,"ey")
# plottingmap(time_final3,ez_final,"ez")
# plottingmap(time_final3,accx_final)
# plottingmap(time_final3,accy_final)
# plottingmap(time_final3,accz_final)
