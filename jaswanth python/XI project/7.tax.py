# SP = selling price
# sgst = state govt gst
# cgst = central govt gst

item = input('enter the item name :')
SP=float(input('enter the cost of the '+item+' item:'))

#gst = tax
gst=float(input('enter the gst rate of the '+item+':'))
sgst=SP*((gst/2)/100)
cgst=sgst

# The combain of all price = amount
amount = SP+cgst+sgst

print('\n')
print("Item:",item)
print("selling price:",SP)
print("SGST :",sgst)
print("CGST :",cgst)
print("Amount payable :",amount)
