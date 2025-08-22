from scipy.optimize import newton

def calculate_xirr(cash_flows, dates):
    def xirr_func(rate):
        return sum([
            cf / ((1 + rate) ** ((d - dates[0]).days / 365))
            for cf, d in zip(cash_flows, dates)
        ])
    try:
        return newton(xirr_func, 0.1)
    except RuntimeError:
        return None
    
