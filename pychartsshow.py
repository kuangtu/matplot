import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import talib as ta

from pyecharts.charts import Kline, Line
from pyecharts.charts import Candlestick
from pyecharts import options as opts


def KLine(filename):
    col_features = ['Open', 'High', 'Low', 'Close']
    col_order = ['Open', 'Close', 'Low', 'High']
    perf = pd.read_csv("pyechartsdata.csv", index_col=0, parse_dates=True, dayfirst=True)
    aap_perf = perf[perf['Symbol'] == 'AAPL']
    aap_perf = aap_perf[col_features]
    print(aap_perf.head())
    aap_perf = aap_perf[col_order]
    print(aap_perf.head())
    # print(aap_perf.head())
    dates = aap_perf.index
    dates = aap_perf.index.strftime("%Y-%m-%d")
    dates = dates.tolist()
    price = aap_perf.values.tolist()
    print(type(dates))
    print(type(price))


    # (
    #     Candlestick(init_opts=opts.InitOpts(width="1440px", height="720px"))
    #         .add_xaxis(xaxis_data=dates)
    #         .add_yaxis(series_name="", y_axis=price)
    #         .set_series_opts()
    #         .set_global_opts(
    #         yaxis_opts=opts.AxisOpts(
    #             splitline_opts=opts.SplitLineOpts(
    #                 is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)
    #             )
    #         )
    #     ).render("kline.html")
    # )
    candles = Candlestick(init_opts=opts.InitOpts(width="1440px", height="720px"))
    candles.add_xaxis(xaxis_data=dates)
    candles.add_yaxis(series_name="", y_axis=price, tooltip_opts="axis")
    candles.set_global_opts(opts.LineStyleOpts(width=2, type_='solid'), opts.TitleOpts(title="APP k-line"),
                            yaxis_opts=opts.AxisOpts
                            (splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(width=1))),
                            datazoom_opts=)
    candles.render("kline.html")

    # kline = Kline("AAP", title_pos='center')
    # kline = Kline("AAP")
    # kline = Kline("K 线图示例")
    # kline = Kline()
    # kline.add_xaxis(dates)
    # kline.add_yaxis("K-Line", price)
    # kline.render()
    # kline.add('K-Line', dates, price, tooltip_tragger='axis', is_datazoom_show=True,
    #           legend_pos='right', legend_orient='vertical', legend_text_size=10)
    # line2 = Line()
    #
    # cols = ['High', "low"]
    # for c in cols:
    #     line2.add(c, dates, price[c], tooltip_tragger='axis')
    #
    # kline.overlap(line2)
    # overlap.add(kline)
    # overlap.add(line2)

def demo():
    x_data = ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]
    y_data = [[20, 30, 10, 35], [40, 35, 30, 55], [33, 38, 33, 40], [40, 40, 32, 42]]

    (
        Candlestick(init_opts=opts.InitOpts(width="1440px", height="720px"))
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="", y_axis=y_data)
            .set_series_opts()
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)
                )
            )
        )
            .render("basic_candlestick.html")
    )

if __name__ == '__main__':
    filename = "pycharts.csv"
    KLine(filename)
    # demo()

