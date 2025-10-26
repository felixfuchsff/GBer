\\ PARI GP

cal_zentriwinkel_bisection = (a, s, epsilon=1E-5, iteration=20) -> {
    RHS = (8*a)/s^2; /* CONST */
    left = 0;
    right = Pi;
    alpha = 0;
    diff = 2*epsilon;
    count_iter = 0;
    for(n = 1, iteration, count_iter = n;
        alpha = (right + left)/2;
        lhs = (alpha - sin(alpha)) / (sin(alpha/2)^2);
        diff = lhs - RHS;
        if( abs(diff) <=epsilon, break );
        if( diff < 0, left = alpha );
        if( diff > 0, right = alpha );
    );
    return ([alpha, diff, count_iter]);
}

a = 100.1214;
s = 49.245363;

result = cal_zentriwinkel_bisection(a, s, epsilon=1E-16, iteration=40);
alpha = result[1];
print(result);
radius =s/2/sin(alpha/2);
print(radius);



