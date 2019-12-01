import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import talib as ta

from pyecharts.charts import Kline, Line,Grid, Bar
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
    candles = Candlestick(init_opts=opts.InitOpts(width="1440px", height="720px"))
    candles.add_xaxis(xaxis_data=dates)
    candles.add_yaxis(series_name="K线",
                      y_axis=price,
                      tooltip_opts=opts.TooltipOpts(is_show=True, trigger='item'),
                      itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c", border_color="#8A0000",border_color0="#008F28")
                      )
    candles.set_global_opts(
                            title_opts=opts.TitleOpts(title="苹果-K线图", pos_top='top'),
                            yaxis_opts=opts.AxisOpts
                            (is_scale=True,
                            splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)),
                            splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),
                            name="点位", name_location="middle", name_gap=40,
                             name_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight="bold")
                            ),
                            xaxis_opts=opts.AxisOpts(name="日期", name_location="middle", name_gap=40,
                            name_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight="bold")),
                            legend_opts=opts.LegendOpts(is_show=True, pos_right=True, orient='vertical', textstyle_opts=
                                                      opts.TextStyleOpts(font_size=10)),
                            datazoom_opts=[opts.DataZoomOpts()],
                            toolbox_opts=opts.ToolboxOpts()
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

def maLine():
    col_features = ['Close']
    win_peroid = [5, 10, 20]
    # col_order = ['Open', 'Close', 'Low', 'High']
    perf = pd.read_csv("pyechartsdata.csv", index_col=0, parse_dates=True, dayfirst=True)
    aap_perf = perf[perf['Symbol'] == 'AAPL']
    aap_perf = aap_perf[col_features]
    print(aap_perf.head())
    # aap_perf = aap_perf[col_order]
    # print(aap_perf.head())
    # print(aap_perf.head())
    dates = aap_perf.index
    dates = aap_perf.index.strftime("%Y-%m-%d")
    dates = dates.tolist()
    price = aap_perf.values.tolist()
    print(type(dates))
    print(type(price))

    # high_price = aap_perf['High'].tolist()
    # low_price = aap_perf['Low'].tolist()


    avgline = Line(init_opts=opts.InitOpts(width="1440px", height="720px"))
    avgline.add_xaxis(xaxis_data=dates)
    # avgline.add_yaxis(series_name="", y_axis=price, tooltip_opts=opts.TooltipOpts(trigger="axis", is_show=True,
    #                                                                               trigger_on="mousemove|click"))
    avgline.add_yaxis(series_name="close",
                      y_axis=price,
                      tooltip_opts=opts.TooltipOpts(is_show=True, trigger='item'),
                      # itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c", border_color="#8A0000",border_color0="#008F28"),
                      is_symbol_show=True, label_opts=opts.LabelOpts(is_show=False)
                      )
    avgline.set_global_opts(
        title_opts=opts.TitleOpts(title="苹果-均线走势", pos_top='top'),
        yaxis_opts=opts.AxisOpts
        (is_scale=True,
         splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(width=1)),
         splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)),
         name="点位", name_location="middle", name_gap=40,
         name_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight="bold")
         ),
        xaxis_opts=opts.AxisOpts(name="日期", name_location="middle", name_gap=40,
                                 name_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight="bold")),
        legend_opts=opts.LegendOpts(is_show=True, pos_right=True, orient='vertical', textstyle_opts=
        opts.TextStyleOpts(font_size=10)),
        datazoom_opts=[opts.DataZoomOpts()],
        toolbox_opts=opts.ToolboxOpts()
    )
    avgline.set_series_opts()

    line = Line()
    for wp in win_peroid:
        MA_price = ta.MA(aap_perf['Close'].values, timeperiod=wp)

        line.add_xaxis(xaxis_data=dates)
        line.add_yaxis(series_name='MA' + str(wp), y_axis=MA_price, is_symbol_show=True,
                       label_opts=opts.LabelOpts(is_show=False))
    avgline.overlap(line)
    avgline.render("mvline.html")

