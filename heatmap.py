
# coding: utf-8

# In[ ]:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:

df = pd.read_csv('./Views/out.csv')

mdc_by_state = df.groupby(by=['provider_state', 'mdc_id'])['average_total_payments'].sum()

mdc_by_state = mdc_by_state.transpose()

mdc_by_state.sort_values(ascending=False, inplace=True)

new_df = pd.DataFrame(index=list(df.provider_state.unique()), columns=list(df.mdc_id.unique()))

idx = list(df.provider_state.unique())

for item in idx:
    new_df.loc[item] = mdc_by_state.get(item).to_dict()

new_df.fillna(0, inplace=True)



# w, h = plt.figaspect(1.)
sns.set()
# sns.set(context="paper", font="monospace")
fig = plt.figure(figsize=(7,12))
sns.heatmap(new_df, square=True, cbar=True, linewidths=0.5)
plt.xlabel('MDC ID')
plt.ylabel('State')
plt.yticks(rotation=0)
plt.xticks(rotation=0)
plt.title("Total Payments by State for MDC", fontsize=18)
fig.savefig('./Views/v5.png')


# In[ ]:

new_df2=new_df.transpose()
fig = plt.figure(figsize=(10,10))
sns.heatmap(new_df2, square=True, vmin=0, cbar=True, linewidths=1)
plt.xlabel('State')
plt.ylabel('MDC ID')
plt.yticks(rotation=0)
plt.xticks(rotation=0)
plt.title("Cost of MDC ID Per State", fontsize=18)
fig.savefig('./Views/v6.png')





