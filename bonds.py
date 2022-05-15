
  
def cashflow_times(n, m):
    """
    develops list of the times at which a bond makes coupon payments, 
    with n years and m coupon payments per year
    """
    return [num for num in range(1, n * m + 1)]


def discount_factors(r, n, m):
    """
    calculates and returns a list of discount factors for a given annualized 
    interest rate r, for n years, and m discounting periods per year. 
    """
    return [1 / ((1 + (r / m)) ** i) for i in range(1, n * m + 1)]



def bond_cashflows(fv, c, n, m):
    """
    calculates and returns a list of cashflows for a bond.
    The parameters are: 
    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year.
    """
    res = [(c / m) * fv] * (n * m)
    res[-1] += fv
    return res


def bond_price(fv, c, n, m, r):
    """
    calculates and returns the price of a bond. 
    The parameters are: 
    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and r, the annualized yield to maturity of the bond
    """
    cf = cashflow_times(n,m)
    bcf = bond_cashflows(fv,c,n,m)
    df = discount_factors(r,n,m)
    res = [bcf[i - 1] * df[i - 1] for i in cf]
    return sum(res) 


def helper(fv, c, n, m, price, low , high):
    """
    calculates the annualized yield_to_maturity on a bond. 
    The parameters are: 
    fv is the future (maturity) value of the bond;
    c is the annual coupon rate expressed as percentage per year;
    n is the number of years until maturity;
    m is the number of coupon payments per year;
    and price is the current market price of the bond
    """
    r = (low + high) / 2 
    temp = bond_price(fv, c, n, m, r)
  
    # if calculated bond price is close enough to actual bond price 
    if abs(temp - price) < 0.0001:
        return r
    
    # if calculated bond price is less than actual bond price 
    if temp < price:
        # move upper bound lower 
        high = r
        return helper(fv, c, n, m, price, low, high)
    
    # if calculated bond price is greated than actual bond price 
    else:
        # move lower bound higher
        low = r
        return helper(fv, c, n, m, price, low, high)


def bond_yield_to_maturity(fv, c, n, m, price):
    low = 0
    high = 1 
    return helper(fv, c, n ,m ,price ,low ,high)