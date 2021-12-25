import math
from math import gcd
import random
import collections
import itertools as it

def shuffledNumberListGenerator(size=10, mat=False):
    numbers = []
    for i in range(int(mat), size): numbers.append(i)
    random.shuffle(numbers)
    if mat and size**(0.5).is_integer():
        res = []
        rowSize = int(size**(0.5))
        for i in range(size - 1):
            if i % rowSize == 0: res.append([])
            res[-1].append(numbers[i])
        res[-1].append(0)
        res.reverse()
        res[0].reverse()
        return res
    return numbers

def listOfRandomNumbers(size, low_bound=0, upper_bound=1000, unique=False):
    if not unique: return [random.randint(low_bound, upper_bound) for i in range(size)]
    visited = set()
    items_in_res = 0
    res = []
    while items_in_res < size:
        cand = random.randint(low_bound, upper_bound)
        if cand not in visited:
            visited.add(cand)
            res.append(cand)
            items_in_res += 1
    return res

def listOfRandomLetters(size: int):
    letters, res = list("abcdefghijklmnopqrstuvwxyz"), []
    for _ in range(size): res.append(letters[random.randint(0, 25)])
    return "".join(res)

def listOfRandomPairs(size, low_bound=0, upper_bound=1000):
    res = []
    visited = set()
    for _ in range(size):
        x = random.randint(low_bound, upper_bound)
        if x not in visited:
            res.append([x, random.randint(low_bound, upper_bound)])
            visited.add(x)
    return res
    return [[random.randint(low_bound, upper_bound), random.randint(low_bound, upper_bound)] for _ in range(size)]

def stringMaker(size):
    if size % 2 != 0: size += 1
    entries, res = [str(i) for i in range(10)] + ["?"], ""
    for i in range(size):
        idx = random.randint(0, 10)
        res += entries[idx]
    print("\"%s\""% res)

def bits_maker(length=2):
    upper_bound = 2**length
    for i in range(upper_bound):
        test = [int(i) for i in bin(i)[2:].zfill(length)]
        print(test)


# print(listOfRandomNumbers(20, -50, 40))