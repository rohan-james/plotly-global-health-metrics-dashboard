from dash import html, dcc
import dash_daq as daq

hero_section = html.Div(
    style={
        "position": "absolute",
        "display": "flex",
        "flexDirection": "column",
        "top": "35%",
        "left": "50%",
        "gap": "0px",
    },
    children=[
        html.P("Average ", style={"margin": "0", "padding": "0"}),
        html.H5(id="hero-metric-text", style={"margin": "0", "padding": "0"}),
        html.P("Other Health Metrics of", style={"margin": "0", "padding": "0"}),
        html.H5(
            id="hero-metric-country",
            style={"margin": "0", "padding": "0", "fontWeight": "bold"},
        ),
    ],
)
