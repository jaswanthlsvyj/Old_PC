# 1) Create a panda’s series from a dictionary of values and a ndarray

import pandas as pd
import numpy as np

#creating a series 
ser=pd.Series(np.array([1,2,3,4,54,643,2,6]))

print('the series we created')
print(ser)
print('\n')

# cerate a dictionary of values
dic={'a':1,'b':4,'c':5,'d':9}
ser1=pd.Series(dic)

print(" dictionary of values")
print(ser1)


