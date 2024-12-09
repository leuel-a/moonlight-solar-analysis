import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


def plot_bar_chart(df: pd.DataFrame, column: str, title: str = '') -> None:
    """
    Plots a bar chart for the specified column in the given DataFrame.

    :param df: the dataframe to use as the data source
    :type df: pd.DataFrame

    :param column: the column to use as the data source
    :type column: str

    :param title: the title for the bar chart plot
    :type title: str

    :returns: Nothing
    :rtype: None
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

    :param df: the dataframe to be used as a data source
    :type df: pd.DataFrame

    :param column: the column from the dataframe
    :type column: str

    :param title: the title for the line chart plot
    :type title: str

    :returns: Nothing
    :rtype: None
    """
    months = [month[:3] for month in MONTHS]
    plt.figure(figsize=(20, 8))
    plt.plot(months, df[column], marker='o', linestyle='-', linewidth=2, markersize=5)

    plt.title(title)
    plt.xlabel('Months')
    plt.ylabel(f'{column}')

    plt.show()


def plot_heatmap(correlation_matrix: pd.DataFrame, title: str) -> None:
    """
    Plots a heatmap for the given correlation matrix.

    :param correlation_matrix: The correlation matrix to plot.
    :type correlation_matrix: pd.DataFrame

    :param title: The title for the heatmap
    :type title: str

    :returns: Nothing
    """
    if not isinstance(correlation_matrix, pd.DataFrame):
        raise ValueError('correlation_matrix must be a pandas.DataFrame')

    plt.figure(figsize=(20, 8))

    # here it uses seaborn to plot the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(title)

    plt.show()


def plot_histogram(df: pd.DataFrame, num_bins: int, col_name: str, title: str) -> None:
    """
    Plots a histogram for the specified DataFrame.

    :param  df: The DataFrame containing the data.
    :type df: pd.DataFrame

    :param num_bins: the number of bins to be plotted in the histogram
    :type num_bins: int

    :param col_name: the name of the column to draw the histogram
    :type col_name: str

    :param title: the title for the histogram
    :type title: str

    :returns: Nothing
    :rtype: None
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('df must be an instance of a pandas.DataFrame')

    max_value = df[col_name].max()
    min_value = df[col_name].min()

    bins = np.linspace(min_value, max_value, num_bins + 1)

    plt.figure(figsize=(20, 8))
    plt.hist(df[col_name], bins=num_bins, edgecolor='black')

    plt.xticks(bins)
    plt.show()
