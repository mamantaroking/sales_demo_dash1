from dash import Dash, Input, Output, State, dash_table, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
import dash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psycopg2

conn = psycopg2.connect(
    dbname='dash_databse_postgres',
    user='dash_databse_postgres_user',
    password='7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z',
    host='dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com',
    port='5432',
)

query = 'SELECT * FROM bpom WHERE date_of_issuance > '
df = pd.read_sql_table('bpom', 'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')

app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])


app.layout = html.Div([
    html.Div([
        dcc.Dropdown([
            {'label': "Malaysia's NPRA", 'value': 'npra'},
            {'label': "Indonesia's BPOM", 'value': 'bpom'},
            {'label': "Philippine's FDA", 'value': 'ph_fda'},
            {'label': "Singapore's HSA", 'value': 'hsa'},
        ], placeholder='Choose Regulatory Administration...', id='dropdown-menu'),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(
                    "Malaysia's NPRA", id="dropdown-npra", n_clicks=0
                ),
                dbc.DropdownMenuItem(
                    "Indonesia' BPOM", id="dropdown-bpom", n_clicks=0
                ),
                dbc.DropdownMenuItem(
                    "Singapore's HSA", id="dropdown-hsa", n_clicks=0
                ),
                dbc.DropdownMenuItem(
                    "Philippine's FDA", id="dropdown-ph_fda", n_clicks=0
                ),
            ],
            label="Choose a Regulatory Administration...", className='m-2 d-flex justify-content-center', id='dropdown-dbc'
        ),
        html.Hr(),
        html.Div(id='place-container'),
    ])
])


@app.callback(
    Output('place-container', 'children', allow_duplicate=True),
    Input('dropdown-menu', 'value'), prevent_initial_call=True
)
def update_table(value):
    query = f'SELECT * FROM {value}'
    df = pd.read_sql_table(value,'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')
    grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            # columnDefs=columnDefs,
            dashGridOptions={
                'rowSelection': 'single',
                'pagination': True,
                'animateRows': False,
            },
            # columnSize='responsiveSizeToFit',
            defaultColDef={"filter": True,
                           "sortable": True,
                           "floatingFilter": True,
                           },
            # exportDataAsCsv=True,
        ),
    return grid


@app.callback(
    Output('place-container', 'children', allow_duplicate=True),
    Output('dropdown-dbc', 'label', allow_duplicate=True),
    Input('dropdown-npra', 'n_clicks'), prevent_initial_call=True
)
def update_table_npra(click):
    if click > 0:
        value = 'npra'
        labelling = "Malaysia's NPRA"
        df = pd.read_sql_table(value,'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')
        grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            # columnDefs=columnDefs,
            dashGridOptions={
                'rowSelection': 'single',
                'pagination': True,
                'animateRows': False,
            },
            # columnSize='responsiveSizeToFit',
            defaultColDef={"filter": True,
                           "sortable": True,
                           "floatingFilter": True,
                           },
            # exportDataAsCsv=True,
        ),
        return grid, labelling


@app.callback(
    Output('place-container', 'children', allow_duplicate=True),
    Output('dropdown-dbc', 'label', allow_duplicate=True),
    Input('dropdown-bpom', 'n_clicks'), prevent_initial_call=True
)
def update_table_bpom(click):
    if click > 0:
        value = 'bpom'
        labelling = "Indonesia's BPOM"
        df = pd.read_sql_table(value,'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')
        grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            # columnDefs=columnDefs,
            dashGridOptions={
                'rowSelection': 'single',
                'pagination': True,
                'animateRows': False,
            },
            # columnSize='responsiveSizeToFit',
            defaultColDef={"filter": True,
                           "sortable": True,
                           "floatingFilter": True,
                           },
            # exportDataAsCsv=True,
        ),
        return grid, labelling


@app.callback(
    Output('place-container', 'children', allow_duplicate=True),
    Output('dropdown-dbc', 'label', allow_duplicate=True),
    Input('dropdown-hsa', 'n_clicks'), prevent_initial_call=True
)
def update_table_hsa(click):
    if click > 0:
        value = 'hsa'
        labelling = "Singapore's HSA"
        df = pd.read_sql_table(value,'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')
        grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            # columnDefs=columnDefs,
            dashGridOptions={
                'rowSelection': 'single',
                'pagination': True,
                'animateRows': False,
            },
            # columnSize='responsiveSizeToFit',
            defaultColDef={"filter": True,
                           "sortable": True,
                           "floatingFilter": True,
                           },
            # exportDataAsCsv=True,
        ),
        return grid, labelling


@app.callback(
    Output('place-container', 'children', allow_duplicate=True),
    Output('dropdown-dbc', 'label', allow_duplicate=True),
    Input('dropdown-ph_fda', 'n_clicks'), prevent_initial_call=True
)
def update_table_ph_fda(click):
    if click > 0:
        value = 'ph_fda'
        labelling = "Philippine's FDA"
        df = pd.read_sql_table(value,'postgresql://dash_databse_postgres_user:7X5Eph0X3oacGqOe7LWfie7xcFM8i44Z@dpg-csun4et6l47c73fvcj1g-a.singapore-postgres.render.com/dash_databse_postgres')
        grid = dag.AgGrid(
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            # columnDefs=columnDefs,
            dashGridOptions={
                'rowSelection': 'single',
                'pagination': True,
                'animateRows': False,
            },
            # columnSize='responsiveSizeToFit',
            defaultColDef={"filter": True,
                           "sortable": True,
                           "floatingFilter": True,
                           },
            # exportDataAsCsv=True,
        ),
        return grid, labelling


if __name__ == '__main__':
    app.run(debug=True, port=8016)

