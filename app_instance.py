from dash import Dash
from assets.styles import external_stylesheets

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
