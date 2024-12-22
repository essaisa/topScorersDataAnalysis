import pandas as pd

def load_data(filepath):
    # Try using 'ISO-8859-1' encoding to handle non-UTF-8 characters
    return pd.read_csv(filepath, encoding='ISO-8859-1')


# Add a new player to the data
def add_player(data, player_info):
    # Use pd.concat() to add a new row to the DataFrame
    data = pd.concat([data, pd.DataFrame([player_info])], ignore_index=True)
    return data

# Search for a player by name
def search_player(data, player_name):
    """Search for a player by name and return their record."""
    return data[data['Player'] == player_name]

# Sort players by a specific column (e.g., 'Goals')
def sort_players(data, by='Goals', ascending=False):
    """Sort players by a specific column (e.g., 'Goals')."""
    return data.sort_values(by=by, ascending=ascending)

def delete_player(data, player_name):
    """Delete a player from the dataset by their name."""
    return data[data['Player'] != player_name]


def best_goal_to_game_ratio(data):
    """Find the player with the best goal-to-game ratio."""
    
    # Check for any rows with 0 caps and handle the division by zero
    if (data['Caps'] == 0).any():
        print("Warning: Some players have 0 caps, which may cause division by zero.")
        data['Goals per Game'] = data['Goals'] / data['Caps'].replace(0, 1)  # Avoid division by zero
    else:
        data['Goals per Game'] = data['Goals'] / data['Caps']
    
    # Find the player with the highest goal-to-game ratio
    best_ratio = data.loc[data['Goals per Game'].idxmax()]
    return best_ratio

