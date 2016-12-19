
# coding: utf-8

# In[82]:

import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv('./Views/MDC_MED_TOP_5.csv')
data.sort('Total Patients',ascending=False, inplace=True)

data.plot(y= 'Total Patients',x= 'MDC',kind='bar',color='tomato',legend=False)
plt.xlabel('MDC ID')
plt.ylabel('No of Patients')
plt.xticks(rotation=-10)
fig = plt.gcf()
fig.set_size_inches(9, 9)
plt.title('TOP 5 MDC(MED) based on total no. of patients')
plt.savefig('./Views/v1_1.png')

