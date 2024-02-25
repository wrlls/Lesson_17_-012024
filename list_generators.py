"""numbers = [1,2,3,4,5,6,7,8,100]
result = []
for number in numbers:
    if number > 5 and number <50:
        result.append(number)
print(result)
"""

"""result = filter(lambda number:number >5 and number < 50, numbers)
print(list(result))
"""
"""numbers = [2, 3,4,5,6,7,8,100,54,32,25 ]
result = [number for number in numbers if number // 2  and number < 50]
print(result)
"""

"""names = ['leo', 'max', 'kate', 'mag']
new_names = []
for name in names:
    if name[0] == 'm':
        new_names.append(name.upper())
print(new_names)
"""

"""numbers = [1,2,3,4,5,6,7,8,9]
new_num = []
for number in numbers:
    if number<5:
        new_num.append(0)
    else:
        new_num.append(1)
print(new_num)
"""

result012 = {i:i**2 for i in range(1, 10)}
print(result012)