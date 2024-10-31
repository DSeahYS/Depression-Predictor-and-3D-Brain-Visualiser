from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

def register_callbacks(app):
    @app.callback(
        Output('sample-graph', 'figure'),
        [Input('region-dropdown', 'value')]
    )
    def update_sample_graph(selected_region):
        df = pd.read_csv('data/processed/processed_data1.csv')
        # Since 'region' and 'feature' columns do not exist in processed_data1.csv,
        # we need to adjust this callback or remove it.
        # For demonstration, let's create a simple bar chart of normalized features.
        if selected_region == "All":
            fig = px.bar(df, x='subject_id', y=['feature1_normalized', 'feature2_normalized', 'feature3_normalized'],
                         barmode='group', title="Normalized Features for All Subjects")
        else:
            # Placeholder for specific region data
            fig = px.bar(title="No specific region data available.")
        return fig
