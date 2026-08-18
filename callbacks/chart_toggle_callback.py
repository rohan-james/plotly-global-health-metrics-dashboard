from dash import Input, Output, html
from components.bubble_chart import bubble_chart
from components.sankey_diagram import sankey_diagram

from app_instance import app


@app.callback(Output("chart-container", "children"), Input("chart-toggle", "value"))
def toggle_chart(show_line_chart):
    wrapper_style = {
        "flex": 1,
        "overflow": "hidden",
        # "padding": "10px",
        "display": "flex",
        "flexDirection": "column",
    }

    if show_line_chart:
        return html.Div(style=wrapper_style, children=[sankey_diagram])

    else:
        return html.Div(style=wrapper_style, children=[bubble_chart])
