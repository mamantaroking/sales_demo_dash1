import dash
from dash import html, Dash, dcc, callback, Output, Input, State, ctx
import pandas as pd
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import json
import map_store
from datetime import date, datetime


# Define external stylesheets
external_stylesheets = ["https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&display=swap",
                        dbc.themes.LITERA]

# ------------------------------------------------- App Initialization -------------------------------------------------
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}

# dash.register_page(__name__, path='/')


df = pd.read_csv('datav4.csv')


limits = [(0, 100000), (100001, 250000), (250001, 500000), (500000, 1000000), (1000000, 10000000)]

fig = go.Figure()
fig2 = go.Figure()
# geojson = json.load(open('../malaysia_cloropeth_geojson.json'))

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
    size='sales_value',
    color='sales_value',
    hover_name='city',
    zoom=5,
    height=650,
    color_continuous_scale='Tealgrn',
    hover_data={
        # 'sales_value': lambda x: f'The Sales Value is {x:,}',
        'sales_value': True,
        'generic': True,
        'latitude': True,
        'longitude': True,
        'datetime': True,
    },
    # text='city'
    # mapbox_style='carto-positron'
    )  # animation_frame='datetime')
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
                    id='header-logo', src=r'../assets/dp_logo.png', alt='duopharma_logo', height='67px',
                    width='100px', className='center'
                ),
            ], href='https://duopharmabiotech.com/about-duopharma-biotech/', target="_blank", className='center',style={'width': '150px'}
            ),
        ], className='p-2', width={'order': 'first', 'size': 1}, sm=1
        ),
        dbc.Col(['Drug Sales Map'], className='mitr-bigger m-2', width=2, align='center', sm=2),

        # dbc.Col([
        #     dbc.Breadcrumb(items=[{'label': 'Drug Sales Map', 'active': True}], itemClassName='center mitr-bigger border py-2 px-3 shadow-sm breadcrumb_gradient rounded-3'),
        # ], className='mitr-bigger m-2', width=2, align='center', sm=2
        # ),
        # dbc.Col([
        #     dbc.Breadcrumb(items=[{'label': 'Sales Table', 'active': False, 'href': '/table'}], itemClassName='center mitr-bigger border py-2 px-3 shadow-sm breadcrumb_gradient rounded-3'),
        # ], className='mitr-bigger m-2', width=2, align='center', sm=2
        # ),

    ], className='border shadow dp_gradient', justify='start', align='center'
    ),

    dbc.Stack([

        html.Div([
            'City',
            dcc.Dropdown(
                df.city.sort_values().unique(), multi=False, className='p-2', id='dropdown-city', # style={'font-size': '11px'}
                # value='Johor'
            )
        ], className='px-2', id='space-dropdown-city', style={'width': '20%', 'font-size': '11'}
        ),

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
                # max_date_allowed=date(2024, 12, 6),
                # initial_visible_month=date(2023, 12, 6),
                # end_date=date(2024, 12, 6),
                className='p-2',
                id='date-picker',
                clearable=True,
                updatemode='bothdates'
                # style={'font-size': '11px'}
            ),
        ], className='px-2', style={'width': '30%', 'font-size': '11'}
        ),

        html.Div([
            'Change Plot',
            dbc.ButtonGroup([
                dbc.Button(['Sales Quantity'], id='cluster-btn', color='primary'),
                dbc.Button(['Scatter Details'], id='detail-btn', color='primary'),
            ], size='md'),
        ], className='px-2', id='space-btn', style={'width': '20%', 'font-size': '11'}
        ),

    ], direction='horizontal', gap=2, className='border p-2 m-2 rounded-3'
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig2, id='map-1')
        ], className='border p-2 rounded-3', sm=7),
        dbc.Col([
            dag.AgGrid(
                id='grid',
                rowData=df.to_dict("records"),
                # columnDefs=[{"field": i} for i in new_count_df.columns],
                columnDefs=[{"field": i} for i in df.columns    ],
                getRowStyle=getRowStyle,
                dashGridOptions={
                    'rowSelection': 'single',
                    'pagination': True,
                    'animateRows': True,
                    # "domLayout": "autoHeight",
                    "suppressColumnMoveAnimation": True,
                    "enableCellTextSelection": True,
                },
                # columnSize='responsiveSizeToFit',
                defaultColDef={"filter": True,
                               "sortable": True,
                               "floatingFilter": True,
                               "resizable": True
                               },
                style={'height': '550px'},
                # columnSize='sizeToFit'
                columnSize='autoSize',
                className='ag-theme-balham'
            )
        ], className='border p-2 rounded-3', style={'height': '550px'}, sm=5)
    ]),

    html.Div(['Disclaimer: This app is only for demonstration purposes. All the data are fake and randomly generated and does not contain any accurate nor sensitive information.'],
             className='text-danger border bg-light px-3')
], className='bg-white')


# --------------------------------------------------- App Callbacks ----------------------------------------------------


