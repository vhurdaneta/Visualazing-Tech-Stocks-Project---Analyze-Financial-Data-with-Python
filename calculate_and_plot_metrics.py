import numpy as np
import matplotlib.pyplot as plt

def plot_metrics(stock_data_daily_returns, metric='mean'):
    """
    Calculate and plot the specified metric for the given stock data daily returns.

    Args:
    stock_data_daily_returns (pd.DataFrame): A dataframe with stock symbols as columns and daily returns as rows.
    metric (str): The metric to calculate and plot. Options: 'mean', 'var', or 'std'. Default: 'mean'.

    Returns:
    None
    """

    def calculate_metrics(metric):
        """
        Calculate the specified metric for the given stock data daily returns.

        Args:
        metric (str): The metric to calculate. Options: 'mean', 'var', or 'std'.

        Returns:
        pd.Series: A pandas Series with the calculated metric for each stock symbol.
        """
        if metric == 'mean':
            result = stock_data_daily_returns.mean()
        elif metric == 'var':
            result = stock_data_daily_returns.var()
        elif metric == 'std':
            result = stock_data_daily_returns.std()
        else:
            raise ValueError("Invalid metric. Choose 'mean', 'var', or 'std'.")
        return result

    # Calculate the specified metric for the stock data
    metrics = calculate_metrics(metric)

    # Print the calculated metric
    print(f'{metric.capitalize()} of return:\n', metrics)

    # Get the metric values for each stock symbol
    height = [metrics[key] for key in metrics.keys()]

    # Get the positions for each stock symbol on the x-axis
    x_pos = np.arange(len(metrics.keys()))

    # Plot the metric values as a bar chart
    plt.bar(x_pos, height)
    plt.xticks(x_pos, stock_data_daily_returns.columns)

    # Set the x-axis and y-axis labels and the chart title
    plt.xlabel("Tech_Stocks")
    plt.ylabel(metric)
    plt.title(f"daily {metric}")

    # Display the chart
    plt.show()

