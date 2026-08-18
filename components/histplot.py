from dash import html, dcc

histplot = html.Div(
    style={"display": "flex", "flexDirection": "column", "overflow": "hidden"},
    children=[
        html.Div(
            style={
                "display": "flex",
                "flexDirection": "column",
                "position": "absolute",
                "top": "2%",
                "left": "4%",
            },
            children=[
                html.H3(
                    "Life Expectancy",
                    style={"margin": 0, "fontSize": "16px"},
                ),
                html.P(
                    "Life expectancy is binned into increments of 2 and countries are grouped; continents, colour coded.",
                    style={"margin": 0, "fontSize": "12px"},
                ),
                html.P(
                    "Emperical Analyses reveal that with the passage of time, women on an average live longer than men.",
                    style={"margin": 0, "fontSize": "12px"},
                ),
            ],
        ),
        dcc.Graph(id="hist-plot", config={"displayModeBar": False}),
    ],
)
