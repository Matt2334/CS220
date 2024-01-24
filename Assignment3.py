#Discrete Structures (CSCI220)
#Assignment3: Basic Mathematical Structures


import random
import numpy as np
from itertools import chain, combinations


# [1] Define a function get_function_type(func, func_domain, func_co_domain) that receives a
# function "func" and two sets - domain and co_domain and determines whether the function
# passed in is "partial", "bijectve", "injective", or "surjective". First, compute func_range
# by evaluating the function for each value of the domain.
def get_function_type(func, func_domain, func_co_domain):
    is_total = True; is_partial = True; is_injective = True
    my_range = set()
    for element in func_domain:
        image = func(element)
        if image not in func_co_domain:
            is_total = False
        elif image in my_range:
            is_injective = False
        else:
            my_range.add(image)
    is_surjective = (my_range == func_co_domain)
    is_bijective = is_injective and is_surjective
    return f"is_total = {is_total}, is_partial = {is_partial}, is_injective = {is_injective}, is_surjective = {is_surjective}, is_bijective = {is_bijective}"


def f_identity(n):
    return n


def f_predecessor(n):
    return n-1


def f_successor(n):
    return n+1

def f_square(n):
    return n*n


def q1():
    decimals = set([i for i in range(10)])
    for func in [f_identity, f_successor, f_predecessor, f_square]:
        print(func.__name__, get_function_type(func, func_domain=decimals, func_co_domain=decimals))



# [2] Define functions that compute the following set operations. The first five functions are binary and should accept two arguments each, while the last function is unary and should accept only one argument. You may use built-in functions to your language or implement them yourself.
# set_union(set1, set2) : X ∪ Y
# set_intersection(set1, set2): X ∩ Y
# set_difference(set1, set2): X − Y
# set_symmetric_difference(set1, set2):  X ∆  Y
# set_cartesian_product(set1, set2): X x Y
# set_power_set(set1):  P(X)
def set_union(set1, set2):
    set3=set1
    for element in set2:
        set3.add(element)
    return set3


def set_intersection(set1, set2):
    set3=set()
    for element in set2:
        if element in set1:
            set3.add(element)
    return set3


def set_difference(set1, set2):
    set3=set1
    for element in set2:
        if element in set1:
            set3.remove(element)
    return set3


def set_symmetric_difference(set1, set2):
    return set_difference(set_union(set1, set2), set_intersection(set1, set2))


def set_cartesian_product(set1, set2):
    set3=set()
    for elem1 in set1:
        for elem2 in set2:
            set3.add((elem1, elem2))
    return set3


def set_power_set(set1):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(set1)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def q2():
    X = {"a", "ab", "abc", "abcd"}
    Y = {"a", "bb", "ccc", "dddd"}
    print("Union:", set_union(X, Y))
    print("Intersection:", set_intersection(X, Y))
    print("Difference:", set_difference(X, Y))
    print("Symmetric Difference:", set_symmetric_difference(X, Y))
    print("Cartesian Product:", set_cartesian_product(X, Y))
    print("Power Set X:", set_power_set(X))
    print("Power Set Y:", set_power_set(Y))


# [3] Consider the following sums of series:
# counting(n) = 1 + 2 + … + n
# squares(n) = 1^2 + 2^2 + 3^2 + … + n^2
# cubes(n) = 1^3 + 2^3 + 3^3 + … + n^3
# geomteric_series(a, r, n) = a + ar + ar^2 + … + ar^n
# arithemetic_series(n, a, d) = a + ad + 2ad + … + nad
#
# [a] Write functions to compute each sum by looping over the terms
# [b] Write functions to compute each term by using a closed-form formula available in slides or online
# [c] Compare the results (since there may be roundoff error, do not look for equality but rather a difference less than 1)
def sum_counting_loop(n):
    return sum([i for i in range(1, n+1)])


def sum_counting_formula(n):
    return n*(n+1)/2


def sum_squares_loop(n):
    return sum([i**2 for i in range(1, n+1)])


def sum_squares_formula(n):
    return n*(n+1)*(2*n+1)/6


