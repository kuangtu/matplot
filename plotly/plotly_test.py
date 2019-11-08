# -*- coding: UTF-8 -*-
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go


def plot_bar():
    data = np.array([1,2,3,4])
    ticker = ['2000', '2001', '2002', '2003']
    df = pd.DataFrame(data, index=ticker, columns=['seq'])
    df['name'] = ticker
    fig = px.bar(df, x='name', y='seq')
    fig.show()

def plot_bar_group():
    '''
    绘制group bar
    :return:
    '''
    animals = ['giraffes', 'orangutans', 'monkeys']

    fig = go.Figure(data=[
        go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
        go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.show()

if __name__ == '__main__':
    # plot_bar()
    plot_bar_group()

