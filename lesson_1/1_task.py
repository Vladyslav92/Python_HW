# дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
# 1.1 найти максимум, минимум и их индексы в массиве
# 1.2 найти три самых часто встречаемых элемента массива
# 1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
# 1.3.1 порядок не сохранялся
# 1.3.2 порядок сохранялся

lst = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print('min = {}, index = {}\nmax = {}, index = {}'
      .format(min(lst), lst.index(min(lst)), max(lst), lst.index(max(lst))))
lst2 = []
lst3 = lst

for element in lst:
    if lst.count(element) > 1:
        lst2.append(element)
lst2, lst = set(lst2), set(lst)
lst2.remove(min(lst2))

print('Часто встречаемые три элемента -', list(lst2))
print('Порядок не сохранялся -', lst3)
print('Порядок сохранялся -', list(set(lst)))