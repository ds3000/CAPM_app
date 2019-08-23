
############ PACKAGES IMPORTATION ###########

import data_collect as dc
import transformation as tr
import capm as cp
import pandas as pd
from sgs import SGS
import unittest

# Data collected from an outside source

Tickers_YF = pd.DataFrame([26.719929,26.640287,27.257513,26.919035,27.277422,27.008631,26.580557,26.461092,26.958855,26.938944])
Tickers_YF.columns = ['adjclose']

MarketReturn_YF = pd.DataFrame([97526.00,96510.00,97659.00,96545.00,96932.00,97886.00,97240.00,97603.00,97307.00,95584.00])
MarketReturn_YF.columns = ['adjclose']

RiskFree_YF = pd.DataFrame([0.02462,0.02462,0.02462,0.02462,0.02462,0.02462,0.02462,0.02462,0.02462,0.02462,0.02462])
RiskFree_YF.columns = ['VALOR']

########### DATA INPUT ##############

# Defining Tickers, Market Return and Risk-Free Rate for usage

Tickers = 'PETR4.SA'
MarketReturn = ['^BVSP']
RiskFree = SGS()

Current = Tickers
Current2 = MarketReturn[0]

# Defining Tickers, Market Return and Risk Free Rate parameters

Period = 'daily'
Start_Date = '2000-01-01'
End_Date = '2019-03-01'

RF_Start_Date = '01/01/2000'
RF_End_Date = '01/03/2019'
RF_Code = 12

########## DATA PROCESSING ##########


# Collecting Tickers, Market Return and Risk Free Rate data

Tickers = dc.Get_Tickers(Tickers)
MarketReturn = dc.Get_MarketReturn(MarketReturn)
RiskFree = dc.Get_RiskFree()

Tickers_CAPM = pd.DataFrame(Tickers['PETR4.SA']['prices'])
Tickers_CAPM = pd.DataFrame(Tickers_CAPM['adjclose'])

MarketReturn_CAPM = pd.DataFrame(MarketReturn['^BVSP']['prices'])
MarketReturn_CAPM = pd.DataFrame(MarketReturn_CAPM['adjclose'])

RiskFree_CAPM = pd.DataFrame(RiskFree['VALOR'])


class TestCalculateReturns(unittest.TestCase):

    def test_calculate_tickerdata(self):

        self.assertEqual(Tickers_CAPM.columns[0],Tickers_YF.columns[0])

    def test_calculate_mrdata(self):

        self.assertEqual(MarketReturn_CAPM.columns[0],MarketReturn_YF.columns[0])

    def test_calculate_rfdata(self):

        self.assertEqual(RiskFree_CAPM.columns[0],RiskFree_YF.columns[0])
