from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
from data_api import *

app = Dash()

app.layout = [
    html.Div(children='--------------------The Most Awesomeness dashboard  in the universe-------------------'),
    dash_table.DataTable(data=auctions_data_df.to_dict('records'), page_size=10),
    dash_table.DataTable(data=auctions_info_df.to_dict('records'), page_size=10),
    dash_table.DataTable(data=distilleries_info_df.to_dict('records'), page_size=10),
    dash_table.DataTable(data=distilleries_info_df_slug.to_dict('records'), page_size=10),


    dcc.Graph(figure=px.histogram(auctions_data_df, x='auction_name', y='auction_trading_volume', histfunc='avg')),
    dcc.Graph(figure=px.histogram(auctions_info_df, x='name', y='buyers_fee', histfunc='avg')),
    dcc.Graph(figure=px.histogram(distilleries_info_df, x='name', y='whiskybase_votes', histfunc='avg'))
]

if __name__ == '__main__':
    app.run(debug=True)