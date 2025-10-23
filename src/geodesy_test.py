from geodesy import *


def test_circular_segment_area():
    alpha = 0.4929278
    r = 100.92244
    f = cal_circular_segment_area(r, alpha)
    print(f)

def test_cal_zentriwinkel_bisection():
    a = 100.1214
    s = 49.245363
    alpha = cal_zentriwinkel_bisection(a, s,epsilon=1e-8)
    print(alpha)


if __name__ == "__main__":
    #test_circular_segment_area()
    test_cal_zentriwinkel_bisection()
