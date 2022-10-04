# EMI = Equated montly installment
#P=Principal
# R = Rate of interest
# N = no of montly installments

P = float(input('enter principal amount :'))
R = float(input('enter rate of interest per annum :'))

# MR= monthly rate of Interest
MR=R/(12*100)
N=int(input('enter the number of installments :'))
EMI=(P*MR*(1+MR)**N)/(((1+MR)**N)-1)

print("\tEMI Calculation")
print("Principal Amount:",P)
print("Rate of interest :",R)
print("Number of installments :",N)
print("EMI amount :",EMI)
