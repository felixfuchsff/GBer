# common functions in geodesy

from math import pi as PI, sin, cos, tan, sqrt, asin, atan

g2r = lambda g : (g / 200) * PI
r2g = lambda r : r / PI * 200
Sin = lambda g : sin(g2r(g))
Cos = lambda g : cos(g2r(g))
Tan = lambda g : tan(g2r(g))
#
Atan = lambda t : r2g(atan(t))
