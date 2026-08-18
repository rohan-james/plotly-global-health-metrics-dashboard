from dash import html, dcc
from data_loader import data

bubble_chart = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "overflow": "hidden",
        "paddingLeft": "10px",
        "height": "90%",
    },
    children=[
        html.Div(
            style={
                "display": "flex",
                "flexDirection": "column",
                "position": "relative",
                "bottom": "2%",
                "left": "4%",
            },
            children=[
                html.H3(
                    "Population Growth Overlay",
                    style={"margin": 0, "fontSize": "16px"},
                ),
                html.P(
                    "With the bubble size representing the population growth rate, the LOESS regression line",
                    style={"margin": 0, "fontSize": "12px"},
                ),
                html.P(
                    "indicates a negative correlation between the fertility rate and the life expectancy at birth.",
                    style={"margin": 0, "fontSize": "12px"},
                ),
            ],
        ),
        dcc.Graph(
            id="bubble-chart",
            style={"flex": "1", "minHeight": 0},
            config={"displayModeBar": False},
        ),
    ],
)
