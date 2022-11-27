from itertools import product


def permutation(alist: list, option: int) -> list:
    for elem in alist:
        if type(elem) != list:
            alist[alist.index(elem)] = [elem]
    res = list(product(*alist))
    if option > len(res):
        option -= len(res)
    return list(res[option - 1])


example = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

assert permutation(example, 1) == [0, 0, 0]
assert permutation(example, 138) == [1, 3, 7]
assert permutation(example, 1012) == [0, 1, 1]

example2 = [
  [False, True],
  0,
  ['first', 'second', 'third']
]

assert permutation(example2, 4) == [True, 0, 'first']
