'''
Функція динамічного програмування find_min_coins.
Ця функція також повинна приймати суму для видачі решти,
але використовувати метод динамічного програмування,
щоб знайти мінімальну кількість монет,
необхідних для формування цієї суми.
Функція повинна повертати словник із номіналами монет
та їх кількістю для досягнення заданої суми найефективнішим способом.
Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
'''

def find_coins_greedy(items, capacity):
    n = 0
    value = []
    count_dict = {}
    
    while sum(value) != capacity and n < len(items):
        if capacity >= items[n]:
            value.append(items[n])
            capacity -= items[n]
        else:
            n += 1
    
    for val in value:
        if val not in count_dict:
            count_dict[val] = 1
        else:
            count_dict[val] += 1
    
    return count_dict

def find_min_coins(items, capacity):
    pass



print(find_coins_greedy([50, 25, 10, 5, 2, 1], 113))
print(find_min_coins([50, 25, 10, 5, 2, 1], 113))