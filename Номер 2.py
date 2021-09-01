print('x | y | z')
for x in range(0, 2): # Кол-во циклов соответствует кол-ву переменных, в них мы рассматриваем 2 значения переменной 0 и 1
    for y in range(0, 2):
        for z in range(0, 2):
            if ((not x) and y and z) == 1 or ((not x) and y and (not z)) == 1 or ((not x) and (not y) and (not z)) == 1: #(¬x ∧ y ∧ z) ∨ (¬x ∧ y ∧ ¬z) ∨ (¬x ∧ ¬y ∧ ¬z)
                print(x, '|', y, '|', z)

# В if пишем условие из задания, где:
# or - дизьюнкция
# and - коньюнкция
# not - инверсия
# == 1 - правда
# == 0 - ложь

# !!!Важно: не забывайте скобки в условии, т.к. от них напрямую зависит конечный результат

#Условие: https://inf-ege.sdamgia.ru/problem?id=9788
#Подробнее смотреть в ролике: https://www.youtube.com/watch?v=vOYqwx6YDoM&t=565s