from dash import html, dcc
from components.metric_cards import metric_card
from data_loader import data

header_filters_section = html.Div(
    style={
        "padding": "20px 40px",
        "fontFamily": "sans-serif",
    },
    children=[
        html.Div(
            style={
                "display": "flex",
                "flexWrap": "wrap",
                "justifyContent": "center",
                "alignItems": "flex-end",
            },
            children=[
                metric_card(
                    "1,686", "Total Records", "#FF6D1F", "metric-total", "black"
                ),
                metric_card(
                    "72.3", "Avg Life Expectancy", "#DC0000", "metric-life", "white"
                ),
                metric_card(
                    "2.62", "Avg Fertility Rate", "#08CB00", "metric-fertility", "black"
                ),
                metric_card(
                    "167.1",
                    "Avg Maternal Mortality",
                    "#7132CA",
                    "metric-maternal",
                    "white",
                ),
                metric_card(
                    "28.6", "Avg Under-5 Mortality", "#00CAFF", "metric-under5", "black"
                ),
            ],
        ),
        # Color Legend
        html.Div(
            style={"marginTop": "5px", "textAlign": "center"},
            children=[
                html.Div(
                    style={
                        "display": "flex",
                        "gap": "20px",
                        "justifyContent": "center",
                        "fontSize": "14px",
                    },
                    children=[
                        html.Div(
                            [
                                html.Span("■", style={"color": "#FF6D1F"}),
                                " Total Records",
                            ]
                        ),
                        html.Div(
                            [
                                html.Span("■", style={"color": "#DC0000"}),
                                " Life Expectancy",
                            ]
                        ),
                        html.Div(
                            [
                                html.Span("■", style={"color": "#08CB00"}),
                                " Fertility",
                            ]
                        ),
                        html.Div(
                            [
                                html.Span("■", style={"color": "#7132CA"}),
                                " Maternal Mortality",
                            ]
                        ),
                        html.Div(
                            [
                                html.Span(
                                    "■",
                                    style={
                                        "color": "#00CAFF",
                                    },
                                ),
                                " Under-5 Mortality",
                            ]
                        ),
                    ],
                )
            ],
        ),
    ],
)
