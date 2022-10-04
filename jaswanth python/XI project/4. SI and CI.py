# To find Simple interest & Compound interest
# Principal =P ,  Rate =R ,  Time = T
# SI=Simple interest , CI=Compound interest

P=float(input('enter the principal amount :'))
R=float(input('enter the rate of interest :'))
T=float(input('enter the years :'))

SI=P*R*T/100
CI=(P*(1-R/100)**T)

print('\n')
print(SI,'is your simple interest')
print(CI,'is your compound interest')
