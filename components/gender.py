from dash import html, dcc

from components.gender_metrics import gender_metrics

gender_section = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "position": "absolute",
        "top": "20%",
        "left": "40%",
        "zIndex": "999",
    },
    children=[
        gender_metrics("assets/images/female.png", "111", "female-rate"),
        gender_metrics("assets/images/male.png", "111", "male-rate"),
    ],
)
