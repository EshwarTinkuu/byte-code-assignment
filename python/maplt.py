
# matplotlib :-- day 1
# what is matplotlib ?
# matplotlib is a py lib which is used to build graphs and charts to represent data graphically & visaully

# # why we use matplotlib ?
# we use to plot graphs 
# we use compare data 
# we use to build DS and ML visaul represenatation
# find noisy data 
# find outliers
# etc..

# # how to install matplotlib ?
# pip install matplotlib 

import matplotlib.pyplot as plt

# matplotlib :-- 
# line chart  -- plot 
# bar -- 
# barh -- horizantal bars
# pie -- 
# scatter plot -- 



# line chart -- plot :

# data
import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

plt.plot(months,revenue)

plt.show()


# -- bar chart :-- 
# how to giev unique color to each bar ? research num - 1

import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

plt.bar(months,revenue,color="yellow")

plt.show()


# # barh:-- 

import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

plt.barh(months,revenue)

plt.show()


# pi-chart :-- 
import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

plt.pie(revenue,labels=months,autopct="%1.1f%%")

plt.show()

# scatter - plot :--- 
import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

# # marker :-- 
# # o - circle
# # s- sqaure
# # * - star
# # ^ -- upwards traingle
# # v -- downwards traingle
# # color :-- color giving 

plt.scatter(months,revenue,color="red",marker="v",s=10,edgecolors="black")

plt.show()


# multiple plots - lines :-- 
months=["jan","feb","mar","apr","may"]

dairy_milk=[100000,140000,120000,80000,950000]
kit_kat=[10000,140000,140000,90000,1050000]
fiveStar=[50000,80000,1120000,180000,1950000]

plt.plot(months,dairy_milk,color="green",marker="*",label="dairy_milk")
plt.plot(months,kit_kat,color="red",marker="s",label="kit_kat")
plt.plot(months,fiveStar,color="orange",marker="o",label="fiveStar")

plt.legend()
plt.show()