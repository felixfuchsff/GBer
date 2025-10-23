# common functions in geodesy
from typing import NamedTuple

from math import pi as PI, sin, cos, tan, sqrt, asin, atan

def g2r(g): return (g / 200) * PI
def r2g(r) : return r / PI * 200
def Sin(g) : return sin(g2r(g))
def Cos(g) : return cos(g2r(g))
def Tan(g) : return tan(g2r(g))
#
def Atan(t) : return r2g(atan(t))

def cal_circular_segment_area (r, alpha ):
    """
        @param r: Radius
        @param alpha: Zentriwinkel in Radian
    """
    return ((r**2)/2) * (alpha - sin(alpha))


class Pkt(NamedTuple):
    """
        Punkt auf geodäsische link-händiges Koordinatessystem
    """
    x: float
    y: float


def cal_Gauss_area(points:[Pkt]) -> float:
    """
        @param points sind die Punkten auf der Ebene. Sie müssen bereits in Uhrzeigersinn zu geordenet.
    """
    n = len(points)
    f = 0
    t = ""
    for i,p in enumerate(points):
        x = p.x
        y_next = points[(i+1)%n].y
        y_last = points[(i-1)%n].y
        t = x*(y_next - y_last)
        print(f"{i} {f} = {f} + {x} * ( {y_next} - {y_last} ) = {f} +  {t}")
        f += x*(y_next - y_last)

    return f


def cal_zentriwinkel_bisection(a, s, epsilon=1E-5, iteration=200) -> (float, float):
    """
        @param a: Flächeninhalt des Kreissegmentes, auch Kreisabschnittsfläche genannt
        @param s: Sehnenlänge
        @param iteration: maximale Iterationen
    """
    RHS = 8 * a / s / s # CONST

    left = 0
    right = PI
    count = 0
    while count < iteration:
        count += 1
        alpha = (right + left) / 2
        lhs = (alpha - sin(alpha)) / (sin(alpha/2)**2)
        diff = lhs - RHS
        print(f"count {count} right: {right} left: {left} alpha: {alpha} lhs: {lhs} diff : {diff}")
        if abs(diff) < epsilon:
            break
        if diff < 0:
            left = alpha
        if diff > 0:
            right = alpha
    return alpha, diff





