def sum_cubes_loop(n):
    return sum([i**3 for i in range(1, n+1)])


def sum_cubes_formula(n):
    return (n*(n+1)/2)**2


def sum_geometric_loop(n, a, r):
    return sum([a*r**i for i in range(0, n+1)])


def sum_geometric_formula(n, a, r):
    return a * ((r**(n+1)-1) / (r-1))


def sum_arithmetic_loop(n, d, a):
    return sum([a+d*i for i in range(0, n+1)])


def sum_arithmetic_formula(n, d, a):
    return a * (n+1) + d*n*(n+1)/2

def q3():
    n = 10; a = 5; r = 6; d = 4
    print("Sum Counting Numbers:",sum_counting_loop(n), "\nSum Counting Formula:", sum_counting_formula(n))
    print("Sum Squares Numbers:", sum_squares_loop(n), "\nSum Squares Formula:", sum_squares_formula(n))
    print("Sum Cubes Numbers:", sum_cubes_loop(n), "\nSum Cubes Formula:", sum_cubes_formula(n))
    print("Sum Geometric Numbers:", sum_geometric_loop(n, a , r), "\nSum Geometric Formula:", sum_geometric_formula(n, a, r))
    print("Sum Arithmetic Numbers:", sum_arithmetic_loop(n, d, a), "\nSum Arithmetic Formula:", sum_arithmetic_formula(n, d, a))

# [4] Consider a pair of matrices
# [a] Code the generation of random n x n integer matrices and call it twice.
# [b] Code the sum of the matrices using loops, list comprehension,  and numpy.matrix.sum(), and compare the results
# [c] Code the product of the matrices using loops, list comprehension,  and numpy.multiply(), and compare the results.
def random_matrix(n):
    return [[random.randint(1, 10) for i in range(n)] for j in range(n)]


def sum_matrices_loops(m1, m2):
    n = len(m1)
    m3 = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3


def sum_matrices_list_comp(m1, m2):
    n = len(m1)
    m3 = [[m1[i][j]+m2[i][j] for j in range(n)] for i in range(n)]
    return m3


def print_matrix(m):
    print(np.array(m))
    print()


def mult_matrices_loops(m1, m2):
    n = len(m1)
    m3 = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3


def mult_matrices_list_comp(m1, m2):
    n = len(m1)
    m3 = [[sum([m1[i][k]*m2[k][j] for k in range(n)]) for j in range(n)] for i in range(n)]
    return m3

def q4():
    m1 = random_matrix(5)
    m2 = random_matrix(5)
    sum1 = sum_matrices_loops(m1, m2)
    sum2 = sum_matrices_list_comp(m1, m2)
    print_matrix(sum1)
    print_matrix(sum2)

    mult1 = mult_matrices_loops(m1, m2)
    mult2 = mult_matrices_list_comp(m1, m2)
    print_matrix(mult1)
    print_matrix(mult2)


# [5] Define a function generate_binary_number(binary_numbers) that takes a list of the string
# representation of some fractional binary numbers in the range [0,1) and uses Cantor's
# diagonalization argument to find a number not already in that list. Be mindful of the
# case where there are more elements in the list than digits in each number, and assume implicit
# trailing zeros as needed.

# 0.010011
# 0.101010
# 0.111000
# 0.000111
# 0.111111
# 0.111000
def generate_binary_number(numbers):
    return "0."+ "".join(["1" if numbers[i][i+2] == "0" else "0" for i in range(len(numbers))])


def convert_to_decimal(num):
    return sum([int(num[i])/2**(i-1) for i in range(2, len(num))])


def q5():
    numbers = ["0.010011", "0.101010", "0.111000", "0.000111", "0.111111", "0.111000"]
    for num in numbers:
        print("Old Number:", num, convert_to_decimal(num))
    number = generate_binary_number(numbers)
    print("New Number:",number, convert_to_decimal(number))

def q6():
    pass


def main():
    questions = [q1,q2,q3,q4,q5,q6]
    for q in questions:
        print("question", q.__name__)
        q()
        print()


if __name__ == '__main__':
    main()