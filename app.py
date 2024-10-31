import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pages.home as home
import pages.brain_visualization as brain_visualization
import pages.predict_depression as predict_depression

# Initialize the Dash app with suppress_callback_exceptions=True
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Neuroimaging Simulator"

# Define the layout
app.layout = html.Div([
    html.Header([
        html.Nav([
            html.Ul([
                html.Li(html.A("Home", href="/")),
                html.Li(html.A("Brain Visualization", href="/brain")),
                html.Li(html.A("Predict Depression", href="/predict")),
            ], className='navbar')
        ], className='nav-container')
    ]),
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content", className='content')
])

# Callback to update the page content based on URL
@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/brain":
        return brain_visualization.layout
    elif pathname == "/predict":
        return predict_depression.layout
    else:
        return home.layout

# Register callbacks from pages
home.register_callbacks(app)
brain_visualization.register_callbacks(app)
predict_depression.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
