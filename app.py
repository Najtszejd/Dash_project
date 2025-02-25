from dash import Dash, html, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from data_api import *

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

@app.callback(
    Output("graph", "figure"), 
    Input("selection", "value")
)
def display_animated_graph(selection):
    df = auctions_data_df.sort_values("Data", ascending=True)
    
    fig = px.bar(
        df, 
        x="Nazwa aukcji", 
        y="Wolumen obrotu", 
        color="Nazwa aukcji", 
        animation_frame="Data", 
        animation_group="Nazwa aukcji", 
        range_y=[0, 5000000],
        template="plotly_dark"
    )
    
    fig.update_layout(
        title_x=0.5,
        transition=dict(duration=1000, easing='cubic-in-out'),
        width = 600,
        height = 600,
        showlegend=False,
        sliders=[{
        "y": 1.7, 
        "yanchor": "top",  
        "pad": {"t": 50, "b": 10}  
    }],
        updatemenus=[{
        "buttons": [
            {
                "args": [None, {
                    "frame": {"duration": 500, "redraw": True},
                    "fromcurrent": True
                }],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {
                    "frame": {"duration": 0, "redraw": True},
                    "mode": "immediate",
                    "transition": {"duration": 0}
                }],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,           
        "xanchor": "right",
        "y": 1.8,         
        "yanchor": "top"
    }]
)
    
    categories = sorted(df["Nazwa aukcji"].unique())
    fig.update_xaxes(
        categoryorder='array', categoryarray=categories,
        # showticklabels=False
        )
    
    return fig

app.layout = dbc.Container([
    html.Div("-------------------Dane dla poszczególnych aukcji od 2023-01-01 -------------------"),
    
    dash_table.DataTable(
        data=auction_table_data.to_dict('records'),
        page_size=10,
        sort_action="native",
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    ),
    
    html.Div([
        html.Div(
            dcc.Graph(figure=px.pie(
                auction_table_data[["Nazwa aukcji", "Wolumen obrotu"]],
                values="Wolumen obrotu",
                names="Nazwa aukcji",
                title=f"Udział poszczególnych aukcji w całkowitym wolumenie <br> od 2023-01-01",
                template="plotly_dark"
            ).update_layout(title_x=0.5, width=600, height=600)),
        style={'flex': '1', 'padding': '10px'},
        ),
        html.Div(
        [
            dcc.RadioItems(
                id='selection',             
            ),
            dcc.Graph(id="graph")
        ],
        style={'flex': '1', 'padding': '10px'}
    )
    ],  style={'display': 'flex', 'justifyContent': 'space-between'}),
    

    dcc.Graph(figure=px.line(
        auctions_data_df[['Data', "Nazwa aukcji", "Wolumen obrotu", "Liczba pozycji"]], 
        x="Data", 
        y="Wolumen obrotu",
        title="Wyres wolumenu dla wszystkich aukcji <br> od 2023-02-01",
        color="Nazwa aukcji", 
        symbol="Nazwa aukcji",
        hover_name="Nazwa aukcji",
        hover_data={"Liczba pozycji": True},
        template="plotly_dark"
    ).update_layout(title_x=0.5))
])

if __name__ == '__main__':
    app.run(debug=True)