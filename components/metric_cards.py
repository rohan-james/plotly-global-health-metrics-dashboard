from dash import html


def metric_card(value, label, color, metric_id, font_colour):

    inverted = metric_id in ["metric-life", "metric-maternal"]

    if inverted:
        border_style = {
            "width": "0",
            "height": "0",
            "border-left": "40px solid transparent",
            "border-right": "40px solid transparent",
            "border-bottom": f"70px solid {color}",
        }
        text_top_pos = "65%"
    else:
        border_style = {
            "width": "0",
            "height": "0",
            "border-left": "40px solid transparent",
            "border-right": "40px solid transparent",
            "border-top": f"70px solid {color}",
        }
        text_top_pos = "35%"

    return html.Div(
        style={
            "position": "relative",
            "width": "120px",
            "height": "100px",
            "margin": "0 -30px",
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
        },
        children=[
            html.Div(style=border_style),
            html.H2(
                value,
                id=metric_id,
                style={
                    "position": "absolute",
                    "top": text_top_pos,
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "margin": "0",
                    "font-size": "14px",
                    "font-weight": "bold",
                    "color": "black",
                    "zIndex": "10",
                    "whiteSpace": "nowrap",
                    "textShadow": "0px 0px 2px rgba(255,255,255,0.5)",
                    "color": font_colour,
                },
            ),
        ],
    )
