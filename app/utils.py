import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# constants
MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

@st.cache_data
def load_data(file_id: str) -> pd.DataFrame:
    """
    Load data from a CSV file at the given URL.

    :param file_id: google id of the file to be loaded
    :type file_id: str

    :return: The loaded data as pandas DataFrame
    :rtype: pd.DataFrame
    """
    download_url = f'https://drive.google.com/uc?id={file_id}&export=download'

    dataframe = pd.read_csv(download_url)
    dataframe['Timestamp'] = pd.to_datetime(dataframe['Timestamp'])
    dataframe['Month'] = dataframe['Timestamp'].dt.month
    return dataframe


def plot_line_chart(df: pd.DataFrame, column: str, title: str = '') -> None:
    """
    Plots a line chart for the specified column in the given DataFrame and renders it in Streamlit.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot the line chart for.
    title (str): Title of the chart (optional).

    Returns:
    None
    """
    # Generate a list of abbreviated month names (assumes MONTHS is defined)
    months = [month[:3] for month in MONTHS]  # Ensure MONTHS is defined in your code

    # Create a Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(months, df[column], marker='o', linestyle='-', linewidth=2, markersize=5, label=column)

    # Add titles and labels
    ax.set_title(title, fontsize=16)
    ax.set_xlabel('Months', fontsize=12)
    ax.set_ylabel(f'{column}', fontsize=12)
    ax.legend()
    ax.grid()

    # Render the figure in Streamlit
    st.pyplot(fig)

def plot_bar_chart(df: pd.DataFrame, column: str, title: str = '') -> None:
    """
    Plots a bar chart for the specified column in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot the bar chart for.

    Returns:
    None
    """
    months = [month[:3] for month in MONTHS]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(months, df[column], color='skyblue')

    ax.set_title(title, fontsize=16)
    ax.set_xlabel('Months', fontsize=12)
    ax.set_ylabel(f'{column}', fontsize=12)
    ax.legend([column], title='Legend')

    ax.grid()
    plt.xticks(rotation=45)

    st.pyplot(fig)
