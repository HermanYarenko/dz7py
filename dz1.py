lst1 = ['пара-ра-рам', 'рам-пам-папам', 'па-ра-па-да']
lst2 = []

for i in lst1:
    summ=0
    for j in i:
        if j in 'а':
            summ +=1
    lst2.append(summ)

if len(lst2) == lst2.count(lst2[0]):
    print('Парам пам-пам')
else:
    print('Пам парам')
print(lst2)
