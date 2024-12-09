import streamlit as st

from utils import load_data, plot_line_chart, plot_bar_chart, plot_histogram

# datasets file paths, in production need to use the gdrive
BENIN = '1eAh3rWhpLyUe8xwLaRKSKNhyjU4nuhpW'
SIERRA = '1moW_22LQgsmjwdmZDkiDPnW6Om5GE6pc'
TOGO = '1h0eRUTzwCUTwAdSA20-r3ddNyslFQiKK'

datasets = {
    'Benin Malanville': BENIN,
    'Sierra Leone': SIERRA,
    'Togo Dapaong QC': TOGO,
}

solar_irradiance_measures = ['GHI', 'DNI', 'DHI']
wind_speed_measures = ['WS', 'WSgust']

st.title('MoonLight Solar Data Analysis')

default_index = 0
dataset_options = [BENIN, SIERRA, TOGO]

# make the user select the dataset from the list of datasets
selected_dataset = st.selectbox('select a dataset', options=list(datasets.keys()), index=default_index,
                                key='dataset_selection_box')

st.subheader('See how the solar radiations change over time')
st.text('Visualize with the help of a bar chart or line chart')

col1, col2 = st.columns(2)
with col1:
    field_1 = st.selectbox('select a field to visualize', options=solar_irradiance_measures, key='field_selection_box_1')
with col2:
    chart_type = st.selectbox('what type of visual do you want', options=['Line Chart', 'Bar Chart'],
                              key='chart_type_selection_box')

df = load_data(datasets[selected_dataset])
monthly_average_df = df.groupby('Month').mean()

# draw the chart based on the users choice
chart_functions = {
    'Line Chart': plot_line_chart,
    'Bar Chart': plot_bar_chart
}

chart_function = chart_functions.get(chart_type)
if chart_function:
    chart_function(monthly_average_df, field_1)

st.subheader('See how the solar radiation readings are distributed')
col1, col2 = st.columns(2)

with col1:
    field_2 = st.selectbox('select a field to visualize', options=solar_irradiance_measures, key='field_selection_box_2')

with col2:
    st.markdown('See how the values are distributed with a **Histogram**')

plot_histogram(df, field_2, '')
