from dash import html

def register_callbacks(app):
    # No callbacks for the home page
    pass

layout = html.Div([
    html.H1("Welcome to the Neuroimaging Simulator"),
    html.P("Explore brain structures, genetic influences, and behavioral correlations.")
])
