import pandas as pd
import plotly.express as px
from dash import Output, Input

from app_instance import app
from data_loader import data


@app.callback(Output("bubble-chart", "figure"), Input("chart-toggle", "value"))
def update_bubble_chart(toggle_value):
    dff = data.df.copy()

    num_cols = [
        "Life expectancy at birth for both sexes (years)",
        "Total fertility rate (children per women)",
        "Population annual rate of increase (percent)",
    ]
    for col in num_cols:
        dff[col] = pd.to_numeric(dff[col], errors="coerce")

    safe_size = dff["Population annual rate of increase (percent)"].abs()

    safe_size = safe_size.fillna(0)

    fig = px.scatter(
        dff,
        x="Life expectancy at birth for both sexes (years)",
        y="Total fertility rate (children per women)",
        size=safe_size,
        size_max=40,
        color="Continent",
        hover_name="Region",
        animation_frame="Year",
        trendline="lowess",
        trendline_options=dict(frac=0.1),
        trendline_scope="overall",
        trendline_color_override="black",
    )

    fig.update_layout(
        xaxis_title="Life Expectancy at Birth",
        yaxis_title="Total Fertility Rate",
        margin={"l": 60, "r": 150, "t": 0, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )

    return fig
