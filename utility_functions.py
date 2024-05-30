import pandas as pd
from bs4 import BeautifulSoup
import os

# get_player_stats() returns the current squads attributes as a dataframe
def get_player_stats():
    # Open data file
    with open("data/squad_data/stats/player_stats_23-24.html") as file:
        # Parse HTML
        soup = BeautifulSoup(file, "html.parser")
    # Read soup as a dataframe
    df = pd.read_html(str(soup))
    # Filter for the first row (Containing dataframe)
    df = df[0]

    return df

# get_player_attributes() returns the current squads attributes as a dataframe
def get_player_attributes():
    # Open data file
    with open("data/squad_data/attributes/player_attributes_23-24.html") as file:
        # Parse HTML
        soup = BeautifulSoup(file, "html.parser")
    # Read soup as a dataframe
    df = pd.read_html(str(soup))
    # Filter for the first row (Containing dataframe)
    df = df[0]

    return df

def clean_player_positions(df):
    # store Positions List variable
    position_list = df["Best Pos"].tolist()

    # Loop through list using enumerate to amend position_list
    for i, position in enumerate(position_list):
        # Replace characters as a new position
        new_position = position.replace("(", "").replace(")", "").replace(" ", "")

        # Amend the old list with the new list
        position_list[i] = new_position
    
    # Replace "Best Pos" column with the updated position_list
    df["Best Pos"] = position_list
    
    # Return the updated dataframe
    return df