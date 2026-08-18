import pandas as pd
import numpy as np
from dash import Input, Output
import plotly.figure_factory as ff
import plotly.express as px

from app_instance import app
from data_loader import data


@app.callback(Output("hist-plot", "figure"), Input("chart-toggle", "value"))
def update_histplot(toggle_value):
    df_hist = data.df[
        (data.df[data.columns.FEMALE_LIFE_EXP].notna())
        & (data.df[data.columns.MALE_LIFE_EXP].notna())
    ][["Continent", data.columns.FEMALE_LIFE_EXP, data.columns.MALE_LIFE_EXP]]

    df_hist_1 = df_hist[["Continent", data.columns.FEMALE_LIFE_EXP]]
    df_hist_1["Gender"] = "female"
    df_hist_2 = df_hist[["Continent", data.columns.MALE_LIFE_EXP]]
    df_hist_2["Gender"] = "male"

    df_hist_concat = pd.concat([df_hist_1, df_hist_2], axis=0)

    df_hist_concat["lifeExpectancy"] = np.where(
        df_hist_concat[data.columns.FEMALE_LIFE_EXP].notna(),
        df_hist_concat[data.columns.FEMALE_LIFE_EXP],
        df_hist_concat[data.columns.MALE_LIFE_EXP],
    )

    fig = px.histogram(
        df_hist_concat,
        x="lifeExpectancy",
        color="Continent",
        marginal="rug",
        nbins=50,
        opacity=0.7,
        barmode="overlay",
        facet_row="Gender",
    )

    fig.update_layout(
        xaxis_title="Life Expectancy (years)",
        yaxis_title="Countries Per Bin",
        showlegend=False,
        margin={"l": 60, "r": 150, "t": 100, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
    )
    fig.for_each_annotation(lambda a: a.update(text=""))
    fig.update_yaxes(title_text="", row=2)
    return fig
