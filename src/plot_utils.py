import pandas as pd
import matplotlib.pyplot as plt

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


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
    plt.figure(figsize=(20, 8))
    plt.bar(months, df[column])

    plt.title(title)
    plt.xlabel('Months')
    plt.ylabel(f'{column}')
    plt.show()


def plot_line_chart(df: pd.DataFrame, column: str, title: str = '') -> None:
    """
    Plots a line chart for the specified column in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot the line chart for.

    Returns:
    None
    """
    months = [month[:3] for month in MONTHS]
    plt.figure(figsize=(20, 8))
    plt.plot(months, df[column], marker='o', linestyle='-', linewidth=2, markersize=5)

    plt.title(title)
    plt.xlabel('Months')
    plt.ylabel(f'{column}')
    plt.show()
