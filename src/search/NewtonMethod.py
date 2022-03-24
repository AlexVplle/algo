def NewtonMethod(function, gradientFunction, firstTerm : int, errorMargin : int) :
    """
    Quadratic convergence
    conditions : C1-smoothness function
    function and gradientFunction are lambda functions
    """
    xk = firstTerm
    while True :
        xkNew = xk - function(xk)/gradientFunction(xk)
        if xk - xkNew < errorMargin : return xk, errorMargin
        xk = xkNew