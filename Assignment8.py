#Discrete Structures (CSCI220)
#Assignment8: Divide and Conquer


import math
import texttable
import inspect
import matplotlib.pyplot as plt
import pandas as pd


def logr(b, x):
    return float_or_int(round(math.log(x, b), 2))


def expstr(b, c):
    return "1" if c == 0 else b if c == 1 else f"{b}^{c}"


def float_or_int(s):
    n = float(s)
    if n.is_integer():
        n = int(n)
    return n


# [1] Define a function master_theorem(a, b, c) that determines the order of magnitude of the solution to a recurrence of the form T(n) = aT(n/b) + O(nc). See https://www.geeksforgeeks.org/how-to-analyse-complexity-of-recurrence-relation/ .
def master_theorem(a, b, c):
    rhs = b ** c
    lhs = a
    if lhs < rhs:
        result = f"Θ({expstr('n', c)})"
    elif lhs == rhs:
        e = expstr('n', c)
        result = f"Θ({e if e !='1' else ''}log n)"
    else:
        result = f"Θ({expstr('n', logr(b, a))})"
    return result


# [2] Define a function parse_recurrence(recurrence) that parses a string representation of a recurrence and extracts the a. b, and c to pass into the function of the previous task. You can make any reasonable assumptions about the format of said recurrence.
def parse_recurrence(recurrence):
    # f = "f"
    idx = recurrence.find("(")
    f = recurrence[idx-1]
    s1 = recurrence[:recurrence.find(f)].strip()
    a = 1 if s1 == "" else float_or_int(s1)
    s2 = recurrence[recurrence.find("/") + 1:recurrence.find(")")].strip()
    b = float_or_int(s2)
    s3 = recurrence[recurrence.find("+") + 1:].strip()
    s3 = "0" if s3.find("n") < 0 else "1" if s3.find("^") < 0 else s3[s3.find("^") + 1:]
    c = float_or_int(s3)
    return a, b, c


# [3] Create an empty dictionary to store intermediate results and a helper function ff:
dict_funcs = {}
def ff(f, n):
    n=int(n)
    func_name = f.__name__
    if func_name not in dict_funcs:
        dict_funcs[func_name] = {}
    dict_func = dict_funcs[func_name]
    if n not in dict_func:
        if n <= 0:
            return 0
        dict_func[n] = f(f, n)
    return dict_func[n]


# [4] Define a sample function f1, like the one for MergeSort. Try to use the one-line if/else
# (aka "ternary expression") as it will make it easier to capture the function content.
def f1(f, n):
    return 0 if n == 1 else 2 * ff(f, n/2) + n


# [5] Create additional functions f2 through f10 corresponding to nine more recurrences from the slides or old exams.
# Time Complexity for Binary Search
def f2(f, n):
    return 1 if n == 1 else ff(f, n / 2) + 1


# Time Complexity for Strassen Multiplication
def f3(f, n):
    return 1 if n == 1 else 7 * ff(f, n / 2) + n ** 2


# Time Complexity for Divide and Conquer Long Integer Multiplication
def f4(f, n):
    return 1 if n == 1 else 4 * ff(f, n / 2) + n


# Time Complexity for Made up example
def f5(f, n):
    return 1 if n == 1 else 25 * ff(f, n / 5) + n


# Time Complexity for Made up example
def f6(f, n):
    return 1 if n == 1 else 3 * ff(f, n / 2) + n ** 2


# Time Complexity for Made up example
def f7(f, n):
    return 1 if n == 1 else 4 * ff(f, n / 2) + n ** 2


# Time Complexity for Made up example
def f8(f, n):
    return 1 if n == 1 else 2 * ff(f, n / 3) + n ** 3


# Time Complexity for Made up example
def f9(f, n):
    return 1 if n == 1 else 2 * ff(f, n / 3) + 5


# Time Complexity for Made up example
def f10(f, n):
    return 1 if n == 1 else 6 * ff(f, n / 2) + n


# Stooge Sort
def f11(f, n):
    return 1 if n == 1 else 3 * ff(f, n / 1.5) + 1


# Karatsuba
def f12(f, n):
    return 1 if n == 1 else 3 * ff(f, n / 2) + n


def f13(f, n):
    return 1 if n == 1 else 8 * ff(f, n / 2) + n**2


# A(1) = 1, A(n) = 16A(n/2) + n for n > 1.
def f14(f, n):
    return 1 if n == 1 else 16 * ff(f, n / 2) + n


