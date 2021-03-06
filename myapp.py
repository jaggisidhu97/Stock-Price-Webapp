import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
Made by **Jagmeet Singh Sidhu**
""")


st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Gooogle

""")



tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end ='2015-5-31')
st.write(""" Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""Volume Price""")
st.line_chart(tickerDf.Volume)

st.write("""

Shown are the stock **closing price** and **volume** of TESLA

""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end ='2015-5-31')
st.write(""" Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""Volume Price""")
st.line_chart(tickerDf.Volume)
