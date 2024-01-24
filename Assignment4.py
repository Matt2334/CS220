#Discrete Structures (CSCI220)
#Assignment4: Permutations and Combinations

import texttable
from math import factorial, perm, comb

# [1] Create a function print_table(name, func, n) that prints a (n+1) x (n+1) table for the function f(i, j) where both i and j iterate over 0 thru n inclusive.
# Print the name of the table
# Add column headings
# Print a blank line after the table
def print_table(name, headers, data, alignments):
   tt = texttable.Texttable(0)
   tt.set_cols_align(alignments)
   tt.add_rows([headers] + data, True)
   print(name)
   print(tt.draw())
   print()


def c(n,r):
    return comb(n, r)

def p(n, r):
    return perm(n, r)


def c2(n,r):
    return 0 if r>n else fact(n)/(fact(r)*fact(n-r))


def p2(n,r):
    return 0 if r>n else fact(n)/fact(n-r)


def fact(n):
    return 0 if n<0 else factorial(n)


# [2] From your main function, call print_table using "Permutations" and the built-in math.perm
def functions(f, c, n, t):
    headers=[f"{c}(n,{r})" for r in range(n+1)]
    data = [[f(i,j) for j in range(n+1)] for i in range(n+1)]
    alignments = ["r"] * (n+1)
    print_table(t, headers, data, alignments)

# Streamlined these into the function "functions" above
# [3] From your main function, call print_table using "Permutations" and your own my_perm
# [4] From your main function, call print_table using "Combinations" and the built-in math.comb
# [5] From your main function, call print_table using "Combinations" and your own my_comb


# [6] In the standard game of poker, one is dealt a "hand" of five cards which is classified into one of several categories. For example, "Four of a Kind" means four cards of one rank and one card of another rank. "Full House'' means three cards of one rank, and two cards of another rank. We want to compute the number of possible ways to get a given hand. Then, use this function to compare your calculated answer with the known correct answer and then call it for all standard hands.
def compare_comb(hand_name, known_answer, computed_answer):
    print("Hand Name:", hand_name, "Known:", known_answer, "Computed:", computed_answer,
"MATCH" if computed_answer == known_answer else "ERROR")


def q6():
    hands = [["Royal Flush", 4, c(4,1)],
             ["Straight Flush", 36, c(10, 1)*c(4, 1)-c(4,1)],
             ["Four of a Kind",624 , c(13,1)*c(4,4)*c(12,1)*c(4,1)],
             ["Full House", 3744, c(13,1)*c(4,3)*c(12,1)*c(4,2)],
             ["Flush", 5108, (c(13,5)*c(4,1))-(c(10,1)*c(4,1))],
             ["Straight", 10200, c(10,1)*(c(4,1)**5)-(c(10,1)*c(4,1))],
             ["Three of a Kind", 54912, c(13,1)*c(4,3)*c(12,2)*(c(4,1)**2)],
             ["Two Pair", 123552, c(13,2)*(c(4,2)**2)*c(11,1)*c(4,1)],
             ["One Pair", 1098240, c(13,1)*c(4,2)*c(12,3)*(c(4,1)**3)],
             ["No Pair", 1302540, (c(13,5)-c(10,1))*(c(4,1)**5-c(4,1))]]
    headers = ["Name", "Frequency", "Computed"]
    alignments = ["l", "r", "r"]
    print_table("Poker Hands", headers, hands, alignments)


def main():
    functions(p, "P", 10, "Permutations using Built-in perm")
    functions(p2, "P", 10, "Permutations using our perm function")
    functions(c, "C", 10, "Combinations using Built-in perm")
    functions(c2, "C", 10, "Combinations using our comb function")
    q6()

if __name__ == '__main__':
    main()