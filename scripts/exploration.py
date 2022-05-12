import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Exploration:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_histogram(self, column: str, color: str) -> None:
        plt.figure(figsize=(8, 5))
        sns.displot(data=self.df, x=column, kde=True, color=color, height=7, aspect=3)
        plt.title(f"Distribution of {column}", size=20, fontweight="bold")
        plt.xlim(0, self.df[column].max())
        plt.show()

    def plot_jointScatter(self, x_value: str, y_value: str, color: str, ax) -> None:
        sns.scatterplot(
            data=self.df, x=x_value, y=y_value, color=color, ax=ax, x_bins=100
        )
        plt.xlabel(f"{x_value}")
