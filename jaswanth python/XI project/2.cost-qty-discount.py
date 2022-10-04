#Amount for given cost-qty-discount
#R_Amo=Real Amount of the product
#Dis_per =Discount percentage
#C_Dispro=cost of discount product

R_Amo=float(input('Enter the real cost of product :'))
Dis_per=float(input('Enter the discount percentage :'))
C_Dispro=R_Amo-(Dis_per*R_Amo/100)

print('\n')
print(R_Amo,'is the real Amount of product')
print(Dis_per,'is the discount percentage')
print(C_Dispro,'is the amount for given cost-qty-discount')
print(R_Amo-C_Dispro,'is the discount amount you got')
