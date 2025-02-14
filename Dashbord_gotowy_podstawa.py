from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
from Dash_project.data_api import *
import dash_mantine_components as dmc
import plotly.express as px


app = Dash()


app.layout = dmc.Container([
    dmc.Title('--------------------The Most Awesomeness dashboard  in the universe-------------------', color="blue", size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ['Łączna suma transakcji', 'Łączna liczba butelek na aukcjach']],
            id='my-dmc-radio-item',
            value='Łączna suma transakcji',
            size="sm"
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(
                                data=df_1_basic_data.to_dict("records"),
                                page_size=8,
                                style_table={'overflowX': 'auto'},
                                # style_header={ 'border': '1px solid black' },
                                # style_cell={ 'border': '1px solid grey' },)
            )
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df_1_basic_data, x='Nazwa Aukcji', y=col_chosen,)
    return fig

if __name__ == '__main__':
    app.run(debug=True)