from typing import NamedTuple

from math import pi as PI, sin, cos, tan, sqrt, asin


g2r = lambda g : (g / 200) * PI
r2g = lambda r : r / PI * 200
Sin = lambda g : sin(g2r(g))
Cos = lambda g : cos(g2r(g))
Tan = lambda g : tan(g2r(g))


class Punkt(NamedTuple):
    """ Horizontale Richtung """
    r: float

    """ Zenitwinkel """
    z: float

    """ Schrägstreck von Standort zu dem Punkt"""
    s: float


def cal_geraete_hoehe(ptA:Punkt, hA: float) -> (float, float):
    SAp = ptA.s * Sin(ptA.z)
    AAp = ptA.s * Cos(ptA.z)
    h = hA - AAp
    return (h, SAp)


def cal_hoehe_B(ptB: Punkt, h: float) -> (float, float):
    BBp = ptB.s * Cos(ptB.z)
    hB = h + BBp
    return hB, ptB.s * Sin(ptB.z)


def cal_alpha(SAp: float, SBp: float, ptB:Punkt) -> float:
    """
    """
    sqrt_term = SAp**2 + SBp**2 - 2*SAp*SBp*Cos(ptB.r)
    ApBp = sqrt(sqrt_term)
    sin_alpha = Sin(ptB.r) * SBp / ApBp
    alpha = r2g( asin(sin_alpha) )
    return alpha, sin_alpha


def cal_hoehe_Ptk(ptP: Punkt, SAp: float, alpha: float, sin_alpha: float, h: float) -> (float, float):
    """
        @param ptP: Punkt zum Berechnen
        @param SAp: Streck SA'
        @param alpha: Winkel SA'B' [gon]
        @param h: Höhe vom Gerät
    """
    gamma = 200 - alpha - ptP.r
    SPp = SAp * sin_alpha / Sin(gamma)
    PPp = SPp * Tan(100 - ptP.z)
    hoehe_P = PPp + h
    ApPp = SAp / Sin(gamma) * Sin(ptP.r)
    return (hoehe_P, ApPp)


def cal_Streck_PQ(hoehe_P, ApPp, hoehe_Q, ApQp) -> float:
    dy = ApQp - ApPp
    dx = hoehe_Q - hoehe_P
    return sqrt(dy**2 + dx**2)


if __name__ == "__main__":
    ll = [48.43, 40.06, 39.46, 47.20, 56.15, 58.08, 51.23, 41.88, 38.64, 44.48, 42.08]
    hA = 23.06
    print("ind.W H-Gerät    HP         HQ         HB          Schr.str. PQ")
    for l in ll:
        ptA = Punkt(0, 85.87, l)
        ptB = Punkt(118.32 , 84.98, 48.52)
        ptP = Punkt( 63.16 , 87.43, None)
        ptQ = Punkt( 65.17 , 81.19, None)
        (h, SAp) = cal_geraete_hoehe(ptA, hA)
        (hB, SBp) = cal_hoehe_B(ptB, h)
        (alpha, sin_alpha) = cal_alpha(SAp, SBp, ptB)
        (hoehe_P, ApPp) = cal_hoehe_Ptk(ptP, SAp, alpha, sin_alpha, h)
        (hoehe_Q, ApQp) = cal_hoehe_Ptk(ptQ, SAp, alpha, sin_alpha, h)
        PQ = cal_Streck_PQ(hoehe_P, ApPp, hoehe_Q, ApQp)
        result = f"{l:5.2f} {h:10.7f} {hoehe_P:10.7f} {hoehe_Q:10.7f} {hB:10.7f} {PQ:10.7f}"
        print(result)







