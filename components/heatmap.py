from dash import html, dcc
import dash_daq as daq

store = dcc.Store(id="selected-countries-store", data=[])

heatmap = html.Div(
    style={
        "height": "100%",
        "display": "flex",
        "flexDirection": "column",
        "overflow": "hidden",
    },
    children=[
        html.Div(
            style={
                "height": "60px",
                "display": "flex",
                "flexDirection": "row",
                "alignItems": "center",
                "gap": "5px",
                "padding": "5px",
                # 'border': '1px solid black',
                "flexShrink": 0,
            },
            children=[
                html.Div(
                    style={"display": "flex", "flexDirection": "column"},
                    children=[
                        html.H3(
                            "Fertility Rate | Mortality Ratio",
                            style={"margin": 0, "fontSize": "16px"},
                        ),
                        html.P(
                            "African countries tend to have the highest fertility and mortality rates, followed by countries in the",
                            style={"margin": 0, "fontSize": "12px"},
                        ),
                        html.P(
                            "Oceanic region and Asia. Europe on the other hand, exhibits contrasting trends.",
                            style={"margin": 0, "fontSize": "12px"},
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        daq.ToggleSwitch(
                            style={
                                "position": "absolute",
                                "bottom": "30%",
                                "right": "1.3%",
                                "zIndex": "999",
                            },
                            id="continent-country-toggle",
                            value=False,
                            vertical=True,
                            color="#17becf",
                        ),
                        html.Div(
                            style={
                                "position": "absolute",
                                "bottom": "30%",
                                "right": "4%",
                                "display": "flex",
                                "flexDirection": "column",
                                "marginRight": "10px",
                                "textAlign": "right",
                                "height": "50px",
                                "justifyContent": "space-around",
                            },
                            children=[
                                html.Span(
                                    "Countries",
                                    style={"fontSize": "12px"},
                                ),
                                html.Span(
                                    "Continents",
                                    style={"fontSize": "12px"},
                                ),
                            ],
                        ),
                    ]
                ),
            ],
        ),
        html.Div(
            style={"flex": 1, "overflow": "hidden", "minHeight": 0},
            children=[
                dcc.Graph(
                    id="heatmap-graph",
                    style={"height": "100%", "width": "100%"},
                    config={"displayModeBar": False},
                )
            ],
        ),
    ],
)
