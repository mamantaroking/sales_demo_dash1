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
import requests
import re
import io
import json
import os


# Define external stylesheets
external_stylesheets = ["https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&display=swap",
                        dbc.themes.LITERA]

# ------------------------------------------------- App Initialization -------------------------------------------------
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
dash.register_page(__name__, path='/geocode_2')

getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}


def get_url(addressLine):
    api_key = '6756a4f537df1888365864rti94069d'
    base_url = 'https://geocode.maps.co/search'
    url = f'{base_url}?q={addressLine}&api_key={api_key}'
    return url


id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
party = ['Guardian Pharmacy', 'Caring Pharmacy', 'Watsons', 'Sherlocks', 'Farmasi Unik', 'UnI Pharmacy', 'Klinik Mediviron', 'Worldwide Clinic', 'Cake Hospital', 'West Point Hospital', 'Cube Clinic', 'Colts Pharmacy']
sales = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
units = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
address = ['123 Jalan Ampang', '456 Jalan Bukit Bintang', 'SS15', '123 Jalan Sultan Zainal Abidin', '456 Jalan Miri-Bintulu', '12 Jalan Hang Tuah', '45 Jalan Tengkera', '789 Jalan Meru', '12 Jalan Gaya', '45 Jalan Tanjung Aru', 'Jalan Kuala Perlis', 'Jalan Barrack']
postcode = ['50450', '55100', '47500', '20000', '98000', '75300', '75200', '41050', '88000', '88100', '02100', '02000']
city = ['Kuala Lumpur', 'Kuala Lumpur', 'Subang Jaya', 'Kuala Terengganu', 'Miri', 'Bandar Melaka', 'Bandar Melaka', 'Klang', 'Kota Kinabalu', 'Kota Kinabalu', 'Kuala Perlis', 'Kangar']
state = ['Kuala Lumpur', 'Kuala Lumpur', 'Selangor', 'Terengganu', 'Sarawak', 'Melaka', 'Melaka', 'Selangor', 'Sabah', 'Sabah', 'Perlis', 'Perlis']
country = ['MY', 'MY', 'MY', 'MY', 'MY', 'Malaysia', 'Malaysia', 'MY', 'MY', 'MY', 'MY', 'MY']

dict = {'id': id, 'party': party, 'sales': sales, 'units': units, 'address': address, 'postcode': postcode, 'city': city, 'state': state, 'country': country}


df = pd.DataFrame(dict)
df['full_address'] = df.apply(lambda row: f"{row['address']} {row['postcode']} {row['city']} {row['state']} {row['country']}", axis=1)
df['full_address'] = df['full_address'].replace([r' '], '+', regex=True)
df['url'] = df['full_address'].apply(get_url)
df.to_csv('sample_url.csv')


def geocode(url):
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        result = r.json()
        if result:
            return result[0]['lat'], result[0]['lon']
    return None, None

df[['latitude', 'longitude']] = df['url'].apply(lambda x: pd.Series(geocode(x)))
df[['latitude', 'longitude']] = df[['latitude', 'longitude']].astype(float)

df.to_csv('geocoded.csv')
print(df.info())


fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='party', zoom=4.5, height=650, size='sales', color='units', color_continuous_scale='Tealgrn',
                     hover_data={
                         'sales': True,
                         'units': True,
                         'city': True,
                         'state': True,
                         'latitude': True,
                         'longitude': True,
                         'country': True,
                     },
                     )
# fig.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
#                        marker_size=df['sales_value'])


layout = html.Div([
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
        # dbc.Col(['Geocoded Maps'], className='mitr-bigger m-2', width=2, align='center', sm=2),
        dbc.Col([
            dbc.Breadcrumb(items=[{'label': 'Drug Sales Map', 'active': False, 'href': '/'}],
                           itemClassName='center mitr-bigger py-2 px-3'),
        ], className='mitr-bigger m-2', width=2, align='center', sm=2
        ),
        dbc.Col([
            dbc.Breadcrumb(items=[{'label': 'Geocoded Map', 'active': True}],
                           itemClassName='center mitr-bigger py-2 px-3'),
        ], className='mitr-bigger m-2', width=2, align='center', sm=2
        ),
    ], className='border shadow dp_gradient', justify='start', align='center'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig, id='map-2')
        ], className='border p-2 rounded-3', sm=7),
        dbc.Col([
            dag.AgGrid(
                id='grid-2',
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
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


@callback(
    Output('map-2', 'figure', allow_duplicate=True),
    Input('grid-2', 'selectedRows'),
    prevent_initial_call=True
)
def click_on_grid(selected_rows):
    df = pd.read_csv('geocoded.csv')
    if not selected_rows:
        fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='party', zoom=4.5, height=650, size_max=30,
                             size='sales',
                             color='units', color_continuous_scale='Tealgrn',
                             hover_data={
                                 'sales': True,
                                 'units': True,
                                 'city': True,
                                 'state': True,
                                 'latitude': True,
                                 'longitude': True,
                                 'country': True,
                             },
                             )
        return fig
    row = [s['id'] for s in selected_rows]
    df = df[df.id.isin(row)]
    fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='party', zoom=8, size_max=30, height=650, size='sales',
                         color='units', color_continuous_scale='Tealgrn',
                         hover_data={
                             'sales': True,
                             'units': True,
                             'city': True,
                             'state': True,
                             'latitude': True,
                             'longitude': True,
                             'country': True,
                         },
                         )

    print(row)
    return fig


'''if __name__ == '__main__':
    app.run(debug=True, port=8052)'''
