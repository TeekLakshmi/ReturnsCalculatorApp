import streamlit as st
from datetime import datetime

from exportToExcel import export_to_excel
from incomeMaturityBenefitProduct import IncomeMaturityBenefitProduct
from lumpSumProduct import LumpSumProduct
from plotResults import plot_cash_flows
from sipProduct import SipProduct
from wealthPlanProduct import WealthPlanProduct
import streamlit as st
from streamlit_google_auth import Authenticate


plot_cash_flows=False

def displayResult(cash_flows, dates,result):
    st.subheader("📊 Results")
    for key, value in result.items():
        st.metric(label=key, value=f"{value}" )
    if plot_cash_flows:
        st.plotly_chart(plot_cash_flows(dates, cash_flows), use_container_width=True)



authenticator = Authenticate(
    secret_credentials_path='client_secret.json',
    cookie_name='auth_cookie',
    cookie_key='super_secret_key',
    redirect_uri='http://localhost:8501',
)

authenticator.check_authentification()

if not st.session_state.get('connected', False):    
    login_url = authenticator.get_authorization_url()
    st.link_button("🔐 Login with Google", login_url)
    st.title("Welcome to Returns Calculator App. Please log in to access the Investment Plan Comparison Dashboard")
else:
    print('Authenticated   ')
    user_info = st.session_state['user_info']
    st.image(user_info.get('picture'))
    st.success(f"Welcome, {user_info.get('name')}!")
    st.write(f"Email: {user_info.get('email')}")
    if st.button("Logout"):
        authenticator.logout()

    st.title("📊 Investment Plan Comparison Dashboard")

    plan_type = st.selectbox("Choose Plan Type", ["Wealth Plan","Lump Sum", "SIP","Income Maturity Benefit"])

    start_date = st.date_input("Start Date", value=datetime.today())
    maturity_year = st.number_input("Maturity Year", value=12)
    maturity_value = st.number_input("Maturity Value (₹)", value=1758000)

    if plan_type == "Lump Sum":
        initial_investment = st.number_input("Initial Investment (₹)", value=200000)
        if st.button("Calculate"):
            cash_flows,dates,result=LumpSumProduct.compute_product_returns(
                initial_investment,
                maturity_year,
                maturity_value,
                datetime.combine(start_date, datetime.min.time())
            )
            displayResult(cash_flows, dates,result)

    elif plan_type == "SIP":
        annual_contribution = st.number_input("Annual Contribution (₹)", value=200000)
        contribution_years = st.number_input("Contribution Duration (Years)", value=5)
        if st.button("Calculate"):        
            cash_flows,dates,result = SipProduct.compute_product_returns(
                annual_contribution,
                contribution_years,
                maturity_year,
                maturity_value,
                datetime.combine(start_date, datetime.min.time())
            )
            displayResult(cash_flows, dates,result)
            
    elif plan_type == "Wealth Plan":
        initial_investment = st.number_input("Initial Investment (₹)", value=200000)
        annual_contribution = st.number_input("Annual Contribution (₹)", value=200000)
        contribution_years = st.number_input("Contribution Duration (Years)", value=5)
        if st.button("Calculate"):
            cash_flows,dates,result = WealthPlanProduct.compute_product_returns(
                initial_investment,
                annual_contribution,
                contribution_years,
                maturity_year,
                maturity_value,
                datetime.combine(start_date, datetime.min.time())
            )
            
            displayResult(cash_flows, dates,result)

    elif plan_type == "Income Maturity Benefit":
        initial_investment = st.number_input("Initial Investment (₹)", value=200000)
        annual_contribution = st.number_input("Annual Contribution (₹)", value=200000)
        contribution_years = st.number_input("Contribution Duration (Years)", value=5)
        annual_return = st.number_input("Annual Return (₹)", value=100000)
        return_start_year = st.number_input("Return Start Year", value=1)
        return_end_year = st.number_input("Return End Year", value=12)
        
        if st.button("Calculate"):
            cash_flows,dates,result = IncomeMaturityBenefitProduct.compute_product_returns(
                datetime.combine(start_date, datetime.min.time()),
                initial_investment,
                annual_contribution,
                contribution_years,
                annual_return,
                return_start_year,
                return_end_year,
                maturity_value
            )
            
            displayResult(cash_flows, dates,result)
