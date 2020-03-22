# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')

#changing the columns dataset on lower case

dataset.columns= map(str.lower, dataset.columns)

#Check column data types
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)


#Convert Columns (join-date & quit-date) on date time

dataset['join_date']= pd.to_datetime(dataset['join_date'])
dataset['quit_date']= pd.to_datetime(dataset['quit_date'])
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)


