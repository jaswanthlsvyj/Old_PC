import pandas as pd
student={'sname':['ram','kumar','shashank','varma','yugendra'],
	'height in cm':[165,172,163,178,160],
	 'weight in kg':[50,56,63,71,69],
	 'state':['ap','ap','assam','hp','ap']}


print('As the given series:','\n',student)

stu_info1=pd.DataFrame(student)
print('\n')
print(stu_info1)
