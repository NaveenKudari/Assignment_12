
# coding: utf-8

# In[22]:


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
boston = load_boston()
bos = pd.DataFrame(boston.data)
bos.columns=boston.feature_names
bos.head()
#Boston.target contains the housing prices.
boston.target[:5]
#add these target prices to the bos data frame.
bos['price']=boston.target
X=bos.drop('price',axis=1)
lm=LinearRegression()
lm.fit(X, bos.price)
#lm.predict()
#print(lm.intercept_)
#pd.DataFrame(zip(X.columns,lm.coef_),columns=['features','estimatedCoefficients'])
print(lm.predict(X))
lm


# In[32]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
df = pd.read_csv(url)
#differ plot color by gender
df['color']=np.where(df['sex']=='female','green','blue')
plt.scatter(df['fare'], df['age'],color=df['color'],label=df['sex'].value_counts(dropna=True))
plt.xlabel("Fare paid")
plt.ylabel("Age")
plt.legend(loc=1)
plt.grid(True)
plt.show()

