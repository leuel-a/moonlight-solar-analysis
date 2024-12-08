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

def plot_heatmap(correlation_matrix: pd.DataFrame, title: str) -> None:
    """
    Plots a heatmap for the given correlation matrix.

    Parameters:
    correlation_matrix (pd.DataFrame): The correlation matrix to plot.

    Returns:
    None
    """
    if not isinstance(correlation_matrix, pd.DataFrame):
        raise ValueError('correlation_matrix must be a pandas.DataFrame')

    plt.figure(figsize=(20, 8))

    # here it uses seaborn to plot the heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(title)

    plt.show()
