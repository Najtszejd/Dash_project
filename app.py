from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from data_api import *

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = dbc.Container([
    html.Div(children='----------------------------------------------------------------- Dane dla poszczególnych aukcji od 2023-01-01 -------------------'),
    dash_table.DataTable(
        data=auction_table_data.to_dict('records'),
        page_size=10,
        sort_action = "native",
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
                             )),

    dcc.Graph(figure=px.pie(auction_table_data[["Nazwa aukcji","Wolumen obrotu"]],
                            values = "Wolumen obrotu",
                            names = "Nazwa aukcji",
                            title = "Udział poszczególnych aukcji w wolumenie",
                            template = "plotly_dark").update_layout(title_x=0.5)
                            )
    # dcc.Graph(figure=px.histogram(distilleries_info_df, x='name', y='whiskybase_votes', histfunc='avg'))
])
    
if __name__ == '__main__':
    app.run(debug=True)