AB = BA = 17.11;
BC = CB = 19.48;
CD = DC = 23.06;

DA = AD = 21.30;
AC = CA = 22.97;

DP = PD = DC/2;
PC = CP = DP;

rho = Pi/200;

cos_delta = (AD^2 + CD^2 - AC^2) / (2*AD*CD)
delta = acos(cos_delta) / rho

print("delta = ", delta)

sin_delta = sqrt(1 - cos_delta^2);
print("sin(delta) = ", sin_delta);

F1p = 0.5 * DA * DP * sin_delta;
print("F'1 = ", F1p);


sqrAP = AD^2 + PD^2 - 2*AD*PD*cos_delta;
print("AP^2 = ", sqrAP);

AP = PA = sqrt(sqrAP);
print("AP = ", AP);

cos_gamma_B = (AC^2 +BC^2 -AB^2)/(2*AC*BC)
print("cos_gamma_B = " ,cos_gamma_B)
gamma_B = acos(cos_gamma_B) / rho
print("gamma_B = ", gamma_B)


cos_gamma_P = (CP^2 +CA^2 - sqrAP)/(2 * CP * CA);
print("cos_gamma_P = ", cos_gamma_P);
gamma_P = acos(cos_gamma_P) / rho;
print("gamma_P = " ,gamma_P);


winkel_gamma = gamma_B + gamma_P;
print("gamma = ", winkel_gamma)

F2p = 0.5* BC * PC * sin(winkel_gamma * rho);
print("F'2 = ", F2p);

sqrPB = PC^2 + CB^2 - 2*PC*CB*cos(winkel_gamma * rho);
print("PB^2 = ", sqrPB);

PB = BP = sqrt(sqrPB);
print("PB = ", PB);

\\ 3-eck ABP
s = (AB + BP + PA)/2;
F_ABP = sqrt(s*(s - AB) * (s - BP) * (s - PA));
print("F_ABP = ", F_ABP)

q = (F_ABP + F2p - F1p)/(F_ABP - F2p + F1p)
print("q = ", q)

QA = AQ = (q*AB)/(1 + q)
QB = BQ = AB - QA
print("QA = ", AQ)
print("QB = ", QB)

\\ PROBE 1: 3-eck APQ
F_APQ = (q * F_ABP)/(1 + q)
print("F_APQ = ", F_APQ)

\\ PROBE 2: 3-eck BCD
F_BCD = 0.5 * CD * CB * sin(winkel_gamma * rho)
print("F_BCD = ", F_BCD)




