# CAPM_app
Computational implementation of Sharpe's (1964) Capital Asset Pricing Model for Brazilian stock exchange B3.

This application collects data, calculates the parameters of CAPM and tests the statistical significance of those parameters for any asset traded in Brazilian Stock Exchange (B3). The model is estimated using Brazilian’s interbank interest rate (CDI) as the risk free return and B3 stock market index (Ibovespa) return as a proxy for market return.  We implemented the CAPM by using Python programming language.

For the proper operation of the application, the user must have Python and the following packages already installed:

1) NumPy
2) pandas
3) Matplotlib
4) Statsmodels
5) YahooFinancials 1.5 (API available at https://pypi.org/project/yahoofinancials/)
6) pySGS (API available at https://pypi.org/project/pysgs/)

For the program usage, the user must open the 'main.py' file in the terminal typing: 'python3 main.py'. The application will require an B3 asset input and then the CAPM will be calculated and its main results will be displayed at the terminal.

For changing the data collection period, the user must alter the default dates at 'data_collect.py'.

The unit tests are available at 'Unit tests' folder.

The (not oficially released) working paper is available at https://drive.google.com/open?id=1Anlw8nHBZwFORu3g9sl7-rrjZjmoUpeg.

Currently the application is in its first version and it does not provide an user-friendly interface. It also may presents some unnoticed bugs or crashes. In the case of finding some bug or suggestions for further development, please contact me at assoniraiter@gmail.com.
