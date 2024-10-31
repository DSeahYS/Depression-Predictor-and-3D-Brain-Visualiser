from dash import html, dcc
from dash.dependencies import Input, Output, State
import joblib
import pandas as pd
import os

def register_callbacks(app):
    @app.callback(
        Output('prediction-output', 'children'),
        [Input('predict-button', 'n_clicks')],
        [State('feature1', 'value'),
         State('feature2', 'value'),
         State('feature3', 'value')]
    )
    def update_output(n_clicks, feature1, feature2, feature3):
        if n_clicks > 0 and feature1 is not None and feature2 is not None and feature3 is not None:
            input_features = pd.DataFrame([[feature1, feature2, feature3]],
                                          columns=['feature1_normalized', 'feature2_normalized', 'feature3_normalized'])
            prediction = model.predict(input_features)[0]
            return f"Prediction: {'Depressed' if prediction == 1 else 'Not Depressed'}"
        return "Enter features and click Predict"

# Load the pre-trained model
model_path = 'models/depression_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}. Please run 'train_model.py' to train the model.")

layout = html.Div([
    html.H2("Depression Prediction"),
    html.Div([
        html.Label("Feature 1"),
        dcc.Input(id='feature1', type='number', placeholder='Feature 1'),
        html.Br(),
        html.Label("Feature 2"),
        dcc.Input(id='feature2', type='number', placeholder='Feature 2'),
        html.Br(),
        html.Label("Feature 3"),
        dcc.Input(id='feature3', type='number', placeholder='Feature 3'),
        html.Br(),
        html.Button('Predict', id='predict-button', n_clicks=0),
    ], className='input-container'),
    html.Div(id='prediction-output', style={'padding': 20, 'fontSize': 24})
])
