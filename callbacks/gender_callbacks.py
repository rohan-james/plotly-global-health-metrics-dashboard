import pandas as pd
from dash import Output, Input
from app_instance import app
from data_loader import data


@app.callback(
    [Output("male-rate", "children"), Output("female-rate", "children")],
    [Input("Year", "value"), Input("global-graph", "clickData")],
)
def update_gender_metrics(year, clickData):
    filtered_df = data.df.copy()

    if year:
        filtered_df = filtered_df[filtered_df["Year"] == int(year)]

    if clickData:
        region = clickData["points"][0]["location"]
        if region and region != "All":
            filtered_df = filtered_df[filtered_df["Region"] == region]
    else:
        region = "All"

    avg_male_life_exp = pd.to_numeric(
        filtered_df[data.columns.MALE_LIFE_EXP], errors="coerce"
    ).mean()

    avg_female_life_exp = pd.to_numeric(
        filtered_df[data.columns.FEMALE_LIFE_EXP], errors="coerce"
    ).mean()

    return (
        (
            f"{avg_male_life_exp:.1f}"
            if not pd.isna(avg_male_life_exp) and avg_male_life_exp > 0
            else "N/A"
        ),
        (
            f"{avg_female_life_exp:.1f}"
            if not pd.isna(avg_female_life_exp) and avg_female_life_exp > 0
            else "N/A"
        ),
    )
