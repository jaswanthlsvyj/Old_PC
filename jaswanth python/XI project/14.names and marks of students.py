# create a dictionary of students to store names and marks obtained in 5 subjects

students=dict()
n= int(input(' how many students are there: '))
for i in range(n):
      sname = input('enter name of the student :')
      marks=[]
      for j in range(5):
            mark= float(input('enter marks:'))
            marks.append(mark)
      students[sname]= marks

print( " created dictionary of students is", students)
