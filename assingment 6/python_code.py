from typing import Callable, List
import math
import nltk

# DO NOT MAKE UNNECESSARY CHANGES


class DistanceFuncs:

    def calc_distance(
        self, point_a: List[float], point_b: List[float], dist_func: Callable, /
    ) -> float:
        """ Calculates distance between two points using the passed dist_func """
        return dist_func(point_a, point_b)

    @staticmethod
    def euclidean(point_a: List[float], point_b: List[float], /) ->float:
        """
        Calculates Euclidean Distance between two points Example:
        >>> DistanceFuncs.euclidean([1,1],[1,1])
        0.0
        """
        return math.dist(point_a, point_b)

    @staticmethod
    def manhattan_distance(point_a: List[float], point_b: List[float], /):
        """ Compute
        the manhattan_distance between two points """
        distance = 0
        for a, b in zip(point_a, point_b):
            distance += abs(a-b)
        return distance


    @staticmethod
    def jaccard_distance(point_a, point_b):
        """Compute
        the jaccard_distance between two points """ 
        return nltk.jaccard_distance(point_a, point_b)

def main():
    """Demonstrate the usage of DistanceFuncs """
    funcs = DistanceFuncs()
    A, B = [1,2], [5,8]
    distance = funcs.calc_distance(A, B, math.dist)
    print("\n\n")
    print(f"\tcalc_distance between {A} and {B} = {distance}")
    print("\n")
    print(f"\teuclidean distance between {A} and {B} = {funcs.euclidean(A, B)}")
    print("\n")
    print(f"\tmanhattan distance between {A} and {B} = {funcs.manhattan_distance(A, B)}")
    print("\n")
    A, B = set('hello'), set('cloudcomputing')
    print(f"\tjaccard distance between 'hello' and 'cloudcomputing' = {funcs.jaccard_distance(A, B)}")
    print("\n\n")

    pass

if __name__ == "__main__":
    main()