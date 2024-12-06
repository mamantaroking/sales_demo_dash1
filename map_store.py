import plotly.express as px
import pandas as pd

def update_product(value, df):
    if value == 'Unihep':
        df = df[df['generic'] == 'Unihep']
        # print(df['generic'])
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Ranofer':
        df = df[df['generic'] == 'Ranofer']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Erysaa':
        df = df[df['generic'] == 'Erysaa']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Bi-Haemosol':
        df = df[df['generic'] == 'Bi-Haemosol']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Haemosol':
        df = df[df['generic'] == 'Haemosol']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Kytron':
        df = df[df['generic'] == 'Kytron']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Zuhera':
        df = df[df['generic'] == 'Zuhera']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Lebreta':
        df = df[df['generic'] == 'Lebreta']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Trevive':
        df = df[df['generic'] == 'Trevive']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Krabeva':
        df = df[df['generic'] == 'Krabeva']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen-R':
        df = df[df['generic'] == 'Insugen-R']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen-N':
        df = df[df['generic'] == 'Insugen-N']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen 30/70':
        df = df[df['generic'] == 'Insugen 30/70']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Basalog':
        df = df[df['generic'] == 'Basalog']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Basalog One':
        df = df[df['generic'] == 'Erysaa']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Kirsty':
        df = df[df['generic'] == 'Kirsty']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    else:
        fig2 = px.scatter_map(df, lat="latitude", lon="longitude", size='sales_value', color='sales_value',
                              hover_name='city', zoom=4.5, height=650, color_continuous_scale='Tealgrn')
        fig2.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig2


def johor_and_products(value, df):
    if value == 'Unihep':
        df = df[df['generic'] == 'Unihep']
        # print(df['generic'])
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Ranofer':
        df = df[df['generic'] == 'Ranofer']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Erysaa':
        df = df[df['generic'] == 'Erysaa']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Bi-Haemosol':
        df = df[df['generic'] == 'Bi-Haemosol']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Haemosol':
        df = df[df['generic'] == 'Haemosol']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Kytron':
        df = df[df['generic'] == 'Kytron']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Zuhera':
        df = df[df['generic'] == 'Zuhera']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Lebreta':
        df = df[df['generic'] == 'Lebreta']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Trevive':
        df = df[df['generic'] == 'Trevive']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Krabeva':
        df = df[df['generic'] == 'Krabeva']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen-R':
        df = df[df['generic'] == 'Insugen-R']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen-N':
        df = df[df['generic'] == 'Insugen-N']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Insugen 30/70':
        df = df[df['generic'] == 'Insugen 30/70']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Basalog':
        df = df[df['generic'] == 'Basalog']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Basalog One':
        df = df[df['generic'] == 'Erysaa']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    elif value == 'Kirsty':
        df = df[df['generic'] == 'Kirsty']
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3
    else:
        fig2 = px.scatter_map(df, lat="latitude", lon="longitude", size='sales_value', color='sales_value',
                              hover_name='city', zoom=4.5, height=650, color_continuous_scale='Tealgrn')
        fig2.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig2
