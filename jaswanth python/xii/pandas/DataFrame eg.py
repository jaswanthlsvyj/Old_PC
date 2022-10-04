import pandas as pd
import numpy as np



# for simple eg for DataFrame

a=[10,20,30,40,50]
b=[90,80,70,60,50]

c=pd.DataFrame(b)
print(b,'\n')
print(c,'\n')

stu_marks=({'ram':100,'kumar':200,'sai':300})

stu_age=({'ram':18,'kumar':17,'sai':16})

stu_info= pd.DataFrame({'Marks':stu_marks,'age':stu_age})

print(' Data Frame for students','\n',stu_info)

