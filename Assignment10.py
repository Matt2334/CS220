#Discrete Structures (CSCI220)
#Assignment10: Discrete Probability


import math
from itertools import accumulate
import numpy as np
from matplotlib import pyplot as plt
import Assignment8 as as8

def C(n,r):
    return math.comb(n, r)


# [1] Define a function prob(n, p, s, f) that computes the probability that one first achieves s successes and f failures on trial n, given that the probabilities of success and failure on a single trial are p and 1-p respectively. Refer to the table and notes above
def prob(n, p, s, f):
    return 0 if s+f > n else (C(n-1, s-1) * (p**s) * (1-p) ** (n-s)) + (C(n-1, f-1) * (p**(n-f)) * (1-p) ** f)


# [2] Define a function pdf() that computes the probability density function for a given probability function.
def pdf(func, max_n, p, s, f):
    return [func(n,p,s,f) for n in range(max_n+1)]


# [3] Define a function cdf() that computes the cumulative distribution function for a given probability function.
def cdf(func, max_n, p, s, f):
    pd = pdf(func, max_n, p, s, f)
    return list(accumulate(pd))


# [4] Define a function ev() that computes the expected value E(X) - or mean - defined as Σk * P(X=k).
def ev(pd):
    return sum([n *pd[n] for n in range(0,len(pd))])


# [5] Define a function var() that computes the variance Var(X) defined as Σk * P(X=k) * (k-𝜇)2 where 𝜇 is the mean
def var(pd, mean):
    return sum([n*pd[n] *(n-mean)**2 for n in range(len(pd))])/len(pd)


# [6] Define a function sd() that computes the standard deviation defined as √Var(X)
def sd(v):
    return math.sqrt(v)


# [7] Define a function plot_graph() that can be used to plot both the PDF and CDF
def plot_graph(pd, cd, p, s, f):
   #https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
   max_n = len(pd)
   x_axis = [n for n in range(max_n)]
   y1, y2 = pd, cd
   x = np.arange(len(x_axis))  # the label locations
   width = 0.35  # the width of the bars
   fig, ax = plt.subplots()
   ax.bar(x - width / 2, y1, width, label='PDF')
   ax.bar(x + width / 2, y2, width, label='CDF')
   # Add some text for labels, title and custom x-axis tick labels, etc.
   ax.set_xlabel('n')
   ax.set_ylabel('PDF and CDF')
   ax.set_title(f'PDF and CDF for {s} successes and {f} failures with p={p}')
   ax.set_xticks(x, x_axis)
   ax.legend()
   fig.tight_layout()
   plt.savefig(f"Assignment10-s-{s}-f-{f}.png")
   plt.show()


def make_table(pd, cd, p, s, f):
    headers = ["n", "PDF", "CDF"]
    data = [[n,pd[n], cd[n]] for n in range(len(pd))]
    title = f'PDF and CDF for {s} successes and {f} failures with p={p}'
    alignments = ["r"]*3
    as8.print_table(title, headers, data, alignments)


def calculate(max_n, p, s, f):
    pd = pdf(prob, max_n, p, s, f)
    cd = cdf(prob, max_n, p, s, f)
    plot_graph(pd, cd, p, s, f)
    make_table(pd, cd, p, s, f)
    mean = ev(pd)
    v = var(pd, mean)
    print("Expected Value is: ", round(mean, 2))
    print("Variance is: ", round(v, 2))
    print("Standard Deviation is: ", round(sd(v), 2))


def main():
    max_n= 25
    calculate(max_n, .25, 5, 5)
    calculate(max_n, .5, 5, 5)
    calculate(max_n, .5, 5, 10)
if __name__ == '__main__':
    main()