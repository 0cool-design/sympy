#!/usr/bin/env python3
from sympy import symbols, Eq, solve

R, C, D = symbols('r c d')

list = [R, C, D]

expr_list = [D+C, R+D+4, R+C+14]

for g in expr_list:
    for h in expr_list:
        expr1 = g - h
        print(expr1)
        for i in list:
            for j in list:
                e1 = expr1.subs(i, j)
                print(e1)
