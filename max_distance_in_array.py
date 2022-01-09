a=[10,9,12,1]
numbers=[]
for i,b in enumerate(a):
    numbers.append((b,i))

numbers.sort()
print(numbers)
minNumber=numbers[2]
print(numbers[3][1])
for items in numbers:
    print(items)