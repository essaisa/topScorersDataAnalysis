# tests/test_operations.py
import pytest
import pandas as pd
from src.data_operations import load_data, add_player, search_player, delete_player, best_goal_to_game_ratio

def test_load_data():
    filepath = '/Users/fo2/Documents/codes/top_scorers_analysis/data/top_scorers.csv'
    data = load_data(filepath)
    
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
    assert 'Player' in data.columns
    assert 'Goals' in data.columns

def test_add_player():
    data = pd.DataFrame(columns=['Player', 'Goals'])
    player_info = {'Player': 'Zlatan Ibrahimović', 'Goals': 62}
    data = add_player(data, player_info)
    
    assert data.shape[0] == 1
    assert data.iloc[0]['Player'] == 'Zlatan Ibrahimović'

def test_search_player():
    filepath = '/Users/fo2/Documents/codes/top_scorers_analysis/data/top_scorers.csv'
    data = load_data(filepath)
    
    # Assuming search_player returns a DataFrame and you want the first match
    player = search_player(data, 'Cristiano Ronaldo')
    
    # Ensure we have a valid player
    assert player is not None
    assert player.iloc[0]['Player'] == 'Cristiano Ronaldo'  # Access the first row's 'Player' column

def test_delete_player():
    filepath = '/Users/fo2/Documents/codes/top_scorers_analysis/data/top_scorers.csv'
    data = load_data(filepath)

    # Deleting a player and checking the result
    player_to_delete = 'Sunil Chhetri'
    data = delete_player(data, player_to_delete)
    assert player_to_delete not in data['Player'].values

def test_best_goal_to_game_ratio():
    filepath = '/Users/fo2/Documents/codes/top_scorers_analysis/data/top_scorers.csv'
    data = load_data(filepath)

    # Find player with the best goal-to-game ratio
    best_player = best_goal_to_game_ratio(data)
    assert best_player is not None
    assert 'Goals per Game' in best_player
    assert best_player['Goals per Game'] == max(data['Goals'] / data['Caps'])

