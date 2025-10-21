# common functions in geodesy
from typing import NamedTuple

from math import pi as PI, sin, cos, tan, sqrt, asin, atan

g2r = lambda g : (g / 200) * PI
r2g = lambda r : r / PI * 200
Sin = lambda g : sin(g2r(g))
Cos = lambda g : cos(g2r(g))
Tan = lambda g : tan(g2r(g))
#
Atan = lambda t : r2g(atan(t))

"""
    @param r: Radius
    @param alpha: Zentriwinkel in Radian
"""
cal_circular_segment_area = lambda r, alpha : ((r**2)/2) * (alpha - sin(alpha))


class Pkt(NamedTuple):
    """
        Punkt auf geodäsische link-händiges Koordinatessystem
    """
    x: float
    y: float


def cal_Gauss_area(points:[Pkt]) -> float:
    """
        @param points sind die Punkten auf der Ebene. Sie müssen bereits in Uhrzeigersinn zugeordenet.
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


def cal_zentriwinkel_bisection(a, s) -> float:
    """
        @param a: Flächeninhalt des Kreissegment, auch Kreisabschnittsfläche genannt
        @param s: Sehnelänge
    """
    RHS = 8 * a / s / s # CONST
    EPSILON = 1E-15

    left = 0
    right = PI
    count = 0
    MAX = 200
    while count < MAX:
        count += 1
        alpha = (right + left) / 2
        lhs = (alpha - sin(alpha)) / (sin(alpha/2)**2)
        diff = lhs - RHS
        #print(f"count {count} right: {right} left: {left} alpha: {alpha} lhs: {lhs} diff : {diff}")
        if abs(diff) < EPSILON:
            break
        if diff < 0:
            left = alpha
            #print("    >>>>>> change")
        if diff > 0:
            right = alpha
            #print("    <<<<<< change")
    return (alpha, diff)





























