from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from data_api import *

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = dbc.Container([
    html.Div(children='----------------------------------------------------------------- Dane dla poszczególnych aukcji od 2023-01-01 -------------------'),
    dash_table.DataTable(
        data=auction_data_df_filter_table.to_dict('records'),
        page_size=10,
        sort_action = "native",
        columns=[
        {"name": "Nazwa aukcji", "id": "Nazwa aukcji", "type": "text"},
        {"name": "Liczba pozycji", "id": "Liczba pozycji", "type": "numeric"},
        {"name": "Wolumen obrotu", "id": "Wolumen obrotu", "type": "numeric"}
    ],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),

    # dash_table.DataTable(data=auctions_info_df.to_dict('records'), page_size=10),
    # dash_table.DataTable(data=distilleries_info_df.to_dict('records'), page_size=10),
    # dash_table.DataTable(data=distilleries_info_df_slug.to_dict('records'), page_size=10),


    dcc.Graph(figure=px.line(auctions_data_df[['Data', "Nazwa aukcji","Wolumen obrotu","Liczba pozycji"]], 
                             x="Data", 
                             y='Wolumen obrotu', 
                             color = 'Nazwa aukcji', 
                             symbol='Nazwa aukcji',
                             hover_name="Nazwa aukcji",
                             hover_data={"Liczba pozycji":True},
                             template="plotly_dark"
                             ))
    # dcc.Graph(figure=px.histogram(auctions_info_df, x='name', y='buyers_fee', histfunc='avg')),
    # dcc.Graph(figure=px.histogram(distilleries_info_df, x='name', y='whiskybase_votes', histfunc='avg'))
])
    
if __name__ == '__main__':
    app.run(debug=True)