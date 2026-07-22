doubles = []
for i in range(1, 11):
    doubles.append(i*2)  

doubles = [i*2 for i in range(1, 11)]
triples = [i*3 for i in range(1, 11)]
squares = [i*i for i in range(1, 11)]

print(doubles)

#string in comprehension

fruits = [fruit.upper() for fruit in ["apple", "banana", "coconut", "lichi"]]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)

#numbers in comprehension
numbers = [1, -2, -3, 4, -5, 6, -7, 8, -9, 10]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)

#grades
grades = [10, 25, 40, 55, 65, 61, 70, 85, 90]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)