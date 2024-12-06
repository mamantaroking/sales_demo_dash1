import dash
from dash import html, Dash, dcc, callback, Output, Input, State
import pandas as pd
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import json
import map_store
from datetime import date, datetime


app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
server = app.server


df = pd.read_csv('datav3.csv')


limits = [(0, 100000), (100001, 250000), (250001, 500000), (500000, 1000000), (1000000, 10000000)]

fig = go.Figure()
fig2 = go.Figure()
geojson = json.load(open('malaysia_cloropeth_geojson.json'))

bins = [0, 100000, 250000, 500000, 1000000, 10000000]
labels = ['0 - 100000', '100000 - 250000', '250000 - 500000', '500000 - 1000000', '1000000 - 10000000']


# df['scale'] = pd.cut(df['population'], bins=bins, labels=labels, right=False)


'''fig = px.scatter_geo(
    df,
    # locations='city',
    size='population',
    color='population_proper',
    lon='lng',
    lat='lat',
    text='city'
    # geojson=geojson,
    # featureidkey="properties.name"
)
fig.update_traces(marker_size=df['population']*2)
fig.update_geos(fitbounds='locations', visible=True, showframe=True,
                showcoastlines=False, resolution=50, bgcolor='lightsteelblue',
                lonaxis_showgrid=True, lataxis_showgrid=True)'''
# fig.show()


fig2 = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    size=df['sales_value']*10,
    color='sales_value',
    hover_name='city',
    zoom=5,
    height=650,
    color_continuous_scale='Tealgrn',
    hover_data={
        'sales_value': lambda x: f'The Sales Value is {x:,}',
        'generic': True,
        'latitude': True,
        'longitude': True,
        'datetime': True,
},
    # text='city'
    # mapbox_style='carto-positron'
) # animation_frame='datetime')
fig2.update_traces(
    cluster=dict(
        enabled=False,
        color='lightcoral',
        # size=[20, 30, 40, 50],
        size=[50, 40, 30, 20],
        step=[-1, 10, 20, 30],
        # step=[50, 40, 30, 20],
        # step=10
    ),
    visible=True,
    # marker_size=df['sales_value'],
    marker_sizemode='area'
)


# df_johor = df[df['admin_name'] == 'Johor']
# print(df_johor)


app.layout = html.Div([
    dbc.Row([

        dbc.Col([
            html.A([
                html.Img(
                    id='header-logo', src=r'assets/dp_logo.png', alt='duopharma_logo', height='67px',
                    width='100px', className='center'
                ),
            ], href='https://duopharmabiotech.com/about-duopharma-biotech/', target="_blank", className='center',style={'width': '150px'}
            ),
        ], className='p-2', width={'order': 'first', 'size': 1}, sm=1
        ),

        dbc.Col([
            'Drug Sales Map'
        ], className='mitr-bigger ms-2', width=2, align='center', sm=1
        ),

    ], className='border shadow dp_gradient', justify='start'
    ),

    dbc.Stack([

        html.Div([
            'State',
            dcc.Dropdown(
                df.admin_name.sort_values().unique(), multi=False, className='p-2', id='dropdown-states', # style={'font-size': '11px'}
                # value='Johor'
            )
        ], className='px-2', id='space-dropdown-states', style={'width': '20%', 'font-size': '11'}
        ),

        # html.Div([
        #     'Date Range',
        #     dcc.Dropdown([
        #         'December 2023', 'January 2024', 'February 2024', 'March 2024', 'April 2024', 'May 2024', 'June 2024',
        #         'July 2024', 'August 2024', 'September 2024', 'October 2024', 'November 2024', 'December 2024'
        #     ], multi=False, className='p-2', id='dropdown-date', # style={'font-size': '11px'}
        #     )
        # ], className='p-2', style={'width': '20%', 'font-size': '11'}
        # ),

        # html.Div([
        #     'Brand',
        #     dcc.Dropdown(
        #         options=df.brand.sort_values().unique(), multi=False, className='p-2,', style={'font-size': '11px'}
        #     )
        # ], className='p-2', id='space-dropdown-brand', style={'width': '30%', 'font-size': '11'}
        # ),

        html.Div([
            'Product Name',
            dcc.Dropdown(
                options=df.generic.sort_values().unique(), multi=False, className='p-2', id='dropdown-generic' # style={'font-size': '11px'}, optionHeight=70
            )
        ], className='px-2', id='space-dropdown-generic', style={'width': '20%', 'font-size': '11'}
        ),

        html.Div([
            'Date Range',
            dcc.DatePickerRange(
                min_date_allowed=date(2023, 12, 1),
                max_date_allowed=date(2024, 12, 6),
                initial_visible_month=date(2023, 12, 6),
                # end_date=date(2024, 12, 6),
                className='p-2',
                id='date-picker',
                clearable=True,
                updatemode='bothdates'
                # style={'font-size': '11px'}
            ),
        ], className='px-2', style={'width': '30%', 'font-size': '11'}
        ),

    ], direction='horizontal', gap=2, className='border p-2 m-2 rounded-3'
    ),

    html.Div(
        [
            # dbc.Col([dcc.Graph(figure=fig)]),
            dbc.Col([dcc.Graph(figure=fig2, id='map-1')])
        ], className='border p-2 m-2 rounded-3'
    ),
    html.Div(['*This app is only for demonstration purposes. All the data are fake and randomly generated (with the exception of Duopharma Products) and does not contain any accurate nor sensitive information.'],
             className='text-danger border bg-light px-3')
])


