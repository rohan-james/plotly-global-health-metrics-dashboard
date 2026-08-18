from dash import html


def gender_metrics(img_src, value, metric_id):
    return html.Div(
        style={
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "fontWeight": "bold",
            "paddingBottom": "30px",
        },
        children=[
            html.Img(src=img_src, style={"width": "40px", "height": "40px"}),
            html.P(value, id=metric_id),
        ],
    )
