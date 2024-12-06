import dash
from dash import html, Dash, dcc, callback, Output, Input
import pandas as pd
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import json


app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])


df = pd.read_csv('my.csv')
limits = [(0, 100000), (100001, 250000), (250001, 500000), (500000, 1000000), (1000000, 10000000)]

fig = go.Figure()
fig2 = go.Figure()
geojson = json.load(open('malaysia_cloropeth_geojson.json'))

bins = [0, 100000, 250000, 500000, 1000000, 10000000]
labels = ['0 - 100000', '100000 - 250000', '250000 - 500000', '500000 - 1000000', '1000000 - 10000000']

df['scale'] = pd.cut(df['population'], bins=bins, labels=labels, right=False)

fig = px.scatter_geo(
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
                lonaxis_showgrid=True, lataxis_showgrid=True)
# fig.show()


fig2 = px.scatter_map(df, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city',zoom=5, height=700)
fig2.update_traces(
    cluster=dict(
        enabled=False,
        color='lightcoral',
        size=20,
        step=1
    ),
    visible=True,
    marker_size=df['population_proper']*2
)


# df_johor = df[df['admin_name'] == 'Johor']
# print(df_johor)


app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.Div([
                'State',
                dcc.Dropdown([
                    'Johor', 'Kedah', 'Kelantan', 'Labuan', 'Kuala Lumpur', 'Malacca', 'Negeri Sembilan', 'Pahang', 'Perak', 'Perlis',
                    'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'
                ], multi=False, className='p-2', id='dropdown-states', # value='Johor'
                )
            ], className='p-2', id='space-dropdown-states'
            ),
        ], style={'width': '20%'}, className='border', md=2
        ),

        dbc.Col([
            html.Div([
                'City',
                dcc.Dropdown([
                    'Johor', 'Kedah', 'Kelantan', 'Labuan', 'Kuala Lumpur', 'Malacca', 'Negeri Sembilan', 'Pahang',
                    'Perak', 'Perlis', 'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'
                ], multi=True, className='p-2'
                )
            ], className='p-2', id='space-dropdown-city'
            ),
        ], style={'width': '20%'}, className='border', md=2,
        ),

        dbc.Col([
            html.Div([
                'Prescriptions',
                dcc.Dropdown([
                    'Johor', 'Kedah', 'Kelantan', 'Labuan', 'Kuala Lumpur', 'Malacca', 'Negeri Sembilan', 'Pahang',
                    'Perak', 'Perlis', 'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'
                ], multi=True, className='p-2'
                )
            ], className='p-2'
            ),
        ], style={'width': '20%'}, className='border', md=2
        ),

    ], className='d-flex border'
    ),

    dbc.Row(
        [
            # dbc.Col([dcc.Graph(figure=fig)]),
            dbc.Col([dcc.Graph(figure=fig2, id='map-1')], style={'height': '500px'})
        ], className='border'),

    '''dbc.Stack([
        html.Div([
            'States',
            dcc.Dropdown([
                'Johor', 'Kedah', 'Kelantan', 'Labuan', 'Kuala Lumpur', 'Malacca', 'Negeri Sembilan', 'Pahang', 'Perak', 'Perlis',
                'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'
            ], multi=True)
        ], className='border border-dark', style={'width': '20%'}),
        html.Div([
            'Prescriptions',
            dcc.Dropdown([
                'Johor', 'Kedah', 'Kelantan', 'Labuan', 'Kuala Lumpur', 'Malacca', 'Negeri Sembilan', 'Pahang',
                'Perak', 'Perlis', 'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'
            ], multi=True)
        ], className='border border-dark', style={'width': '20%'}),
    ], direction='horizontal'),'''
])


# --------------------------------------------------- App Callbacks ----------------------------------------------------

@app.callback(
    Output('map-1', 'figure'),
    Input('dropdown-states', 'value'),
    # prevent_initial_call=True
)
def update_map(value):
    if value == 'Johor':
        df_johor = df[df['admin_name'] == 'Johor']
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Kedah':
        df_johor = df[df['admin_name'] == 'Kedah']
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Kelantan':
        df_johor = df[df['admin_name'] == 'Kelantan']
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=7.5, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Labuan':
        df_johor = df[df['admin_name'] == 'Labuan']
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Kuala Lumpur':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Malacca':
        df_johor = df[df['admin_name'] == 'Melaka']
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Negeri Sembilan':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Pahang':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Perak':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Perlis':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Pulau Pinang':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Putrajaya':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Sabah':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=7, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=30)
        return fig3
    elif value == 'Sarawak':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=6, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=30)
        return fig3
    elif value == 'Selangor':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=8, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3
    elif value == 'Terengganu':
        df_johor = df[df['admin_name'] == value]
        print(df_johor)
        fig3 = px.scatter_map(df_johor, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=7.5, height=700)
        fig3.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=20)
        return fig3

    else:
        fig2 = px.scatter_map(df, lat="lat", lon="lng", size="population_proper", color='population_proper', hover_name='city', zoom=4.5, height=700)
        fig2.update_traces(cluster=dict(enabled=False, color='lightcoral', size=20, step=1), visible=True, marker_size=df['population_proper'] * 2)
        return fig2


if __name__ == '__main__':
    app.run(debug=True, port=8050)

