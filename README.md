# ReturnsCalculatorApp
ReturnsCalculatorApp is a system design to compute returns of various investments schemes by taking inputs and computing absolute returns in terms of XIRR.

Currently supported return computations are
Income+maturity benefit -- Invest for #Years ->  wait for #Years -> Receive Regular income for #Years -> at maturity receive Maturity benefit
Wealth Plan -- Invest for #years -> Wait for #years -> Receive maturity benefir as lumpsum
Lump sum -> Invest one time -> Wait for #years -> Receive lumpsum
SIP -> Invest regularly-> Wait for # years (optional) -> Receive


This is a study project to explore the following 
Python 3.9
streamlit
scipy
pandas
plotly
streamlit-authenticator

Objective of this application is to do project and learn. This may be enhanced later as required.

Anyone is free to download and use this but please do modify in local repository only.

Dockerfile is included to have an option to containerize the application.

NOTE: client_secret.json is not included in this repository due to security reasons but referred in the code. Do create own Google OAUTH client and add in the project to enable Google based authentication.


To Run: python -m streamlit run dashboard.py