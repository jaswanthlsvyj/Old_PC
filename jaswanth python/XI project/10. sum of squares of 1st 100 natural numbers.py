# Let 'b' be the variable for 0

b=0

# So by using the range command
for a  in range(1,101):
    a=a**2
    b+=a

print(b,'is the sum of squares of the 1st 100 naturalnumbers')
