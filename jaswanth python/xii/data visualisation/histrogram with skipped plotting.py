# To plot a histogram for number of students with no value for range 40-50
import matplotlib.pyplot as plt

Data_students=[5,15,25,35,35,55]
plt.hist(Data_students,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],edgecolor='m')

plt.show()
