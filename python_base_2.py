age = 23
if age < 20:
    print('Error')
    print('Error')
    if age <15:
        print('Fatal')
    else:
        print('Not fatal')
elif age < 25:
    print('<25')
else:
    print('Ok')
print('Next')


# цикл FOR

numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = 10
# for i in range(5,N,2):
#     print(i)
# for i in range(N,0,-1):
#     print(i)

cars = ['bmv', 'audi', 'lada']
# for car in cars:
#     print(car)

# for ind in range(len(cars)):
#     print(ind)
#
# print (cars[0])
# print (cars[-1])

# for ind in range(len(cars)):       # выводится индес+название
#     print(ind,cars[ind])

a = 10
b = 0
while a < 20:
    print(a)
    b += 1
    if b == 15:
        break
