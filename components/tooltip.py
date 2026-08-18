from dash import html


source = html.Div(
    style={
        "display": "flex",
        "flexDirection": "row",
        "position": "absolute",
        "bottom": "2%",
        "left": "42%",
        "gap": "8px",
    },
    children=[
        html.A(
            href="http://data.un.org/_Docs/SYB/PDFs/SYB67_246_202411_Population%20Growth,%20Fertility%20and%20Mortality%20Indicators.pdf",
            target="_blank",
            children=[
                html.Img(
                    src="/assets/images/database.png",
                    style={"width": "15px", "height": "15px", "cursor": "pointer"},
                ),
            ],
        ),
        html.Div(
            style={"display": "flex", "flexDirection": "column", "fontSize": "8px"},
            children=[
                html.P(
                    "Title: Population growth, fertility, life expectancy and mortality",
                    style={"margin": "0", "padding": "0"},
                ),
                html.P("Author: CSO-UNSC", style={"margin": "0", "padding": "0"}),
            ],
        ),
    ],
)
