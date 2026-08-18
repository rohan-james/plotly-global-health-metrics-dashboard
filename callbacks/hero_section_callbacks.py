from dash import callback, Output, Input
from app_instance import app


@app.callback(
    Output("hero-metric-text", "children"),
    Output("hero-metric-country", "children"),
    Input("global-graph", "clickData"),
    Input("metric-select", "value"),
)
def update_hero_section(clickData, metric_value):
    metric_name = "Life Expectancy and"
    country_name = "The World"
    if clickData and "points" in clickData and len(clickData["points"]) > 0:
        country_name = clickData["points"][0].get("location", "The World")

    return metric_name, country_name
