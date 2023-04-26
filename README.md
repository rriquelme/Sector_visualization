# Sector_visualization
- This program generates an orverview of the US stock sectors using Yahoo Finance library.
- In the program you have an overview of SPY, XLY, XLC, XLK, XLI, XLB, XLE, XLP, XLV, XLU, XLF, XLRE.
- Indicators used: EMA20, EMA50, EMA200, MACD.

# Screenshot
![Screenshot](Screenshot.png)

# Explanation
- This program uses the Symbol.py library that abstracts Yahoo Finance, so the source of the data can be easily swapped to obtain the same result.
- The user interface has been made with PyQt5.
- The charts are made using mplfinance.
- The program uses a cache file for every symbol that it download so the program only query the latest data, not all the data every time.