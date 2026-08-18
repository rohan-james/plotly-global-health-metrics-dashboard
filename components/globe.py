from dash import html, dcc
import dash_daq as daq

globe = html.Div(
    style={
        "height": "100%",
        "display": "flex",
        "flexDirection": "column",
        "overflow": "hidden",
    },
    children=[
        dcc.Store(id="animation-trigger", data="start"),
        html.Div(
            style={
                "display": "flex",
                "flexDirection": "column",
                "position": "absolute",
                "top": "3%",
                "left": "56%",
            },
            children=[
                html.H3(
                    "Overview of The World",
                    style={"margin": 0, "fontSize": "16px"},
                ),
                html.P(
                    "Fertility reflects reproductive capacity, while mortality ratio measures deaths per",
                    style={"margin": 0, "fontSize": "12px"},
                ),
                html.P(
                    "100,000 population, with their difference determining natural population growth.",
                    style={"margin": 0, "fontSize": "12px"},
                ),
            ],
        ),
        html.Div(
            style={
                "height": "60px",
                "display": "flex",
                "flexDirection": "row",
                "alignItems": "center",
                "paddingLeft": "10px",
            },
            children=[
                html.Div(
                    children=[
                        html.H3(
                            "Global",
                            style={
                                "position": "absolute",
                                "top": "0%",
                                "left": "43%",
                                "fontSize": "48px",
                            },
                        ),
                        html.H3(
                            "Health",
                            style={
                                "position": "absolute",
                                "top": "6%",
                                "left": "46%",
                                "fontSize": "48px",
                                "color": "green",
                            },
                        ),
                        html.H3(
                            "Metrics",
                            style={
                                "position": "absolute",
                                "top": "12%",
                                "left": "49%",
                                "fontSize": "48px",
                            },
                        ),
                    ],
                ),
                dcc.Dropdown(
                    style={
                        "position": "absolute",
                        "top": "46%",
                        "right": "3%",
                        "zIndex": "999",
                        "width": "100px",
                    },
                    id="Year",
                    options=["2010", "2015", "2020"],
                    value="2010",
                    clearable=False,
                ),
                html.Div(
                    children=[
                        daq.ToggleSwitch(
                            style={
                                "position": "absolute",
                                "top": "4%",
                                "right": "1.3%",
                                "zIndex": "999",
                            },
                            id="metric-select",
                            value=False,
                            vertical=True,
                            color="#AA2B1D",
                        ),
                        html.Div(
                            style={
                                "position": "absolute",
                                "top": "4.5%",
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
                                    "Mortality Ratio",
                                    style={"fontSize": "12px"},
                                ),
                                html.Span(
                                    "Fertility Rate",
                                    style={"fontSize": "12px"},
                                ),
                            ],
                        ),
                    ]
                ),
            ],
        ),
        html.Div(
            style={"flex": 1, "overflow": "visible", "height": "200px"},
            children=[
                dcc.Graph(
                    id="global-graph",
                    style={"height": "100%", "width": "100%"},
                    config={"displayModeBar": False, "scrollZoom": True},
                )
            ],
        ),
    ],
)
