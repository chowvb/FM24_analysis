import pandas as pd
from bs4 import BeautifulSoup

# get_player_stats() returns the current squads attributes as a dataframe
def get_player_stats():
    # Open data file
    with open("data/squad_data/stats/player_stats_23-24.html", "r", encoding = "utf-8") as file:
        # Parse HTML
        soup = BeautifulSoup(file, "html.parser")
    # Read soup as a dataframe
    df = pd.read_html(str(soup))
    # Filter for the first row (Containing dataframe)
    df = df[0]

    keys_to_change = ["Clean Sheets","Con/90", "Cr C/A", "Gwin", "Hdr %", "Pas %", "Pen/R", 
                      "Pens Saved Ratio", "Shot %", "Sv %", "Tck" ,"Tck R",
                      "xSv %"]
    # Cleaning player data for analysis and data visualisation 
    def percent_clean(stats_df, list):
        for i, key in enumerate(list):
            key_values = stats_df[key].tolist()
            for i, percent in enumerate(key_values):
                change = percent.replace("%", "").replace("-", "0")
                key_values[i] = change
            stats_df[key] = key_values
            stats_df[key] = pd.to_numeric(stats_df[key])
        return stats_df
    
    new_df = percent_clean(df, keys_to_change)

    def standardise_appearance(stats_df):
        apps_list = stats_df["Apps"].tolist()
        for i, apps in enumerate(apps_list):
            change = apps.replace("(", " ").replace(")", "")
            try:
                starts, subs = change.split(" ", 1)
                appearances = int(starts) + int(subs)
            except:
                appearances = int(change)
            
            apps_list[i] = appearances
        return apps_list
    
    new_df["Apps"] = standardise_appearance(df)

    keys = new_df.columns.tolist()
    for key in keys:
        try:
            new_df[key] = pd.to_numeric(new_df[key])
        except:
            pass
    return new_df

    

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