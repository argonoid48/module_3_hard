# Галкин Андрей
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    summ = 0

    for i in args:
        if isinstance(i, (list, tuple, set)):
            summ += calculate_structure_sum(*i)

        elif isinstance(i, dict):
            summ += calculate_structure_sum(*i.items())

        elif isinstance(i, str):
            summ += len(i)

        elif isinstance(i, (int, float)):
            summ += i

    return summ

print( calculate_structure_sum(data_structure))

