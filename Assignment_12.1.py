
# coding: utf-8

# In[69]:


import matplotlib.pyplot as plt
import pandas as pd
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
df =  pd.read_csv(url)
labels='male','female'
male,female=df["sex"].value_counts(dropna=True)
proportions=[male,female]
explode=(0.05,0)
colors = ["#2f44c6", "#ff3f0e"]
fig1,ax1 = plt.subplots()
ax1.pie(proportions,explode=explode,colors=colors,labels=labels,shadow=True, startangle=90,autopct='%1.1f%%')
ax1.axis("equal")
plt.title("Gender Portions")
plt.show()

