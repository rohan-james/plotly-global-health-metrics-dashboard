from dash import html, dcc

sankey_diagram = html.Div(
    style={
        "display": "flex",
        "flexDirection": "column",
        "overflow": "hidden",
    },
    children=[html.H3("Sankey Diagram"), dcc.Graph(id="sankey-diagram")],
)
