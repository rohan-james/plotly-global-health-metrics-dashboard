import pandas as pd
import plotly.graph_objects as go
from app_instance import app
from dash import callback, Output, Input, State, ctx
from data_loader import data


@app.callback(
    Output("global-graph", "figure"),
    Output("selected-countries-store", "data"),
    Input("Year", "value"),
    Input("metric-select", "value"),
    Input("global-graph", "clickData"),
    Input("continent-country-toggle", "value"),
    State("selected-countries-store", "data"),
)
def update_globe(selected_year, metric, clickData, show_continents, selected_countries):
    if selected_countries is None:
        selected_countries = []

    temp_df = data.df[data.df["Year"] == int(selected_year)].copy()

    if not metric:
        col = data.columns.FERTILITY_COL
        colors = "Greens"
    else:
        col = data.columns.MATERNAL_COL
        colors = "Reds"

    temp_df_un = temp_df[temp_df["Source"] == "United Nations Population Division"]
    temp_df_un[col] = pd.to_numeric(temp_df_un[col], errors="coerce")

    if temp_df_un[col].isna().all() or len(temp_df_un) == 0:
        temp_df[col] = pd.to_numeric(temp_df[col], errors="coerce")
        temp_df = temp_df.dropna(subset=[col])
    else:
        temp_df = temp_df_un

    zvals = (
        pd.to_numeric(temp_df[col], errors="coerce") if col in temp_df.columns else None
    )

    if not show_continents:
        selected_countries = []
    elif clickData and ctx.triggered_id == "global-graph":
        clicked_country = clickData["points"][0]["location"]
        if clicked_country not in selected_countries:
            selected_countries = selected_countries.copy()
            selected_countries.append(clicked_country)

    fig = go.Figure(
        data=go.Choropleth(
            locations=temp_df["Region"],
            z=zvals,
            text=temp_df["Region"],
            locationmode="country names",
            colorscale=colors,
            marker_line_color="darkgray",
        )
    )

    fig.update_geos(
        projection_type="robinson",
        showframe=False,
        showcoastlines=True,
        projection_scale=1.2,
        showcountries=True,
    )

    fig.update_layout(
        uirevision="constant",
        height=None,
        autosize=True,
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(bgcolor="rgba(0,0,0,0)"),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.1,
            xanchor="center",
            x=0.5,
        ),
    )

    return fig, selected_countries
