import plotly.graph_objects as go

def plot_cash_flows(dates, cash_flows):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=dates, y=cash_flows, name="Cash Flow", marker_color="teal"))
    fig.update_layout(title="Investment Cash Flow Timeline", xaxis_title="Date", yaxis_title="Amount (₹)")
    return fig
