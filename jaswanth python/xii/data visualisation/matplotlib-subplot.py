import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0.0,20.0,1)
s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
s2=[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

plt.subplot(2,1,1)
plt.ylabel('value')
plt.title('First chart')
plt.grid(False)
plt.plot(t,s)
plt.subplots_adjust(hspace=0.4, wspace=0.4)

plt.subplot(2,1,2)
plt.xlabel('items')
plt.ylabel('Value')
plt.title('\n second chart')
plt.plot(t,s2)
plt.grid(True)
plt.show()
