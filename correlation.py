
# coding: utf-8

# In[1]:

# lib imports
import pandas as pd
import matplotlib.pyplot as plt

# this allows plots to appear directly in the notebook
get_ipython().magic('matplotlib inline')


# In[2]:

data = pd.read_csv('./Views/MDC_by_SuperRegion_and_ProviderCount.csv')
data.head()


# In[3]:

data.shape


# In[5]:

# fig = plt.figure()
data.plot(kind='scatter', x='Patients', y='average_total_payments')
fig = plt.gcf()
fig.savefig('./Visualizations/corr1.png')



# In[86]:

data.plot(kind='scatter', x='Patients', y='average_total_payments')
fig = plt.gcf()
fig.savefig('./Visualizations/corr1.png')


# In[35]:

data.columns


# In[27]:


# this is the standard import if you're using "formula notation" (similar to R)
import statsmodels.formula.api as smf

# create a fitted model in one line
lm = smf.ols(formula='average_total_payments ~Number_of_Providers  ', data=data).fit()

# print the coefficients
lm.params


# In[28]:

X_new = pd.DataFrame({'Number_of_Providers': [data.Number_of_Providers.min(), data.Number_of_Providers.max()]})
X_new.head()


# In[29]:

lm.predict(X_new)


# In[30]:

preds = lm.predict(X_new)
preds


# In[32]:

# first, plot the observed data
data.plot(kind='scatter', y='average_total_payments', x='Number_of_Providers')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)
fig = plt.gcf()
fig.savefig('./Visualizations/corr2.png')




# In[12]:

lm.rsquared


# In[33]:

import statsmodels.formula.api as smf
# create a fitted model in one line
lm = smf.ols(formula='average_total_payments ~Patients', data=data).fit()

# print the coefficients
lm.params


# In[34]:

X_new = pd.DataFrame({'Patients': [data.Patients.min(), data.Patients.max()]})
X_new.head()


# In[35]:

lm.predict(X_new)


# In[36]:

preds = lm.predict(X_new)
preds


# In[37]:

# first, plot the observed data
data.plot(kind='scatter', y='average_total_payments', x='Patients')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)
fig = plt.gcf()
fig.savefig('./Visualizations/corr1.png')




# In[24]:

lm.rsquared

