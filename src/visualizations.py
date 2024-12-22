import matplotlib.pyplot as plt
import seaborn as sns

# Plot the top N goal scorers
def plot_top_scorers(data, top_n=10):
    """Plot the top N goal scorers."""
    top_players = data.nlargest(top_n, 'Goals')
    sns.barplot(x='Goals', y='Player', data=top_players, palette='viridis')
    plt.title(f'Top {top_n} Goal Scorers')
    plt.xlabel('Goals')
    plt.ylabel('Player')
    plt.show()
