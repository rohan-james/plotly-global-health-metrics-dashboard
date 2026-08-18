from dash import html
import dash_mantine_components as dmc
import dash_daq as daq

from components.filters_box import header_filters_section
from components.globe import globe
from components.heatmap import heatmap, store
from components.bubble_chart import bubble_chart
from components.histplot import histplot
from components.gender import gender_section
from components.hero_text import hero_section
from components.right_down_arrow import right_down_arrow
from components.up_arrow import up_arrow
from components.tooltip import source
from components.lines.vertical_spans import vertical_line
from components.lines.horizontal_spans import (
    horizontal_line_female,
    horizontal_line_male,
    horizontal_line_avg,
)

layout = html.Div(
    style={
        "width": "100vw",
        "height": "100vh",
        "overflow": "hidden",
        "backgroundColor": "#EFF8FF",
        "boxSizing": "border-box",
    },
    children=[
        html.Div(
            style={
                "display": "flex",
                "flexDirection": "row",
                "width": "100%",
                "height": "100%",
                "boxSizing": "border-box",
            },
            children=[
                # Left column
                html.Div(
                    style={
                        "width": "50%",
                        "height": "100%",
                        "display": "flex",
                        "flexDirection": "column",
                        "overflow": "hidden",
                        "boxSizing": "border-box",
                    },
                    children=[
                        html.Div(
                            style={
                                "flexShrink": 0,
                                "overflowY": "hidden",
                                "height": "55%",
                            },
                            children=[histplot],
                        ),
                        html.Div(
                            style={
                                "position": "absolute",
                                "top": "50%",
                                "left": "-30%",
                                "flexShrink": 0,
                                "padding": "10px",
                                "display": "flex",
                                "alignItems": "center",
                                "justifyContent": "center",
                            },
                            children=[
                                daq.ToggleSwitch(
                                    id="chart-toggle",
                                    value=False,
                                    label={
                                        "label": "Bubble Chart | Sankey Diagram",
                                        "style": {"fontSize": "14px"},
                                    },
                                    color="#3498db",
                                    vertical=True,
                                )
                            ],
                        ),
                        html.Img(
                            style={
                                "position": "absolute",
                                "top": "52%",
                                "left": "40%",
                                "width": "120px",
                                "height": "130px",
                                "border": "solid 0.4px",
                            },
                            src="/assets/images/legend.png",
                        ),
                        up_arrow,
                        hero_section,
                        vertical_line,
                        horizontal_line_female,
                        horizontal_line_male,
                        horizontal_line_avg,
                        right_down_arrow,
                        html.Div(
                            id="chart-container",
                            style={
                                "flex": 1,
                                "overflow": "hidden",
                                "display": "flex",
                                "flexDirection": "column",
                            },
                            children=[
                                html.Div(
                                    style={
                                        "flex": 1,
                                        "overflow": "hidden",
                                        "display": "flex",
                                        "flexDirection": "column",
                                    },
                                    children=[bubble_chart],
                                )
                            ],
                        ),
                    ],
                ),
                # Right column
                source,
                html.Div(
                    style={
                        "width": "50%",
                        "height": "100%",
                        "display": "flex",
                        "flexDirection": "column",
                        "overflow": "visible",
                        "boxSizing": "border-box",
                    },
                    children=[
                        html.Div(
                            style={
                                "height": "40%",
                                "overflow": "visible",
                                "padding": "10px",
                                # "boxSizing": "border-box",
                            },
                            children=[globe],
                        ),
                        gender_section,
                        html.Div(
                            style={
                                "flexShrink": 0,
                                "overflowY": "hidden",
                                "height": "20%",
                            },
                            children=[header_filters_section],
                        ),
                        html.Div(
                            style={
                                "height": "40%",
                                "overflow": "auto",
                                "padding": "10px",
                                "boxSizing": "border-box",
                            },
                            children=[heatmap, store],
                        ),
                    ],
                ),
            ],
        )
    ],
)
