import pandas as pd
from dash import Output, Input
from app_instance import app
from data_loader import data


@app.callback(
    [
        Output("metric-total", "children"),
        Output("metric-life", "children"),
        Output("metric-fertility", "children"),
        Output("metric-maternal", "children"),
        Output("metric-under5", "children"),
    ],
    [Input("Year", "value"), Input("global-graph", "clickData")],
)
def update_metrics(year, clickData):

    filtered_df = data.df.copy()

    if year:
        filtered_df = filtered_df[filtered_df["Year"] == int(year)]

    if clickData:
        region = clickData["points"][0]["location"]
        if region and region != "All":
            filtered_df = filtered_df[filtered_df["Region"] == region]
    else:
        region = "All"

    total_records = len(filtered_df)

    avg_life = (
        pd.to_numeric(
            filtered_df[data.columns.LIFE_EXPECTANCY_COL], errors="coerce"
        ).mean()
        if (
            data.columns.LIFE_EXPECTANCY_COL
            and data.columns.LIFE_EXPECTANCY_COL in filtered_df.columns
            and len(filtered_df) > 0
        )
        else 0
    )

    avg_fertility = (
        pd.to_numeric(filtered_df[data.columns.FERTILITY_COL], errors="coerce").mean()
        if (
            data.columns.FERTILITY_COL
            and data.columns.FERTILITY_COL in filtered_df.columns
            and len(filtered_df) > 0
        )
        else 0
    )

    avg_maternal = (
        pd.to_numeric(filtered_df[data.columns.MATERNAL_COL], errors="coerce").mean()
        if (
            data.columns.MATERNAL_COL
            and data.columns.MATERNAL_COL in filtered_df.columns
            and len(filtered_df) > 0
        )
        else 0
    )

    avg_under5 = (
        pd.to_numeric(filtered_df[data.columns.UNDER5_COL], errors="coerce").mean()
        if (
            data.columns.UNDER5_COL
            and data.columns.UNDER5_COL in filtered_df.columns
            and len(filtered_df) > 0
        )
        else 0
    )

    return (
        f"{total_records:,}",
        f"{avg_life:.1f}" if not pd.isna(avg_life) and avg_life > 0 else "N/A",
        (
            f"{avg_fertility:.2f}"
            if not pd.isna(avg_fertility) and avg_fertility > 0
            else "N/A"
        ),
        (
            f"{avg_maternal:.1f}"
            if not pd.isna(avg_maternal) and avg_maternal > 0
            else "N/A"
        ),
        f"{avg_under5:.1f}" if not pd.isna(avg_under5) and avg_under5 > 0 else "N/A",
    )
