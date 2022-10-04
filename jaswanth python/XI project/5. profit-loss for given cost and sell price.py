# C = cost of the product
# SP = selling price of the product

C=float(input('enter the cost of the product :'))
SP=float(input('enter the selling price of the product :'))

# let the variable 'A' be the difference of cost and sell price

A=SP-C
if A<0:
    print('You have a loss of ',A)
else:
    print('You have a profit of ',A)