# [6] Test the function by calling from your main function
def call_and_print(func, n, desc):
    print(func.__name__, desc, "for n =", n, "is", ff(func, n))
    call_and_print(f1, 256, "f(n) = 2*f(n/2) + n")


def func_body(f):
    body = inspect.getsource(f)
    idx = body.index("return")
    return body[7 + idx:].strip()


def print_table(title, headers, data, alignments):
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows([headers] + data, True)
    print(title)
    print(tt.draw())
    print()


def run_function(functions, data, description, recurrence, function, n):
    a, b, c = parse_recurrence(recurrence)
    mt = master_theorem(a, b, c)
    val = ff(function, n)
    log_val = 0 if val == 0 else math.log(val)
    parameters = f"a={a}, b={b}, c={c}"
    data.append([function.__name__, description, recurrence, parameters, func_body(function), mt, val, log_val])
    functions.append(function)

def prepare_output(data, n, ranked=False):
    if ranked:
        data = sorted(data, key=lambda l:l[-1])
    title = f"Divide-and-Conquer Recurrences for n={n}"
    heads = ["Name", "Description", "Recurrence", "Parameters", "Function Syntax", "Master Theorem", "Value", "Log Value"]
    align = ["l", "l", "l", "l", "l", "l", "r", "r"]
    print_table(title, heads, data, align)


# [7] See all the intermediate values that were also computed by executing:
# for func in dict_funcs:
#     func_name = func.__name__
#     print(func_name, dict_funcs[func_name])


def run_functions(n):
    data = []
    functions = []
    run_function(functions, data, "Merge Sort", "2f(n/2)+n", f1, n)
    run_function(functions, data, "Binary Search", "f(n/2)+1", f2, n)
    run_function(functions, data, "Strassen's Matrix Multiplication", "7f(n/2)+n^2", f3, n)
    run_function(functions, data, "Long Integer Multiplication", "4f(n/2)+n", f4, n)
    run_function(functions, data, "D&C Recurrence", "25f(n/5)+n", f5, n)
    run_function(functions, data, "Example 6", "3f(n/2)+n^2", f6, n)
    run_function(functions, data, "Example 7", "4f(n/2)+n^2", f7, n)
    run_function(functions, data, "Example 8", "2f(n/3)+n^3", f8, n)
    run_function(functions, data, "Example 9", "2f(n/3)+5", f9, n)
    run_function(functions, data, "Example 10", "6f(n/2)+n", f10, n)
    run_function(functions, data, "Stooge Sort", "3f(n/1.5)+1", f11, n)
    run_function(functions, data, "Long Integer Karatsuba", "3f(n/2)+n", f12, n)
    run_function(functions, data, "D&C Matrix Multiplication", "8f(n/2)+n**2", f13, n)
    run_function(functions, data, "Teitleman Exam Problem", "16f(n/2)+n", f14, n)
    return data, functions


def plot_values(file_name, dict_funcs, inputs, funcs):
    func_num = 0
    plt.xticks([j for j in range(len(inputs))], [str(n) for n in inputs])
    for func in funcs:
        funcName= func_name(func)
        func_num += 1
        d = dict_funcs[funcName]
        x_axis = [j + 0.05 * func_num for j in range(len(inputs))]
        y_axis = [d[i] for i in inputs]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=func_body(func))
    plt.legend()
    plt.title("Value of functions")
    plt.xlabel("n")
    plt.ylabel("log f(n)")
    plt.savefig(file_name)
    plt.show()


def func_name(func):
    return func.__name__ + " " + func_body(func)


def compute_values(funcs, inputs):
    dict_f = {}
    for func in funcs:
        funcName = func_name(func)
        dict_f[funcName] = {}
        for n in inputs:
            val = func(func, n)
            log_val = 0 if val <=0 else math.log(val, 10)
            dict_f[funcName][n] = log_val
    return dict_f


def print_values(dict_f, ranked=False):
    print("List of functions", "ranked" if ranked else "unranked")
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_f).T
    if ranked:
        df = df.sort_values(by=[df.columns[-1]])
    print(df)


def main():
    n = 100000000
    assn = "Assignment8"
    data, functions = run_functions(n)
    prepare_output(data, n, True)
    inputs = [100 * i for i in range(1,11)]
    dict_funcs2 = compute_values(functions, inputs)
    plot_values(assn+".png", dict_funcs2, inputs, functions)
    print_values(dict_funcs2, True)



if __name__ == '__main__':
    main()