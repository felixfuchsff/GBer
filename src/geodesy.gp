\\ PARI GP

cal_zentriwinkel_bisection = (a, s, epsilon=1E-5, iteration=20) -> {
    RHS = (8*a)/s^2;
    left = 0;
    right = Pi;
    alpha = 0;
    diff = 2*epsilon;
    i = 0;
    for(n = 1, iteration, ;
        i = n;
        alpha = (right + left)/2;
        lhs = (alpha - sin(alpha)) / (sin(alpha/2)^2);
        diff = lhs - RHS;
        if(abs(diff) <=epsilon, break());
        if(diff < 0, left = alpha);
        if(diff > 0, right = alpha);
    );
    return ([alpha, diff, i]);
}

a = 100.1214;
s = 49.245363;

r = cal_zentriwinkel_bisection(a, s, epsilon=1E-5, iteration=40);
print(r);
