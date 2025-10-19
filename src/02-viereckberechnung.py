##! /usr/bin/env python3

from typing import NamedTuple

from geodesy import *

class Viereck(NamedTuple):
    alpha: float
    beta: float
    delta: float


def cal_separated_angle(alpha: float, g:(float, float)) -> (float,float, float, float):
    ta = Tan(alpha)
    q = g[0]/g[1]
    a = q*ta; b = q + 1; c = -ta
    d = b**2 - 4*a*c
    t = (-b + sqrt(d))/2/a
    alpha_D = Atan(t)
    alpha_B = alpha - alpha_D
    return alpha_B, alpha_D, g[0]/Tan(alpha_B), g[1]/t

def cal_diagonal(viereck:Viereck, g:(float,float)):
    (a_B, a_D, _, _) = cal_separated_angle(viereck.alpha, g)
    gamma = 400 - viereck.alpha - viereck.beta - viereck.delta
    beta_C = viereck.beta - 100 + a_B
    strecke_AD = g[1]/Sin(a_D)
    strecke_CD = Sin(beta_C) * (g[0] + g[1]) / Sin(gamma)
    sqr_strecke_AC = strecke_AD**2 + strecke_CD**2 - 2*strecke_AD*strecke_CD*Cos(viereck.delta)
    return sqrt(sqr_strecke_AC)


if __name__ == '__main__':
    print("2.te Aufgabe Viereckberechnung")
    g = (16.10, 17.11)
    v = Viereck(alpha=90.241, delta=97.236, beta=140.292)
    streck_AC = cal_diagonal(v, g)
    print(streck_AC)