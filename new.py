# Step 1: Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the built-in Iris dataset
df = px.data.iris()

# Step 2: Initialize the Dash app
app = Dash(__name__)

# Step 3: Define the app layout
app.layout = html.Div([
    html.H1("Iris Dataset Interactive Scatter Plot"),

    # Dropdown to select species
    dcc.Dropdown(
        id="species_dropdown",
        options=[{"label": s, "value": s} for s in df["species"].unique()],
        value="setosa",  # Default selected value
        clearable=False
    ),

    # Graph container
    dcc.Graph(id="iris_graph")
])


# Step 4: Create callback (Shown in your photo)
@app.callback(
    Output(component_id="iris_graph", component_property="figure"),
    Input(component_id="species_dropdown", component_property="value")
)
def update_graph(selected_species):
    # Filter dataset
    filtered_df = df[
        df["species"] == selected_species
        ]

    # Generate graph
    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        title=f"Sepal Dimensions for {selected_species.capitalize()}"
    )

    return fig


# Step 5: Run the server
if __name__ == "__main__":
    app.run(debug=True)