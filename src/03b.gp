AB = BA = 17.11;
BC = CB = 19.48;
CD = DC = 23.06;

d = DA = AD = 21.30;
AC = CA = 22.97;

DP = PD = DC/2;
PC = CP = DP;

rho = Pi/200;

print("=====================")

s = (AB + BC + CA)/2;
F_ABC = sqrt( s*(s - AB)*(s - BC)*(s - CA) );
print("F_ABC = ", F_ABC); \\ 162.683243


h_c = 2*F_ABC / AB;
print("h_c = ", h_c);   \\ 19.016159

b = sqrt(BC^2 - h_c^2);
print("m = ", m);  \\ 12.884354
print("b = ", b);  \\  4.225646

print("")
print("PROBE 1: m + b = AB");
m = sqrt(AC^2 - h_c^2);
print("m + b = ", m + b);
print("   AB = ", AB);
print("PROBE 1 done");
print("")

s = (AD + DC + AC)/2;
F_ACD = sqrt(s*(s - AD)*(s - DC)*(s - AC));
F_ABCD = F_ABC + F_ACD;
print("    F_ABCD = ", F_ABCD)


beta_rad = acos(b/BC);
beta_gon = beta_rad / rho;
print("  beta_gon = ", beta_gon);

cos_gamma_b = (AC^2 + BC^2 - AB^2)/(2*AC*BC);
gamma_b_rad = acos(cos_gamma_b);
cos_gamma_d = (CD^2 + CA^2 - AD^2)/(2*CD*CA);
gamma_d_rad = acos(cos_gamma_d);
gamma_rad = gamma_b_rad + gamma_d_rad;

gamma_gon = gamma_rad / rho;
print(" gamma_gon = ", gamma_gon);

varphi_rad = 3*Pi/2 - beta_rad - gamma_rad;
varphi_gon = varphi_rad / rho;
print("varphi_gon = ", varphi_gon);

aP = 1/tan(varphi_rad);
bP = 2*h_c;
cP = h_c*b - F_ABCD;

print("Equation paramters:")
print("a : ", aP, ";");
print("b : ", bP, ";");
print("c : ", cP, ";");
print("")


l = -(17*sqrt(74682240625315657653331391016726904478113) - 4671258189720594550017)/3226741595787642208;
print("l = ", l);
h = h_c + l/tan(varphi_rad);
print("h = ", h);

print("")
AR = AB - b - l;
print("AR &= AB - b - l = ", AR);
RB = AB - AR;
print("RB &= AB - AR", RB);
CS = l * sin(varphi_rad);
print("CS &= l\\sin(200 - \\varphi) = l \\sin(\\varphi) = ", CS);
SD = DC - CS;
print("SD &= DC - CS = ", SD);

print("");
lhs = l*(h + h_c) + h_c*b;
print("   lhs = ", lhs);
print("F_ABCD = ", F_ABCD)




























