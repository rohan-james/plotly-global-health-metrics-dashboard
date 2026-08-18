import pandas as pd
import plotly.graph_objects as go
from dash import Output, Input

from app_instance import app
from data_loader import data


def get_top_n_countries(group, n=5):
    return group.nlargest(n, "Life expectancy at birth for both sexes (years)")


@app.callback(Output("sankey-diagram", "figure"), Input("chart-toggle", "value"))
def update_sankey_diagram(show_sankey):
    if not show_sankey:
        return go.Figure()

    df_filtered = (
        data.df.groupby("Continent", group_keys=False)
        .apply(get_top_n_countries)
        .reset_index(drop=True)
    )

    all_labels = []
    all_labels.extend(df_filtered["World"].unique())
    all_labels.extend(df_filtered["Continent"].unique())
    all_labels.extend(df_filtered["Region"].unique())

    label_to_index = {label: i for i, label in enumerate(all_labels)}

    source = []
    target = []
    value = []

    world_continent_df = (
        df_filtered.groupby("Continent")[
            "Life expectancy at birth for both sexes (years)"
        ]
        .sum()
        .reset_index()
    )

    for _, row in world_continent_df.iterrows():
        source.append(label_to_index["World"])
        target.append(label_to_index[row["Continent"]])
        value.append(row["Life expectancy at birth for both sexes (years)"])

    for _, row in df_filtered.iterrows():
        source.append(label_to_index[row["Continent"]])
        target.append(label_to_index[row["Region"]])
        value.append(row["Life expectancy at birth for both sexes (years)"])

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=all_labels,
                    color=["blue"] * len(df_filtered["World"].unique())
                    + ["red"] * len(df_filtered["Continent"].unique())
                    + ["green"] * len(df_filtered["Region"].unique()),
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value,
                ),
            )
        ]
    )

    fig.update_layout(
        title_text="Life Expectancy Flow: World -> Continents -> Top 10 Countries",
        font_size=10,
        margin={"l": 0, "r": 0, "t": 20, "b": 80},
        # paper_bgcolor='rgba(0,0,0,0)',
        # plot_bgcolor='rgba(0,0,0,0)',
    )

    return fig
