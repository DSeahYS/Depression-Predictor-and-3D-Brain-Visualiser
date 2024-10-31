from dash import html, dcc
import plotly.graph_objs as go
import nibabel as nib
import numpy as np
from nilearn import datasets

def register_callbacks(app):
    # No callbacks for brain visualization currently
    pass

def load_brain_data():
    # Use Nilearn to fetch an example functional brain image
    motor_images = datasets.fetch_neurovault_motor_task()
    # Load the first image from the collection
    img = nib.load(motor_images.images[0])
    data = img.get_fdata()
    return data

def create_3d_brain_figure(brain_data):
    # Threshold the data to focus on areas with significant activation
    threshold = np.percentile(brain_data, 99)
    x, y, z = np.nonzero(brain_data > threshold)
    values = brain_data[x, y, z]
    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=1.5,
            color=values,
            colorscale='Hot',
            opacity=0.7
        )
    )
    layout = go.Layout(
        title="3D Brain Visualization",
        scene=dict(
            xaxis=dict(title='X Axis', visible=False),
            yaxis=dict(title='Y Axis', visible=False),
            zaxis=dict(title='Z Axis', visible=False),
            aspectmode='data'
        ),
        margin=dict(l=0, r=0, b=0, t=50)
    )
    fig = go.Figure(data=[trace], layout=layout)
    return fig

brain_data = load_brain_data()
fig = create_3d_brain_figure(brain_data)

layout = html.Div([
    html.H2("3D Brain Visualization"),
    dcc.Graph(
        id='3d-brain',
        figure=fig,
        style={'height': '80vh'}
    )
])
