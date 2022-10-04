import matplotlib.pyplot as plt
import numpy as np

s=['1st','2nd','3rd']
per_sc=[95,89,77]
per_com=[90,93,75]
per_hum=[97,92,77]
x=np.arange(len(s))

plt.bar(x,per_sc,label='science',width=0.25,color='g')
plt.bar(x+.25,per_com,label='commerce',width=0.25,color='r')
plt.bar(x+.50,per_hum,label='humanities',width=0.25,color='gold')

plt.xticks(x,s)
plt.xlabel('position')
plt.ylabel('percentage')
plt.title('bar graph for result analysis')
plt.legend()
plt.show()