# --------------------------------------------------- App Callbacks ----------------------------------------------------

'''
@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('dropdown-states', 'value'),
    prevent_initial_call=True
)
def update_map(value):
    df = pd.read_csv('datav3.csv')
    if value == 'Johor':
        df3 = df[df['admin_name'] == 'Johor']
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Kedah':
        df3 = df[df['admin_name'] == 'Kedah']
        print(df3)
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Kelantan':
        df3 = df[df['admin_name'] == 'Kelantan']
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Labuan':
        df3 = df[df['admin_name'] == 'Labuan']
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Kuala Lumpur':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Melaka':
        df3 = df[df['admin_name'] == 'Melaka']
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Negeri Sembilan':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Pahang':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Perak':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Perlis':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Pulau Pinang':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650,  color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Putrajaya':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650,  color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Sabah':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650,  color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Sarawak':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650,  color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Selangor':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650,  color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3
    elif value == 'Terengganu':
        df3 = df[df['admin_name'] == value]
        fig3 = px.scatter_map(df3, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=7.5, height=650, color_continuous_scale='Tealgrn' )
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig3

    else:
        fig2 = px.scatter_map(df, lat="latitude", lon="longitude", size='sales_value', color='sales_value', hover_name='city', zoom=4.5, height=650,  color_continuous_scale='Tealgrn')
        fig2.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['sales_value'])
        return fig2


@callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('date-picker', 'start_date'),
    State('date-picker', 'end_date'),
    prevent_initial_call=True
)
def update_output(start_date, end_date):
    df = pd.read_csv('datav3.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])
    if start_date and end_date is not None:
        datetime.strptime(start_date, '%Y-%m-%d')
        print(start_date, type(start_date))
        datetime.strptime(end_date, '%Y-%m-%d')
        df2 = df[(df['datetime'] > start_date) & (df['datetime'] < end_date)]
        # df[df['datetime'] > start_date]
        # df[df['datetime'] < end_date]
        # print(df['datetime'])
        fig3 = px.scatter_map(df2, lat="latitude", lon="longitude", size="sales_value", color='sales_value', hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df2['sales_value'])
        return fig3
    else:
        fig2 = px.scatter_map(df, lat="latitude", lon="longitude", size='sales_value', color='sales_value',
                              hover_name='city', zoom=5, height=650, color_continuous_scale='Tealgrn')
        fig2.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig2
        '''


@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('dropdown-generic', 'value'),
    prevent_initial_call=True
)
def start_product(value):
    df = pd.read_csv('datav3.csv')
    if value is not None:
        df = df[df['generic'] == value]
        # print(df['generic'])
        fig3 = map_store.update_graph(df)
        print('value is available')
        return fig3
    else:
        print('value is None')
        fig2 = map_store.update_graph(df)
        return fig2

@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date'),
    prevent_initial_call=True
)
def date_start(start, end):
    df = pd.read_csv('datav3.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])
    if start and end is not None:
        fig3 = map_store.check_time(start, end, df)
        return fig3
    else:
        fig2 = map_store.update_graph(df)
        return fig2


@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('dropdown-states', 'value'),
    State('date-picker', 'start_date'),
    State('date-picker', 'end_date'),
    State('dropdown-generic', 'value'),
    prevent_initial_call=True
)
def state_start(states, start, end, product):
    df = pd.read_csv('datav3.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])

    if states is not None:
        df = df[df['admin_name'] == states]
        fig3 = map_store.update_graph(df)

        if product is not None:
            df = df[df['generic'] == product]
            print(df['generic'])
            fig3 = map_store.update_graph(df)

            if start and end is not None:
                fig3 = map_store.check_time(start, end, df)
                return fig3
            else:
                return fig3

        elif start and end is not None:
            fig3 = map_store.check_time(start, end, df)
            return fig3
        else:
            return fig3

    else:
        fig2 = map_store.update_graph(df)
        return fig2





if __name__ == '__main__':
    app.run(debug=True, port=8051)
