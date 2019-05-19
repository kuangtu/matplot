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
from snapshot_selenium import snapshot as driver
from pyecharts.render import make_snapshot


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
    high_price = aap_perf['High'].tolist()
    low_price = aap_perf['Low'].tolist()


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
    # candles.add_yaxis(series_name="", y_axis=price, tooltip_opts=opts.TooltipOpts(trigger="axis", is_show=True,
    #                                                                               trigger_on="mousemove|click"))
    candles.add_yaxis(series_name="K线",
                      y_axis=price,
                      tooltip_opts=opts.TooltipOpts(is_show=True, trigger='item'),
                      itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c", border_color="#8A0000",border_color0="#008F28")
                      )
    candles.set_global_opts(
                            title_opts=opts.TitleOpts(title="苹果-K线图"),
                            yaxis_opts=opts.AxisOpts
                            (is_scale=True,
                             splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)),
                             splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1))),
                             legend_opts=opts.LegendOpts(is_show=True, pos_right=True, orient='vertical', textstyle_opts=
                                                       opts.TextStyleOpts(font_size=10)),
                             datazoom_opts=[opts.DataZoomOpts()],
                            )
    candles.set_series_opts()

    line = Line()
    line.add_xaxis(xaxis_data=dates)
    line.add_yaxis(series_name='最高', y_axis=high_price, is_symbol_show=True,
                   label_opts=opts.LabelOpts(is_show=False))
    line.add_xaxis(xaxis_data=dates)
    line.add_yaxis(series_name='最低', y_axis=low_price, is_symbol_show=True,
                   label_opts=opts.LabelOpts(is_show=False))
    candles.overlap(line)
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
            .render()
    )

def office_demo():
    data = [
        [2320.26, 2320.26, 2287.3, 2362.94],
        [2300, 2291.3, 2288.26, 2308.38],
        [2295.35, 2346.5, 2295.35, 2345.92],
        [2347.22, 2358.98, 2337.35, 2363.8],
        [2360.75, 2382.48, 2347.89, 2383.76],
        [2383.43, 2385.42, 2371.23, 2391.82],
        [2377.41, 2419.02, 2369.57, 2421.15],
        [2425.92, 2428.15, 2417.58, 2440.38],
        [2411, 2433.13, 2403.3, 2437.42],
        [2432.68, 2334.48, 2427.7, 2441.73],
        [2430.69, 2418.53, 2394.22, 2433.89],
        [2416.62, 2432.4, 2414.4, 2443.03],
        [2441.91, 2421.56, 2418.43, 2444.8],
        [2420.26, 2382.91, 2373.53, 2427.07],
        [2383.49, 2397.18, 2370.61, 2397.94],
        [2378.82, 2325.95, 2309.17, 2378.82],
        [2322.94, 2314.16, 2308.76, 2330.88],
        [2320.62, 2325.82, 2315.01, 2338.78],
        [2313.74, 2293.34, 2289.89, 2340.71],
        [2297.77, 2313.22, 2292.03, 2324.63],
        [2322.32, 2365.59, 2308.92, 2366.16],
        [2364.54, 2359.51, 2330.86, 2369.65],
        [2332.08, 2273.4, 2259.25, 2333.54],
        [2274.81, 2326.31, 2270.1, 2328.14],
        [2333.61, 2347.18, 2321.6, 2351.44],
        [2340.44, 2324.29, 2304.27, 2352.02],
        [2326.42, 2318.61, 2314.59, 2333.67],
        [2314.68, 2310.59, 2296.58, 2320.96],
        [2309.16, 2286.6, 2264.83, 2333.29],
        [2282.17, 2263.97, 2253.25, 2286.33],
        [2255.77, 2270.28, 2253.31, 2276.22],
    ]

    def kline_base() -> Kline:
        c = (
            Kline()
                .add_xaxis(["2017/7/{}".format(i + 1) for i in range(31)])
                .add_yaxis("kline", data)
                .set_global_opts(
                yaxis_opts=opts.AxisOpts(is_scale=True),
                xaxis_opts=opts.AxisOpts(is_scale=True),
                title_opts=opts.TitleOpts(title="Kline-基本示例"),
            )
        )
        return c

    make_snapshot(driver, kline_base().render(), "kline.png")
if __name__ == '__main__':
    filename = "pycharts.csv"
    KLine(filename)
    # demo()
    # office_demo()