def rsiLine():
    col_features = ['Close']
    win_peroid = [5, 10, 20]
    # col_order = ['Open', 'Close', 'Low', 'High']
    perf = pd.read_csv("pyechartsdata.csv", index_col=0, parse_dates=True, dayfirst=True)
    aap_perf = perf[perf['Symbol'] == 'AAPL']
    aap_perf = aap_perf[col_features]
    print(aap_perf.head())
    # aap_perf = aap_perf[col_order]
    # print(aap_perf.head())
    # print(aap_perf.head())
    dates = aap_perf.index
    dates = aap_perf.index.strftime("%Y-%m-%d")
    dates = dates.tolist()
    price = aap_perf.values.tolist()
    print(type(dates))
    print(type(price))
    print(price)

    # high_price = aap_perf['High'].tolist()
    # low_price = aap_perf['Low'].tolist()


    avgline = Line(init_opts=opts.InitOpts(width="1440px", height="720px"))
    avgline.add_xaxis(xaxis_data=dates)
    avgline.add_yaxis(series_name="close",
                      y_axis=price,
                      )
    avgline.extend_axis(yaxis=opts.AxisOpts(
                    name="RSI强弱",
                    name_location="middle",
                    name_gap=40,
                    position='right',
                    axislabel_opts=opts.LabelOpts(formatter="{value}"),
                    interval=10,
                    axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#d14a61")),
                    splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(opacity=1))
    ))
    avgline.set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    avgline.set_global_opts(
        title_opts=opts.TitleOpts(title="苹果-价格走势", pos_top='top'),
        yaxis_opts=opts.AxisOpts
        (
            name="股票价格",
            name_location='middle',
            name_gap=50,
            position='left',
            # offset=80,
            # min_=0, max_=100,
            is_scale=True,
            splitline_opts=opts.SplitLineOpts(
                is_show=True,
                linestyle_opts=opts.LineStyleOpts(width=1)),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True,
                areastyle_opts=opts.AreaStyleOpts(opacity=1)),
            name_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight="bold"),
            axislabel_opts=opts.LabelOpts(formatter="{value} ($)"),
         ),
        datazoom_opts=[opts.DataZoomOpts()],
        toolbox_opts=opts.ToolboxOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_right=True,
            orient='vertical',
            textstyle_opts=opts.TextStyleOpts(
                font_size=10)),
        xaxis_opts=opts.AxisOpts(
            name="日期",
            name_location="middle",
            name_gap=30,
            name_textstyle_opts=opts.TextStyleOpts(
                font_size=15,
                font_weight="bold")),
    )
    line = Line()
    wp = 14
    RSI = ta.RSI(np.array(aap_perf['Close']), timeperiod=wp)
    line.add_xaxis(xaxis_data=dates)
    line.add_yaxis(series_name='RSI',
                   y_axis=RSI,
                   yaxis_index=1,
                   label_opts=opts.LabelOpts(
                       is_show=False))
    line.add_yaxis(series_name='Support',
                   y_axis=30 * np.ones(np.shape(RSI)),
                   label_opts=opts.LabelOpts(
                       is_show=False),
                   yaxis_index=1,)
    line.add_yaxis(series_name='Resistance',
                   y_axis=70 * np.ones(np.shape(RSI)),
                   label_opts=opts.LabelOpts(
                       is_show=False),
                   yaxis_index=1)

    line.set_series_opts(linestyle_opts=opts.LineStyleOpts(type_='dashed'))

    avgline.overlap(line).render("rsi.html")

def grid_mutil_yaxis() -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"))
def multi_y():
    col_features = ['Close']
    win_peroid = [5, 10, 20]
    # col_order = ['Open', 'Close', 'Low', 'High']
    perf = pd.read_csv("pyechartsdata.csv", index_col=0, parse_dates=True, dayfirst=True)
    aap_perf = perf[perf['Symbol'] == 'AAPL']
    aap_perf = aap_perf[col_features]
    print(aap_perf.head())
    dates = aap_perf.index
    dates = aap_perf.index.strftime("%Y-%m-%d")
    dates = dates.tolist()
    price = aap_perf.values.tolist()
    wp = 14
    RSI = ta.RSI(np.array(aap_perf['Close']), timeperiod=wp)
    colors = ['#5793f3', '#d14a61', '#675bba']
    x_data = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    rainfall_capacity = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    average_temperature = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

    line1 = (
        Line(init_opts=opts.InitOpts(width="1680px", height="800px"))
            .add_xaxis(
            xaxis_data=dates
        )
            # .add_yaxis(
            # series_name="蒸发量",
            # y_axis=evaporation_capacity,
            # yaxis_index=0,
            # color=colors[1]
        # )
            .add_yaxis(
            series_name="点位",
            y_axis=price,
            yaxis_index=0,
            color=colors[0]
        )
        #     .extend_axis(
        #     yaxis=opts.AxisOpts(
        #         name="蒸发量",
        #         type_="value",
        #         min_=0,
        #         max_=250,
        #         position="right",
        #         axisline_opts=opts.AxisLineOpts(
        #             linestyle_opts=opts.LineStyleOpts(color=colors[1])
        #         ),
        #         axislabel_opts=opts.LabelOpts(
        #             formatter="{value} ml"
        #         )
        #     )
        # )
            .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="点位",
                # min_ = 100,
                # max_ = 200,
                min_=0,
                max_=500,
                # is_scale=True,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color=colors[2])
                ),
                axislabel_opts=opts.LabelOpts(
                    formatter="{value}点"
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        opacity=1
                    )
                )
            )
        )
            .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="RSI",
                min_=0,
                max_=100,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color=colors[0])
                ),
                axislabel_opts=opts.LabelOpts(
                    formatter="{value} 值"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross"
            ),
        )
    )

    line2 = (
        Line()
            .add_xaxis(
            xaxis_data=dates
        )
            .add_yaxis(
            series_name="RSI",
            y_axis=RSI,
            yaxis_index=1,
            color=colors[2],
        )
    )

    line1.overlap(line2).render("multiple_y_axes.html")

