import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

pwd = os.getcwd()
print(pwd)

data = pd.read_csv('posal.csv')
print(data.shape)
print(data)
#data.head()
