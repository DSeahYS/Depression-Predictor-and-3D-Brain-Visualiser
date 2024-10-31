# Neuroimaging Simulator

## Overview
An interactive simulator for visualizing neuroimaging data and predicting depression based on synthetic data.

## Features
- 3D Brain Visualization using synthetic data
- Depression Prediction Model with a simple RandomForestClassifier
- Interactive Dash application

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/neuro_simulator.git
   cd neuro_simulator

neuro_simulator/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── assets/
│   └── style.css
├── data/
│   ├── raw/
│   │   └── study1_data.csv
│   └── processed/
│       └── processed_data1.csv
├── models/
│   └── depression_model.pkl  # Generated by train_model.py
├── utilities/
│   ├── __init__.py
│   └── data_processing.py
└── pages/
    ├── __init__.py
    ├── home.py
    ├── brain_visualization.py
    └── predict_depression.py
