
import pandas as pd
import seaborn as sns #Python visualization library
import os
import matplotlib.pyplot as plt

data = pd.read_csv('./stats/out3.csv')
data=data[data['DRG type']=="MED"]

data.info()

for column in ['average_covered_charges', 'average_total_payments', 'average_medicare_payments']:
    data[column] = pd.to_numeric(data[column])
agg_columns = ['mean', 'median', 'var', 'std', 'count', 'min', 'max']
groupby_mdc = data[['mdc_id', 'average_total_payments']].groupby(by='mdc_id').agg(agg_columns)
groupby_mdc.columns = [header + '-' + agg_column
                       for header, agg_column in zip(groupby_mdc.columns.get_level_values(0), agg_columns)]
groupby_mdc.columns = groupby_mdc.columns.get_level_values(0)

groupby_mdc.reset_index(inplace=True)
groupby_mdc['average_total_payments-range'] = groupby_mdc['average_total_payments-max'] - groupby_mdc['average_total_payments-min']
groupby_mdc.head()
groupby_mdc.to_csv('./stats/summarystats_med.csv')


