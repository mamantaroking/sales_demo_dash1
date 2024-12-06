import plotly.express as px
import pandas as pd
from datetime import date, datetime

def update_graph(df):
    fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                          hover_name='generic', zoom=4.5, height=650, color_continuous_scale='Tealgrn')
    fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                       marker_size=df['sales_value'])
    return fig3

def check_time(start, end, df):
    datetime.strptime(start, '%Y-%m-%d')
    # print(start, type(start))
    datetime.strptime(start, '%Y-%m-%d')
    df2 = df[(df['datetime'] > start) & (df['datetime'] < end)]
    fig3 = update_graph(df2)
    return fig3