@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('dropdown-states', 'value'),
    Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date'),
    Input('dropdown-generic', 'value'),
    Input('cluster-btn', 'n_clicks'),
    Input('detail-btn', 'n_clicks'),
    prevent_initial_call=True
)
def state_start(states, start, end, product, click1, click2):
    df = pd.read_csv('datav4.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])

    # When choosing states as the first dropdown arguement
    if states is not None:
        df = df[df['admin_name'] == states]
        fig3 = map_store.update_graph(df)

        # When choosing product as the second
        if product is not None:
            df = df[df['generic'] == product]
            # print(df['generic'])
            fig3 = map_store.update_graph(df)

            # When choosing dates as the third
            if start and end is not None:
                fig3 = map_store.check_time(start, end, df)

                # if the button is pressed
                if 'cluster-btn' == ctx.triggered_id:
                    fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                       visible=True,
                                       marker_size=df['sales_value'])
                    return fig3
                # If button is not pressed or detail button is triggered
                elif 'cluster-btn' == ctx.triggered_id:
                    return fig3
                else:
                    return fig3

            if 'cluster-btn' == ctx.triggered_id:
                fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                   visible=True,
                                   marker_size=df['sales_value'])
                return fig3

            # If button is not pressed or detail button is triggered
            elif 'cluster-btn' == ctx.triggered_id:
                return fig3
            else:
                return fig3

        # When choosing dates as the second
        elif start and end is not None:
            fig3 = map_store.check_time(start, end, df)

            # If button is pressed
            if 'cluster-btn' == ctx.triggered_id:
                fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                   visible=True,
                                   marker_size=df['sales_value'])
                return fig3

            # If button is not pressed or detail button is triggered
            elif 'cluster-btn' == ctx.triggered_id:
                return fig3
            else:
                return fig3

        # When button is clicked second after choosing states
        if 'cluster-btn' == ctx.triggered_id:
            fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                               visible=True,
                               marker_size=df['sales_value'])
            return fig3

            # If button is not pressed or detail button is triggered
        elif 'cluster-btn' == ctx.triggered_id:
            return fig3
        else:
            return fig3

    # When choosing product as the first dropdown
    elif product is not None:
        df = df[df['generic'] == product]
        # print(df['generic'])
        fig3 = map_store.update_graph(df)

        if 'cluster-btn' == ctx.triggered_id:
            fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                               visible=True,
                               marker_size=df['sales_value'])
            return fig3

        # When choosing states as the second
        if states is not None:
            df = df[df['admin_name'] == states]
            fig3 = map_store.update_graph(df)

            if 'cluster-btn' == ctx.triggered_id:
                fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                   visible=True,
                                   marker_size=df['sales_value'])
                return fig3

            # When choosing dates as the third
            if start and end is not None:
                fig3 = map_store.check_time(start, end, df)

                # If button is pressed
                if 'cluster-btn' == ctx.triggered_id:
                    fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                       visible=True,
                                       marker_size=df['sales_value'])
                    return fig3

                # If button is not pressed or detail button is triggered
                elif 'cluster-btn' == ctx.triggered_id:
                    return fig3
                else:
                    return fig3

            # Return chosen dates
            else:
                return fig3

        # When choosing dates as the second
        elif start and end is not None:
            fig3 = map_store.check_time(start, end, df)

            # If button is pressed
            if 'cluster-btn' == ctx.triggered_id:
                fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                                   visible=True,
                                   marker_size=df['sales_value'])
                return fig3

            # If button is not pressed or detail button is triggered
            elif 'cluster-btn' == ctx.triggered_id:
                return fig3
            else:
                return fig3

        # Return chosen dates
        else:
            return fig3

    # When date is the only one chosen
    elif start and end is not None:
        fig3 = map_store.check_time(start, end, df)

        if 'cluster-btn' == ctx.triggered_id:
            fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1),
                               visible=True,
                               marker_size=df['sales_value'])
            return fig3
            # If button is not pressed or detail button is triggered
        elif 'cluster-btn' == ctx.triggered_id:
            return fig3
        else:
            return fig3

    # If button is pressed first
    elif 'cluster-btn' == ctx.triggered_id:
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='generic', zoom=4.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3

    elif 'cluster-btn' == ctx.triggered_id:
        fig2 = map_store.update_graph(df)
        return fig2

    # When everything is cleared
    else:
        fig2 = map_store.update_graph(df)
        return fig2


'''@callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('cluster-btn', 'n_clicks'),
    prevent_initial_call=True
)
def cluster_plot(click):
    if 'cluster-btn' == ctx.triggered_id:
        fig3 = px.scatter_map(df, lat="latitude", lon="longitude", size="sales_value", color='sales_value',
                              hover_name='generic', zoom=4.5, height=650, color_continuous_scale='Tealgrn')
        fig3.update_traces(cluster=dict(enabled=True, color='mediumaquamarine', size=20, step=1), visible=True,
                           marker_size=df['sales_value'])
        return fig3'''


@app.callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('grid', 'selectedRows'),
    prevent_initial_call=True
)
def click_on_grid(selected_rows):
    df = pd.read_csv('datav4.csv')
    if not selected_rows:
        return dash.no_update
    row = [s['id'] for s in selected_rows]
    df = df[df.id.isin(row)]
    fig3 = map_store.update_graph(df)
    print(row)
    return fig3



if __name__ == '__main__':
    app.run(debug=True, port=8051)
