from datetime import timedelta

from xirrCalculator import calculate_xirr

class IncomeMaturityBenefitProduct:
    @staticmethod
    def compute_product_returns(start_date, initial_investment, annual_contribution, contribution_years, annual_return, return_start_year, return_end_year, maturity_value):
        cash_flows = []
        dates = []

        # Initial investment
        cash_flows.append(-initial_investment)
        dates.append(start_date)

        # Annual contributions
        for i in range(1, contribution_years + 1):
            cash_flows.append(-annual_contribution)
            dates.append(start_date + timedelta(days=365 * i))

        if return_start_year > contribution_years:
            for i in range(contribution_years, return_start_year):
                cash_flows.append(0)
                dates.append(start_date + timedelta(days=365 * i))

        # Annual returns
        for i in range(return_start_year, return_end_year + 1):
            cash_flows.append(annual_return)
            dates.append(start_date + timedelta(days=365 * i))

        # Maturity payout
        cash_flows.append(maturity_value)
        dates.append(start_date + timedelta(days=365 * return_end_year))

        total_investment = sum([cf for cf in cash_flows if cf < 0])
        
        absolute_return = maturity_value + total_investment
        
        for i in range(return_start_year, return_end_year + 1):
            absolute_return+=annual_return
        
        return_percentage = (absolute_return / -total_investment) * 100
        xirr = calculate_xirr(cash_flows, dates)

        return cash_flows, dates, {
            "Total Investment ₹": -total_investment,
            "Absolute Return ₹": absolute_return,
            "Return %": round(return_percentage, 2),
            "XIRR %": round(xirr * 100, 2) if xirr else "Could not compute"
        }
    
