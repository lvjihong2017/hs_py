# import requests
#
#
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# # 文档网址 https://www.alphavantage.co/documentation/#weeklyadj
# # api-key=9KE758YHG3AZU0W2
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=000001.SS&apikey=9KE758YHG3AZU0W2'
# url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=601127.SHZ&apikey=9KE758YHG3AZU0W2'
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=9KE758YHG3AZU0W2'
# # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey=9KE758YHG3AZU0W2'
#
# r = requests.get(url)
# data = r.json()
#
# print(data)

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf

# 创建主窗口
root = tk.Tk()
root.title("A股分时图")

# 获取A股股票数据（这里以腾讯控股作为示例）
stock = yf.Ticker("0700.HK")
data = stock.history(period="1d", interval="5m")

# 创建分时图
figure = Figure(figsize=(6, 4))
plot = figure.add_subplot(1, 1, 1)
plot.plot(data.index, data['Close'])

# 创建画布并将分时图添加到Tkinter窗口
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack()

# 运行Tkinter主循环
root.mainloop()
