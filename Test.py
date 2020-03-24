import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dtime

#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')

#changing the columns dataset on lower case

dataset.columns= map(str.lower, dataset.columns)


dfPlot=dataset[['join_date','salary']]
dfPlot.plot.box(dfPlot,y="salary")