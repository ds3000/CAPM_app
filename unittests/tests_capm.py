import unittest
import transformation as tr
import data_collect as dc
import pandas as pd
import capm as cp
import numpy as np
from yahoofinancials import YahooFinancials

# Expected values

Gretl_alpha = np.array(0.0021536163249977194)
Gretl_alpha_std = np.array(0.004697294467791647)
Gretl_alpha_p = np.array(0.6605022754189103)

Gretl_beta = np.array(0.557795729239579)
Gretl_beta_std = np.array(0.47519574125054403)
Gretl_beta_p = np.array(0.27885186440084)

# Program config

Ticker_Asset = 'PETR4.SA'
Ticker_MR = '^BVSP'
Ticker_RF = 12

Current = Ticker_Asset
Current2 = Ticker_MR

Period = 'daily'
Start_Date = '2019-02-15'
End_Date = '2019-03-01'

Asset =  dc.Get_Tickers(Ticker_Asset)
Market = dc.Get_MarketReturn(Ticker_MR)
RiskFree = dc.Get_RiskFree()

Tickers_DF = tr.Tickers_Cleaning(Asset,Current)
MarketReturn_DF = tr.MarketReturn_Cleaning(Market,Current2)
RiskFree_DF = tr.RiskFree_Cleaning(RiskFree)

ExcessTicker_DF = tr.ExcessTicker_DF(Tickers_DF,RiskFree_DF)
ExcessMarket_DF = tr.ExcessMarket_DF(MarketReturn_DF,RiskFree_DF)

Tickers_Return = tr.Tickers_Var(ExcessTicker_DF)
MarketReturn_Return = tr.MarketReturn_Var(ExcessMarket_DF)

Tickers_Subtracted = tr.Tickers_Sub(Tickers_Return) #retorna Series / float64
MarketReturn_Subtracted = tr.MarketReturn_Sub(MarketReturn_Return) #retorna Series / float64

DataMaster = tr.Master(Tickers_Subtracted,MarketReturn_Subtracted)

X = DataMaster['ExcessReturnTicker']
Y = DataMaster['ExcessReturnMarket']

# Calculating CAPM by OLS and collecting general results of the regression

CAPM_Result = cp.CAPM_OLS(X,Y)

CAPM_alpha = CAPM_Result.params['const']
CAPM_alpha = np.array(CAPM_alpha)

CAPM_alpha_std = CAPM_Result.bse['const']
CAPM_alpha_std = np.array(CAPM_alpha_std)

CAPM_alpha_p = CAPM_Result.pvalues['const']
CAPM_alpha_p = np.array(CAPM_alpha_p)

CAPM_beta = CAPM_Result.params['ExcessReturnMarket']
CAPM_beta = np.array(CAPM_beta)

CAPM_beta_std = CAPM_Result.bse['ExcessReturnMarket']
CAPM_beta_std = np.array(CAPM_beta_std)

CAPM_beta_p = CAPM_Result.pvalues['ExcessReturnMarket']
CAPM_beta_p = np.array(CAPM_beta_p)

class TestCalculateResults(unittest.TestCase):

    def test_calculate_alpha_results(self):

        self.assertEqual(CAPM_alpha,Gretl_alpha)

    def test_calculate_alpha_std(self):

        self.assertEqual(CAPM_alpha_std,Gretl_alpha_std)

    def test_calculate_alpha_p(self):

        self.assertEqual(CAPM_alpha_p,Gretl_alpha_p)

    def test_calculate_beta_results(self):

        self.assertEqual(CAPM_beta,Gretl_beta)

    def test_calculate_beta_std(self):

        self.assertEqual(CAPM_beta_std,Gretl_beta_std)

    def test_calculate_beta_p(self):

        self.assertEqual(CAPM_beta_p,Gretl_beta_p)
