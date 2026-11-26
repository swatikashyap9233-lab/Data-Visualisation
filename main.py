
from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = dbc.Container([
    html.H1("My First Dash App"),

    dcc.Input(
        id="my_text",
        value="Type Text here",
        type="text"
    ),

    dcc.Markdown(
        id="my_output",
        children=""
    )
])

@app.callback(
    Output("my_output", "children"),
    Input("my_text", "value")
)
def update_output(value):
    return f"You typed: {value}"

if __name__ == "__main__":
    app.run(debug=True)
