import numpy as np
import pandas as pd
import streamlit as st

from utils import load_data, plot_line_chart, plot_bar_chart

# datasets file paths, in production need to use the gdrive
BENIN = '1eAh3rWhpLyUe8xwLaRKSKNhyjU4nuhpW'
SIERRA = '1moW_22LQgsmjwdmZDkiDPnW6Om5GE6pc'
TOGO = '1h0eRUTzwCUTwAdSA20-r3ddNyslFQiKK'

datasets = {
    'Benin Malanville': BENIN,
    'Sierra Leone': SIERRA,
    'Togo Dapaong QC': TOGO,
}

SOLAR_IRRADIANCE_MEASURES = ['GHI', 'DNI', 'DHI']
WIND_SPEED_MEASURES = ['WS', 'Wgust']

st.title('Moon Light Solar Data Analysis')

default_index = 0
dataset_options = [BENIN, SIERRA, TOGO]

# make the user select the dataset from the list of datasets
selected_dataset = st.selectbox('Select a dataset', options=list(datasets.keys()), index=default_index)

# TODO: come up with a better naming for this st.subheader('Time Series Analysis')
st.text('Visualize with the help of a bar chart or line chart')

col1, col2 = st.columns(2)
with col1:
    field = st.selectbox('Select a field to visualize', options=SOLAR_IRRADIANCE_MEASURES)
with col2:
    chart_type = st.selectbox('What type of visual do you want', options=['Line Chart', 'Bar Chart'])

df = load_data(datasets[selected_dataset])
monthly_average_df = df.groupby('Month').mean()

# draw the chart based on the users choice
chart_functions = {
    'Line Chart': plot_line_chart,
    'Bar Chart': plot_bar_chart
}

chart_function = chart_functions.get(chart_type)
if chart_function:
    chart_function(monthly_average_df, field)