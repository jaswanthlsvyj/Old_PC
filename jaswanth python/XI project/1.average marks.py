# average marks for the given subjects
'''IP=Informatices pratices
ENG=English
MAT=Maths
PHY=Physics
CHE=Chenistry
TOT_MAR=Total marks'''

IP=float(input('enter your informatices pratices marks :'))
ENG=float(input('enter your english marks :'))
MAT=float(input('enter your maths marks :'))
PHY=float(input('enter your physics marks :'))
CHE=float(input('enter your chemistry marks :'))
TOT_MAR=float(input('enter your total marks that exam conducted :'))

#TOT=total marks got by user
TOT=IP+ENG+PHY+CHE+MAT
#AVG=average marks
AVG=TOT/5
#PER =percentage
PER=TOT/TOT_MAR*100

print('total marks you got:',TOT)
print('average marks you got:',AVG)
print('percentage you got:',PER)

if PER>90:
    print('Your grade is A+')
elif 91>PER>80:
    print('Your grade is B+')
elif 81>PER>70:
    print('YOur grade is C+')
else:
    print('You are too low')
    print('better luck next time')
