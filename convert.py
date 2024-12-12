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

party = ['Guardian Pharmacy', 'Caring Pharmacy', 'Watsons', 'Sherlocks', 'Farmasi Unik', 'UnI Pharmacy', 'Klinik Mediviron', 'Worldwide Clinic', 'Cake Hospital', 'West Point Hospital', 'Cube Clinic', 'Colts Pharmacy']
address = ['123 Jalan Ampang', '456 Jalan Bukit Bintang', '789 Jalan SS15/4', '123 Jalan Sultan Zainal Abidin', '456 Jalan Miri-Bintulu', '12 Jalan Hang Tuah', '45 Jalan Tengkera', '789 Jalan Meru', '12 Jalan Gaya', '45 Jalan Tanjung Aru', 'Jalan Kuala Perlis', 'Jalan Barrack']
postcode = ['50450', '55100', '47500', '20000', '98000', '75300', '75200', '41050', '88000', '88100', '02100', '02000']
city = ['Kuala Lumpur', 'Kuala Lumpur', 'Subang Jaya', 'Kuala Terengganu', 'Miri', 'Bandar Melaka', 'Bandar Melaka', 'Klang', 'Kota Kinabalu', 'Kota Kinabalu', 'Kuala Perlis', 'Kangar']
state = ['Kuala Lumpur', 'Kuala Lumpur', 'Selangor', 'Terengganu', 'Sarawak', 'Melaka', 'Melaka', 'Selangor', 'Sabah', 'Sabah', 'Perlis', 'Perlis']
country = ['MY', 'MY', 'MY', 'MY', 'MY', 'Malaysia', 'Malaysia', 'MY', 'MY', 'MY', 'MY', 'MY']

dict = {'party': party, 'address': address, 'postcode': postcode, 'city': city, 'state': state, 'country': country}

df = pd.DataFrame(dict)
# print(df)

ex_address = df.iloc[:, 2:6]
df['full_address'] = df.apply(lambda row: f"{row['address']} {row['postcode']} {row['city']} {row['state']} {row['country']}", axis=1)
# df.to_csv('geocoder.csv')
# print(df)
'''addressLine = df.iloc[:, 7]
address = addressLine
print(address)'''
addressLine = '123 Jalan Ampang 50450 Kuala Lumpur Kuala Lumpur MY'
addressLine = re.sub('\s', '+', addressLine)
api_key = '6756a4f537df1888365864rti94069d'
url = f'https://geocode.maps.co/search?q={addressLine}&api_key={api_key}'
print(url)

headers = {'Accept': 'application/json'}
r = requests.get(url, headers=headers)
with open("sample.json", "w") as outfile:
    json.dump(r.json(), outfile)
# print(f"Response: {r.json()}")


def geocode(addressLine):
    api_key = '6756a4f537df1888365864rti94069d'
    # addressLine = df.iloc[:, 7]
    # addressLine = df.replace([r' '], '+', regex=True)
    url = f'https://geocode.maps.co/search?q={addressLine}&api_key={api_key}'
    return url


df['full_address'] = df.apply(
    lambda row: f"{row['address']} {row['postcode']} {row['city']} {row['state']} {row['country']}", axis=1)
df['full_address'] = df['full_address'].replace([r' '], '+', regex=True)
df['url'] = df['full_address'].apply(geocode)
print(df.url)
df.to_csv('sample_url.csv')
