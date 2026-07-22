name = "Vedanti"
age = 20
cgpa = 8.8
student = True

#type of casting like str, float, boolean, int
print(type(name))
print(type(age))
print(type(cgpa))
print(type(student))

age = float(age)
print(age)
print(type(age))

cgpa = int(cgpa)
print(cgpa)

student = str(student)
print(student)

age = bool(age)
print(age)

age = 0
age = bool(age)
#if we print this when age is zero then the output come as false
print(age)   
#this all is explicit typecasting 

#now we begin with implicit typecasting
x = 2
y = 2.0
x = x/y
y = y/x
print(x)
print(y)