def barline():
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
    months = ["{}月".format(i) for i in range(1, 13)]
    line1 = (
        Line()
        .add_xaxis(months)
        .add_yaxis("蒸发量", v1)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5,
                is_scale=True
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Overlap-bar+line"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} ml")
            ),

            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross"
            ),
        )
    )

    line2 = Line().add_xaxis(months).add_yaxis("平均温度", v3, yaxis_index=1)
    line1.overlap(line2)
    return line1

def GridDemo():
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

    aap_close = perf[perf['Symbol'] == 'AAPL']
    aap_close= aap_close['Close'].values.tolist()

    candles = Candlestick(
        init_opts=opts.InitOpts(
            width="1440px",
            height="720px"))
    candles.add_xaxis(xaxis_data=dates)
    candles.add_yaxis(
        series_name="K线",
        y_axis=price,
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            trigger='item'),
        itemstyle_opts=opts.ItemStyleOpts(
            color="#ec0000",
            color0="#00da3c",
            border_color="#8A0000",
            border_color0="#008F28")
    )
    candles.set_global_opts(
        title_opts=opts.TitleOpts(
            title="苹果-K线图",
            pos_top='top'),
        yaxis_opts=opts.AxisOpts
        (is_scale=True,
         splitline_opts=opts.SplitLineOpts(
             is_show=True,
             linestyle_opts=opts.LineStyleOpts(
                 width=1)),
         splitarea_opts=opts.SplitAreaOpts(
             is_show=True,
             areastyle_opts=opts.AreaStyleOpts(
                 opacity=1)),
         name="点位",
         name_location="middle",
         name_gap=40,
         name_textstyle_opts=opts.TextStyleOpts(
             font_size=15,
             font_weight="bold")
         ),
        xaxis_opts=opts.AxisOpts(
            name="日期",
            name_location="middle",
            name_gap=40,
            name_textstyle_opts=opts.TextStyleOpts(
                font_size=15,
                font_weight="bold")),
        legend_opts=opts.LegendOpts(
            is_show=True,
            pos_top=True,
            orient='vertical',
            textstyle_opts=opts.TextStyleOpts(
                font_size=10)),
        datazoom_opts=[opts.DataZoomOpts(
            xaxis_index=[1,0]
        )],
        toolbox_opts=opts.ToolboxOpts()
    )
    candles.set_series_opts()

    line = Line(init_opts=opts.InitOpts(
            width="1440px",
            height="720px")
    )
    line.add_xaxis(xaxis_data=dates)
    line.add_yaxis(
        series_name='fb',
        y_axis=aap_close,
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False)
    )

    line.set_global_opts(
        title_opts=opts.TitleOpts(
            title="FB走势",
            pos_top='48%',
        ),
        legend_opts=opts.LegendOpts(
            pos_bottom='200%,'
        ),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitline_opts=opts.SplitLineOpts(
                is_show=True,
                linestyle_opts=opts.LineStyleOpts(
                    width=1)),
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True,
                areastyle_opts=opts.AreaStyleOpts(
                    opacity=1)),
            name="点位",
            name_location="middle",
            name_gap=40,
            name_textstyle_opts=opts.TextStyleOpts(
                font_size=15,
                font_weight="bold")
                  ),
        xaxis_opts=opts.AxisOpts(
            name="日期",
            name_location="middle",
            name_gap=40,
            name_textstyle_opts=opts.TextStyleOpts(
                font_size=15,
                font_weight="bold")),
        datazoom_opts=[opts.DataZoomOpts()],
    )

    grid = Grid()
    grid.add(candles, grid_opts=opts.GridOpts(pos_bottom='60%'))
    grid.add(line, grid_opts=opts.GridOpts(pos_top='60%'))
    grid.render("grid.html")


if __name__ == '__main__':
    filename = "pycharts.csv"
    # KLine(filename)
    # demo()
    # office_demo()
    # maLine()
    rsiLine()
    # g = Grid()
    # g = grid_mutil_yaxis()
    # g.render('grid.html')
    # multi_y()
    # bar = barline()
    # bar.render("bar.html")
    # GridDemo()


