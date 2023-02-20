import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_a = pd.read_csv("metingen/frequency_a.csv", delimiter=";")
df_b = pd.read_csv("metingen/frequency_b.csv", delimiter=";")
df_c = pd.read_csv("metingen/frequency_c.csv", delimiter=";")


def generate(df):
    df_matrix = df.pivot("x", "y", "nagalmtijd")

    # Plot the heatmap with origin in the left corner
    sns.heatmap(df_matrix, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={"label": "My Colorbar Label"},
            xticklabels=[str(i) for i in range(0, df_matrix.shape[1])],
            yticklabels=[str(i) for i in range(df_matrix.shape[0]-1, -1, -1)],
            vmin=0)

    plt.title('Nagalmtijd per positie in seconden')
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.show()


generate(df_a)
