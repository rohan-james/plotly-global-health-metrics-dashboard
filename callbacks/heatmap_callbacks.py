import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Output, Input
from app_instance import app
from data_loader import data


@app.callback(
    Output("heatmap-graph", "figure"),
    Input("selected-countries-store", "data"),
    Input("continent-country-toggle", "value"),
    Input("metric-select", "value"),
    Input("Year", "value"),
)
def update_heatmap(selected_countries, show_continents, metric, selected_year):
    if not metric:
        col = data.columns.FERTILITY_COL
        color_scale = "Greens"
        metric_label = "Fertility Rate"
    else:
        col = data.columns.MATERNAL_COL
        color_scale = "Reds"
        metric_label = "Mortality Ratio"

    if not show_continents:
        continents = data.df["Continent"].unique().tolist()

        subset = data.df[data.df["Continent"].isin(continents)].copy()
        subset[col] = pd.to_numeric(subset[col], errors="coerce")

        if subset.empty:
            fig = go.Figure()
            fig.update_layout(
                height=None,
                autosize=True,
                margin=dict(l=100, r=20, t=30, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                title="No continent data available",
            )
            return fig

        heat_df = subset.pivot_table(
            index="Continent",
            columns="Year",
            values=col,
            aggfunc="mean",
        )

        heat_df["_sort_value"] = heat_df.mean(axis=1)
        heat_df = heat_df.sort_values("_sort_value", ascending=False)
        heat_df = heat_df.drop("_sort_value", axis=1)

    else:
        if not selected_countries:
            fig = go.Figure()
            fig.update_layout(
                height=None,
                autosize=True,
                margin=dict(l=100, r=20, t=30, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                annotations=[
                    dict(
                        text="Click different countries on the globe to populate the heatmap",
                        xref="paper",
                        yref="paper",
                        x=0.5,
                        y=0.5,
                        showarrow=False,
                        font=dict(size=14, color="gray"),
                    )
                ],
            )
            return fig

        subset = data.df[data.df["Region"].isin(selected_countries)].copy()
        subset[col] = pd.to_numeric(subset[col], errors="coerce")

        if subset.empty:
            fig = go.Figure()
            fig.update_layout(
                height=None,
                autosize=True,
                margin=dict(l=100, r=20, t=30, b=20),
                paper_bgcolor="rgba(0,0,0,0)",
                title="No data available for selected countries",
            )
            return fig

        heat_df = subset.pivot_table(index="Region", columns="Year", values=col).copy()

        heat_df["_sort_value"] = heat_df.mean(axis=1)
        heat_df = heat_df.sort_values("_sort_value", ascending=False)
        heat_df = heat_df.drop("_sort_value", axis=1)

    fig = px.imshow(
        heat_df,
        aspect="auto",
        color_continuous_scale=color_scale,
        labels=dict(x="Year", y="Region", color=metric_label),
    )

    num_rows = len(heat_df.index)
    font_size = max(8, min(12, 200 / num_rows))

    fig.update_layout(
        height=None,
        autosize=True,
        margin=dict(l=120, r=20, t=40, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(side="bottom", tickfont=dict(size=font_size)),
        yaxis=dict(tickfont=dict(size=font_size), automargin=True),
        coloraxis_colorbar=dict(thickness=15, len=0.7, yanchor="middle", y=0.5),
    )

    fig.update_traces(xgap=1, ygap=1)

    return fig
