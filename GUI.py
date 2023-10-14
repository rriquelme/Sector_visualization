from PyQt5 import QtWidgets
import sys
import Symbol
import mplfinance as mpf
from plotly.graph_objects import Figure, Scatter
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import talib
import datetime

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QTabWidget):
    def __init__(self,):
        super(MainWindow,self).__init__()
        self.showMaximized()
        self.tab0 = QtWidgets.QWidget()
        self.addTab(self.tab0,"mplfinance")
        self.tab1 = QtWidgets.QWidget()
        self.addTab(self.tab1,"plotly")
        g0_layout = QtWidgets.QGridLayout()
        self.tab0.setLayout(g0_layout)
        g1_layout = QtWidgets.QGridLayout()
        self.tab1.setLayout(g1_layout)
        Symbols_to_test = ["SPY","XLY","XLC","XLK","XLI","XLB","XLE","XLP","XLV","XLU","XLF","XLRE"]
        fig = []
        for x in Symbols_to_test:
            s = Symbol.Symbol(x)
            blank_data = 4 # Blank data for plotting purposes...
            for blank_d in range(1,blank_data+1):
                s.data.loc[((datetime.datetime.now()+ datetime.timedelta(days=blank_d)).date())] = np.NAN 
            cut_data = -int(len(s.data['Close'])/4)
            macd, signal, histogram = talib.MACD(s.data['Close'])
            ema20 = talib.EMA(s.data["Close"],timeperiod=20)
            ema50 = talib.EMA(s.data["Close"],timeperiod=50)
            ema200 = talib.EMA(s.data["Close"],timeperiod=200)
            apds = [mpf.make_addplot(ema20.iloc[cut_data:],color='lime',alpha = 0.5),
                    mpf.make_addplot(ema50.iloc[cut_data:],color='green',alpha = 0.5),
                    mpf.make_addplot(ema200.iloc[cut_data:],color='blue',alpha = 0.5),
                    mpf.make_addplot(histogram.iloc[cut_data:],type='bar',width=0.7,panel=1,
                                    color='dimgray',alpha=1,secondary_y=True),
                    mpf.make_addplot(macd.iloc[cut_data:],panel=1,color='fuchsia',secondary_y=True),
                    mpf.make_addplot(signal.iloc[cut_data:],panel=1,color='b',secondary_y=True),
                ]
            s.data.index = pd.DatetimeIndex(s.data.index)
            fig.append(FigureCanvas(mpf.plot(
                s.data.iloc[cut_data:],
                # type='candle',
                title=x,
                returnfig=True,
                scale_padding={'left': 0.5, 'top': 6, 'right': 6, 'bottom': 2},
                figsize=(5, 10),
                addplot=apds,
                volume_panel=2,
                panel_ratios=(7,2,1),
                volume=True,
                tight_layout=True,
                style='charles'
            )[0]))
        count = 0
        for x in range(3):
            for y in range(4):
                g0_layout.addWidget(fig[count],x,y)
                count +=1
    def closeEvent(self,event):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Sectors')
    mw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

