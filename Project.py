# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')
#df=pd.DataFrame(dataset)
dataset.columns= map(str.lower, dataset.columns)
