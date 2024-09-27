# создаем список из чисел от 1 до 16
numbers = []
for num in range(1,16):
    numbers.append(num)
print(numbers)

# создаем списоки для сбора значений сортировки
list_prime = []
list_noprime = []

# запускаем цикл по значениям списка
for i in numbers:
    '''
    проверяем число на деление без остатка на 
    делители которые в 2 раза меньше делимого + 1
    '''
    for a in range(2, (i // 2) + 1):
       # если делится значит число не простое
       if i % a == 0:
           list_noprime.append(i)
           break
    '''
    если число отсутвуе в списке не простых чисел 
    после работы цикла, значит число простое
    '''
    if i not in list_noprime:
        list_prime.append(i)

list_prime.remove(1)

#вывод
print('Prime: ',list_prime)
print('No prime: ',list_noprime)


