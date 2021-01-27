#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np
import argparse


# In[87]:


parser = argparse.ArgumentParser()
parser.add_argument("--X")
parser.add_argument("--Y")
parser.add_argument("--T")


def st_line(X, Y):
    # Straight line
    N = len(X)
    print("Straight Line Fitting")
    print("X", " ", "Y", " ", "X^2", " ", "XY")
    print("----------------")
    sumX2 = 0
    sumXY = 0
    sumX = 0
    sumY = 0
    for x, y in zip(X, Y):
        sumX2 += x**2
        sumXY += x*y
        sumX += x
        sumY += y
        print(x, " ", y, " ", x**2, " ", x*y)
    print("----------------")
    print("EX=", sumX, "EY=", sumY, "EX^2=", sumX2, "EXY=", sumXY)
    a = (N * sumXY - sumX * sumY)/(N * sumX2 - (sumX)**2)
    b = (sumY - a*sumX)/N
    print("a =", a, "b =", b)
    print(f"y^ = {a}x + {b}")


def poly_line(X, Y):
    # Polynomial
    N = len(X)
    print("Polynomial Line Fitting")
    print("X", " ", "Y", " ", "X^4", " ", "X^3",
          " ", "X^2", " ", "X^2Y", " ", "XY")
    print("-------------------------------------------")
    sumX4 = 0
    sumX3 = 0
    sumX2 = 0
    sumX = 0
    sumX2Y = 0
    sumY = 0
    sumXY = 0
    for x, y in zip(X, Y):
        sumX4 += x**4
        sumX3 += x**3
        sumX2 += x**2
        sumX += x
        sumX2Y += (x**2)*y
        sumXY += x*y
        sumY += y
        print(x, " ", y, " ", x**4, "    ", x**3,
              "    ", x**2, "    ", (x**2)*y, "   ", x*y)
    print("--------------------------------------------")
    print(
        f"EX={sumX} EY={sumY} EX^4={sumX4} EX^3={sumX3} EX^2Y={sumX2Y} EXY={sumXY}")
    A = np.array([[sumX4, sumX3, sumX2], [
                 sumX3, sumX2, sumX], [sumX2, sumX, N]])
    B = np.array([[sumX2Y], [sumXY], [sumY]])
    XV = np.matmul(np.linalg.inv(A), B)
    print("a =", XV[0], "b =", XV[1], "c =", XV[2])
    print(f"y^ = {XV[0][0]}x^2 + {XV[1][0]}x + {XV[2][0]}")


try:
    X = parser.parse_args().X
    Y = parser.parse_args().Y
    T = parser.parse_args().T
    X = [float(i) for i in X[1:-1].split(",")]
    Y = [float(i) for i in Y[1:-1].split(",")]
    if T == "poly":
        poly_line(X, Y)
    else:
        st_line(X, Y)


except:
    print("Error")
