import functools
import random


# question := 1

def splitIntoChars(word: str) -> list:
    """
    Function that return list of charcters of a given string. 
    >>> splitIntoChars("abcdef")
    ['a', 'b', 'c', 'd', 'e', 'f']
    >>> splitIntoChars("cloud")
    ['c', 'l', 'o', 'u', 'd']
    """
    return list(word)


# question := 2
def stringFromChars(letters: list) -> str:
    """
    Function that return string from a given list of chars.
    >>> stringFromChars(['a', 'b','c','d','e','f'])
    'abcdef'
    >>> stringFromChars(['c','l','o','u','d'])
    'cloud'
    """
    s = ""
    for char in letters:
        s += char
    return s


# question := 3


def generateRandomNumber(n: int) -> list:
    """
    A function that return list of random n integer from range (1->n).
    >>> generateRandomNumber(5) # doctest: +SKIP
    >>> generateRandomNumber(8) # doctest: +SKIP
    """
    a = [random.randint(1, n) for x in range(n)]
    return a


# question := 4
def sortList(num_list: list) -> list:
    """
    A function thst sort num_list into reverse order
    >>> sortList([1,2,3,4,5])
    [5, 4, 3, 2, 1]
    >>> sortList([3,6,3,2,5])
    [6, 5, 3, 3, 2]
    """
    num_list.sort(reverse=1)
    return num_list


# question := 5
def freqOfListMem(mylist: list) -> dict:
    """
    A function that return a dictinary of element:freq in mylist

    >>> freqOfListMem([1, 3, 2, 1, 3, 4, 2, 6, 8])
    {1: 2, 3: 2, 2: 2, 4: 1, 6: 1, 8: 1}
    >>> freqOfListMem([4, 4, 7, 4, 2, 5, 1, 0, 7, 9])
    {4: 3, 7: 2, 2: 1, 5: 1, 1: 1, 0: 1, 9: 1}
    """
    freq = {}
    [freq.update({x: mylist.count(x)})for x in mylist]
    return freq

# question := 6


def uniqEleList(mylist: list) -> set:
    """
    A function that return set of unique element from my_list.
    >>> uniqEleList( [1, 2, 1, 3, 1, 3, 4, 1, 3, 9])
    {1, 2, 3, 4, 9}
    >>> uniqEleList([1, 8, 5, 3, 6, 2, 0, 1])
    {0, 1, 2, 3, 5, 6, 8}
    """
    my_set = set(mylist)
    return my_set


# question := 7
def firstRepeatedEle(mylist: list) -> int:
    """
    A function that return first repeated element in mylist
    >>> firstRepeatedEle([1, 2, 3, 4, 5, 1, 2, 3])
    1
    >>> firstRepeatedEle([2, 4, 3, 5, 2, 4, 1, 1])
    2
    """
    my_set = set()
    for x in mylist:
        if x not in my_set:
            my_set.add(x)
        else:
            return x


# question := 8
def sqrtqubefunc(n: int) -> dict:
    """
    A function that return a dict that contain x:[x^2,x^3] for evry x in range(0->n).
    >>> sqrtqubefunc(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> sqrtqubefunc(8)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125], 6: [36, 216], 7: [49, 343], 8: [64, 512]}
    """
    my_dict = {}
    [my_dict.update({x: [x*x, x*x*x]}) for x in range(n+1)]
    return my_dict

# question := 9


def ziptutfunc(mylist1: list, mylist2: list) -> list:
    """
    A function that uses zip..
    >>> ziptutfunc([1, 2, 3, 4],['a', 'b', 'c', 'd'])
    [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    >>> ziptutfunc([3, 7, 3, 5],["ram", "shyam", "mohan", "sohan"])
    [(3, 'ram'), (7, 'shyam'), (3, 'mohan'), (5, 'sohan')]
    """
    ans = zip(mylist1, mylist2)
    return list(ans)

# question := 10


def listComprehensiontut(n: int) -> list:
    """
    A function that return list of x^2 in range(0->n).

    >>> listComprehensiontut(5)
    [0, 1, 4, 9, 16, 25]
    >>> listComprehensiontut(10)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    y = [x*x for x in range(n+1)]
    return y

# question := 11


def dictComprehensiontut(n: int) -> dict:
    """
    A function that uses dict comprehension to generate x:x^2 in range(0->n).
    >>> dictComprehensiontut(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> dictComprehensiontut(9)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    """
    my_dict = {x: x*x for x in range(n+1)}
    return my_dict

# question := 12


class Que12:
    """
    A class that serves the purpose of que12.
    >>> a = Que12([1,2,3,4])
    >>> a.apply(lambda x:x**2)
    [1, 4, 9, 16]
    >>> a = Que12([3,2,3,1])
    >>> a.apply(lambda x:x**3)
    [27, 8, 27, 1]
    """

    def __init__(self, mylist) -> None:
        self.mylist = mylist

    def apply(self, func):
        try:
            ans = map(func, self.mylist)
            return list(ans)
        except:
            return "some error occured !"

# question := 13


def listEletoUpperCase(mylist: list) -> list:
    """
    A func that convert evry ele of list to uppercase.
    >>> listEletoUpperCase(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    >>> listEletoUpperCase(['abCd', 'cSw', 'dfG', 'eWG'])
    ['ABCD', 'CSW', 'DFG', 'EWG']
    """
    def upper(s: str) -> str:
        return s.upper()
    mylist = map(upper, mylist)
    return list(mylist)


# question := 14


def functoolreducetut(mylist: list) -> int:
    """
    A func that functools.reduce to give multiplication of a elements in list.
    >>> functoolreducetut([1, 2, 3, 4, 5])
    120
    >>> functoolreducetut([1, 2, 3, 4, 5, 9, 8, 0])
    0
    """
    ans = functools.reduce(lambda x, y: x*y, mylist)
    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
