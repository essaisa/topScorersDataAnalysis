import sys
import os

# Add the absolute path of the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now try importing the modules
from data_operations import load_data, add_player, sort_players, search_player, delete_player, best_goal_to_game_ratio
from visualizations import plot_top_scorers


def main():
    # **Manually adjust this line** if needed, but this is the absolute path to your dataset.
    data_filepath = '/Users/fo2/Documents/codes/top_scorers_analysis/data/top_scorers.csv'  # (Absolute path)
    
    # Load the dataset using the absolute file path
    data = load_data(data_filepath)  # Ensure you use the absolute path here, or adjust relative path if needed

    # Perform operations
    # **Manually define the new player** information
    new_player = {
        'Player': 'Zlatan Ibrahimović',  # Add the player name here
        'Goals': 62,                     # Add the goals scored by the player
        'Caps': 122,                     # Add the number of matches played
        'Goals per match': 0.51,         # Goals per match, can adjust this value as needed
        'Career span': '2001-2023'       # Career span, adjust the years as needed
    }
    data = add_player(data, new_player)  # Adds the new player to the dataset

    # Search for a player (Example: Cristiano Ronaldo)
    player = search_player(data, 'Cristiano Ronaldo')
    print("Search Result for Cristiano Ronaldo:", player)  # This will print the search result

    # Sort players by goals
    sorted_data = sort_players(data, by='Goals', ascending=False)
    top_5_players = sorted_data.head(5)
    print(top_5_players.to_string())

     # Delete a player (Example: removing "Sunil Chhetri")
    data = delete_player(data, 'Sunil Chhetri')

    # Resort data after deletion 

    sorted_data = sort_players(data, by='Goals', ascending=False)
    print("Top 5 players after deleting Sunil Chhetri:")
    print(sorted_data.head(5).to_string()) 

    # Aggregation: Best goal-to-game ratio
    sorted_data = sort_players(data, by='Goals', ascending=False)

    # Select the top 50 players based on goals
    top_50_players = sorted_data.head(50)
    
    # Aggregation: Best goal-to-game ratio from top 50 players
    best_player = best_goal_to_game_ratio(top_50_players)
    print("Player with the best goal-to-game ratio from the top 50 players:")
    print(best_player)


    # Visualize the top 10 goal scorers
    plot_top_scorers(sorted_data, top_n=10)


if __name__ == "__main__":
    main()