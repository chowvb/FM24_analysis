# This script will review the players in the current squad whos contracts are due to expire at the end of the current and next season.
import pandas as pd
from bs4 import BeautifulSoup

# Read squad attributes html file
with open("data/squad_data/attributes/player_attributes_23-24.html") as file:
    # Parse html
    soup = BeautifulSoup(file, "html.parser")
# Read html file as a dataframe
squad_attributes = pd.read_html(str(soup))
# Filter df for the first row (Containing dataframe)
squad_attributes = squad_attributes[0]

# Read squad season stats html file 
with open("data/squad_data/stats/player_stats_23-24.html") as file:
    # Parse html
    soup = BeautifulSoup(file, "html.parser")
# Read html file as a dataframe
squad_stats = pd.read_html(str(soup))
# Filter df for the first row (Containing Dataframe)
squad_stats = squad_stats[0]


# Extracting players who's contracts are expiring.
# Change the Contract Expiry date to only show the year of expiry
squad_attributes["Expires"] = squad_attributes["Expires"].str[5:]

# Get the most recent expiry year 
expiry_year = squad_attributes["Expires"].iloc[0]

# Filter dataframe for players whos contracts are expiring soon 
expiring_players_df = squad_attributes.loc[squad_attributes["Expires"] == expiry_year]

# Extract the player names 
expiring_players = expiring_players_df["Name"].tolist()

# Using the extracted players names who's contracts are soon to be expiring, filter the season stats for those players
expiring_players_season_stats = squad_stats.loc[squad_stats["Name"].isin(expiring_players)]

# Create a list of column names to filter for the most important stats in deciding to renew contracts
filter_list = ["Name", "Best Pos", "Age", "Wage", "Transfer Value", "Apps", "Starts", "Mins", "Mins/Gm", "Won", "D", "Lost", "Gwin", "Av Rat", "Dist/90"]

expiring_players_season_stats = expiring_players_season_stats[filter_list]

position_list = squad_stats["Best Pos"].tolist()

for i, position in enumerate(position_list):
    new_position = position.replace("(", "").replace(")", "").replace(" ", "")
    position_list[i] = new_position

squad_stats["Best Pos"] = position_list