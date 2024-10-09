import yfinance as yf
import streamlit as st

tickerSymbols = ['GOOGL', 'AAPL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'DIS', 'PYPL']
startDate = '2010-5-10'
endDate = '2024-10-8'

selectedTicker = st.selectbox("Select a ticker: ", tickerSymbols)

st.write(f"""
         # Stock Price App
         This is the stock closing price and volume of **{selectedTicker}** between {startDate} and {endDate}
         """)


tickerData = yf.Ticker(selectedTicker)

tickerDf = tickerData.history(period = '1d', start=startDate, end=endDate)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)