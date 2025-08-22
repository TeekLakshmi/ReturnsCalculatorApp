import pandas as pd

def export_to_excel(dates, cash_flows, result):
    df = pd.DataFrame({
        "Date": dates,
        "Cash Flow": cash_flows
    })
    for k, v in result.items():
        df.loc[len(df)] = [k, v]
    df.to_excel("investment_summary.xlsx", index=False)
