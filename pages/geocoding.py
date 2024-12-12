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
import numpy as np


# Define external stylesheets
external_stylesheets = ["https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&display=swap",
                        dbc.themes.LITERA]

# ------------------------------------------------- App Initialization -------------------------------------------------
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
dash.register_page(__name__, path='/geocode')

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


# df = pd.read_csv('not real data.csv')
df = pd.read_csv('sample_data.csv')
df_l = pd.DataFrame()
df = df[df['Billing Type'] == 'ZF2']
df = df.fillna('')
df['full_address'] = df.apply(lambda row: f"{row['DO ShipTo Street']} {row['DO ShipTo Street 4']} {row['DO ShipTo Street 5']} {row['DO ShipTo City']} {row['DO ShipTo PostCode']} {row['DO ShipTo State']} {row['DO ShipTo State']} {row['DO ShipTo Ctry']}", axis=1)
df_l['full_address'] = df['full_address'].replace([r' '], '+', regex=True)
# print(df_l.info())
df_l['url'] = df_l['full_address'].apply(get_url)
df_l.to_csv('df_l.csv')
# print(df_l.head())


def geocode(url):
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        result = r.json()
        if result:
            return result[0]['lat'], result[0]['lon']
    return None, None


df[['latitude', 'longitude']] = df_l['url'].apply(lambda x: pd.Series(geocode(x)))
df[['latitude', 'longitude']] = df[['latitude', 'longitude']].astype(float)
df[['Local Net Value', 'CCM Billed Quantity']] = df[['Local Net Value', 'CCM Billed Quantity']].replace([r','], '', regex=True)
df[['Local Net Value', 'CCM Billed Quantity']] = df[['Local Net Value', 'CCM Billed Quantity']].astype(float)
df.insert(0, 'id', range(0, 0 + len(df)))

df.to_csv('geocoded.csv')
print(df.info())

fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='Ship To Party Name', zoom=4, height=650,
                     size='Local Net Value', color='CCM Billed Quantity', color_continuous_scale='Tealgrn', size_max=30,
                     hover_data={
                         "Doctor's Name": True,
                         "Material Group Desc.": True,
                         'Local Net Value': True,
                         'Ship To Party Name': True,
                         'DO ShipTo City': True,
                         'DO ShipTo State': True,
                         'DO ShipTo PostCode': True,
                         'latitude': True,
                         'longitude': True,
                         'DO ShipTo Ctry': True,
                     },
                     )
# fig.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True,
#                        marker_size=df['sales_value'])


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
        fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='Ship To Party Name', zoom=4, height=650,
                             size='Local Net Value', color='CCM Billed Quantity', color_continuous_scale='Tealgrn', size_max=30,
                             hover_data={
                                 "Doctor's Name": True,
                                 "Material Group Desc.": True,
                                 'Local Net Value': True,
                                 'Ship To Party Name': True,
                                 'DO ShipTo City': True,
                                 'DO ShipTo State': True,
                                 'DO ShipTo PostCode': True,
                                 'latitude': True,
                                 'longitude': True,
                                 'DO ShipTo Ctry': True,
                             },
                             )
        return fig
    row = [s['id'] for s in selected_rows]
    df = df[df.id.isin(row)]
    fig = px.scatter_map(df, lat="latitude", lon="longitude", hover_name='Ship To Party Name', zoom=12, height=650,
                         size='Local Net Value', color='CCM Billed Quantity', color_continuous_scale='Tealgrn', size_max=30,
                         hover_data={
                             "Doctor's Name": True,
                             "Material Group Desc.": True,
                             'Local Net Value': True,
                             'Ship To Party Name': True,
                             'DO ShipTo City': True,
                             'DO ShipTo State': True,
                             'DO ShipTo PostCode': True,
                             'latitude': True,
                             'longitude': True,
                             'DO ShipTo Ctry': True,
                         },
                         )

    print(row)
    return fig


'''if __name__ == '__main__':
    app.run(debug=True, port=8052)'''
