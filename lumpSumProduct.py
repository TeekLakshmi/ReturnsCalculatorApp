from xirrCalculator import calculate_xirr
from datetime import datetime, timedelta

class LumpSumProduct:
    @staticmethod
    def compute_product_returns(initial_investment, maturity_year, maturity_value, start_date=datetime.today()):
        cash_flows = [-initial_investment]
        dates = [start_date]
        
        cash_flows.append(maturity_value)
        dates.append(start_date + timedelta(days=365 * maturity_year))

        total_investment = sum([cf for cf in cash_flows if cf < 0])
        absolute_return = maturity_value + total_investment
        return_percentage = (absolute_return / -total_investment) * 100
        xirr = calculate_xirr(cash_flows, dates)

        return cash_flows, dates,{
            "Total Investment ₹": -total_investment,
            "Absolute Return ₹": absolute_return,
            "Return %": round(return_percentage, 2),
            "XIRR %": round(xirr * 100, 2) if xirr else "Could not compute"
        }