from xirrCalculator import calculate_xirr
from datetime import datetime, timedelta

class SipProduct:
    @staticmethod
    def compute_product_returns(annual_contribution, contribution_years, maturity_year, maturity_value, start_date):
        cash_flows = []
        dates = []
        for i in range(contribution_years):
            cash_flows.append(-annual_contribution)
            dates.append(start_date + timedelta(days=365 * i))
        if maturity_year > contribution_years:
            for i in range(contribution_years, maturity_year):
                cash_flows.append(0)
                dates.append(start_date + timedelta(days=365 * i))

            

        total_investment = sum([cf for cf in cash_flows if cf < 0])
        absolute_return = maturity_value + total_investment
        return_percentage = (absolute_return / -total_investment) * 100
        xirr = calculate_xirr(cash_flows + [maturity_value], dates + [dates[-1] + timedelta(days=365)])
        return cash_flows, dates,{
            "Total Investment ₹": -total_investment,
            "Absolute Return ₹": absolute_return,
            "Return %": round(return_percentage, 2),
            "XIRR %": round(xirr * 100, 2) if xirr else "N/A"
        }