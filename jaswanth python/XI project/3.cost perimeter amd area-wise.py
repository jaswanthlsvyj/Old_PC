#To calculate cost perimeter/area -wise
#C_p_m=cost per meter
#C_p_a=cost per area

a=input('enter the shape of the object(square [1] or rectangle [2] or triangle [3]):')

#Cpm=total cost per meter
#Cpa=total cost per area

if a=='1':
    b=float(input('enter the size of side:'))
    perimeter=4*b
    area=b**2
    C_p_m=float(input('cost per unit meter :'))
    C_p_a=float(input('cost per unit area :'))
    Cpm=perimeter*C_p_m
    Cpa=area*C_p_a
    print(Cpm,'is the total cost in perimeter wise')
    print(Cpa,'is the total cost in area wise')

if a=='2':
    b=float(input('enter the length :'))
    c=float(input('enter the breath :'))
    C_p_m=float(input('enter the cost of unit perimeter:'))
    C_p_a=float(input('enter the cost of unit area :'))
    perimeter=2*(b+c)
    area=b*c
    Cpm=perimeter*C_p_m
    Cpa=area*C_p_a
    print(Cpm,'is the total cost in perimeter wise')
    print(Cpa,'is the total cost in area wise')

if a=='3':
    e=float(input('enter the size of 1st side of triangle :'))
    f=float(input('enter the size of 2nd side of triangle :'))
    g=float(input('enter the size of 3rd side of triangle :'))
    perimeter=e+f+g
    s=(e+f+g)/2
    area=(s*(s-e)*(s-f)*(s-g))**1/2
    C_p_m=float(input('enter the cost of unit perimeter:'))
    C_p_a=float(input('enter the cost of unit area :'))
    Cpm=perimeter*C_p_m
    Cpa=area*C_p_a
    print(Cpm,'is the total cost in perimeter wise')
    print(Cpa,'is the total cost in area wise')
