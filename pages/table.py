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


dash.register_page(__name__, path='/table')


getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}


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


layout = html.Div([
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

        dbc.Col([
            dbc.Breadcrumb(items=[{'label': 'Drug Sales Map', 'active': False, 'href': '/'}], itemClassName='center mitr-bigger border py-2 px-3 shadow-sm breadcrumb_gradient rounded-3'),
        ], className='mitr-bigger m-2', width=2, align='center', sm=2
        ),
        dbc.Col([
            dbc.Breadcrumb(items=[{'label': 'Sales Table', 'active': True}], itemClassName='center mitr-bigger border py-2 px-3 shadow-sm breadcrumb_gradient rounded-3'),
        ], className='mitr-bigger m-2', width=2, align='center', sm=2
        ),

    ], className='border shadow dp_gradient', justify='start', align='center'
    ),


    html.Div(
        [
            # dbc.Col([dcc.Graph(figure=fig)]),
            dag.AgGrid(
                rowData=df.to_dict("records"),
                # columnDefs=[{"field": i} for i in new_count_df.columns],
                columnDefs=[{"field": i} for i in df.columns],
                getRowStyle=getRowStyle,
                dashGridOptions={
                    'rowSelection': 'single',
                    'pagination': True,
                    'animateRows': True,
                    # "domLayout": "autoHeight",
                    "suppressColumnMoveAnimation": True,
                    "enableCellTextSelection": True
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
                # exportDataAsCsv=True,
            )
        ], className='border p-3 m-3 rounded-3', style={'height': '600px'}
    ),
    html.Div(['Disclaimer: This app is only for demonstration purposes. All the data are fake and randomly generated and does not contain any accurate nor sensitive information.'],
             className='text-danger border bg-light px-3')
], className='bg-white')


# --------------------------------------------------- App Callbacks ----------------------------------------------------


'''@callback(
    Output('map-1', 'figure', allow_duplicate=True),
    Input('dropdown-states', 'value'),
    Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date'),
    Input('dropdown-generic', 'value'),
    prevent_initial_call=True
)
def state_start(states, start, end, product):
    df = pd.read_csv('../datav4.csv')
    df['datetime'] = pd.to_datetime(df['datetime'])

    if states is not None:
        df = df[df['admin_name'] == states]
        fig3 = map_store.update_graph(df)

        if product is not None:
            df = df[df['generic'] == product]
            # print(df['generic'])
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

    elif product is not None:
        df = df[df['generic'] == product]
        # print(df['generic'])
        fig3 = map_store.update_graph(df)

        if states is not None:
            df = df[df['admin_name'] == states]
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

    elif start and end is not None:
        fig3 = map_store.check_time(start, end, df)
        return fig3

    else:
        fig2 = map_store.update_graph(df)
        return fig2'''

'''if __name__ == '__main__':
    app.run(debug=True, port=8052)'''
