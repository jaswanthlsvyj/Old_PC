# To assign a string to variable "A"

A = input('enter the string :')

# To be reverse a string and assing to 'B'
B=A[::-1]

#So , if A=B , then it is a palindrome

if A==B:
    print('The string is',A)
    print('It is a palindrome')
else:
    print('The string is ',A)
    print('It is not a palindrome')
    
