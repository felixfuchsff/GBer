##! /usr/bin/env python3

from typing import NamedTuple

from geodesy import *



pA = Pkt(15.48, 7.56)
pB = Pkt(24.47,13.12)
pC = Pkt(36.01, 2.95)
pD = Pkt(45.88, 7.56)
pE = Pkt(53.97,14.86)
pF = Pkt(64.71, 6.33)

pG1 = Pkt(15.48, 2.95)
pG2 = Pkt(64.71, 2.95)
pG3 = Pkt(64.71,14.86)
pG4 = Pkt(15.48,14.86)


def cal_flaeche():
    leftPolygon = [pG2, pF, pE, pD, pC, pB, pA, pG1]
    fLhs = cal_Gauss_area(leftPolygon) / 2
    print(fLhs)


    rightPolygon = [pG4, pA, pB, pC, pD, pE, pF, pG3]
    fRhs = cal_Gauss_area(rightPolygon) / 2
    print(fRhs)

    f = fLhs + fRhs
    print(f)


def cal_radius_gleich_glaeche():
    a = 100.1214
    s = 49.245363
    alpha, diff, iterations = cal_zentriwinkel_bisection(a, s, epsilon=1e-13, iteration=40)
    radius = s/2/sin(alpha/2)
    print(alpha, diff, iterations)
    print(radius)


if __name__ == "__main__":
    cal_radius_gleich_glaeche()
