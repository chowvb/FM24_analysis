import pandas as pd
import utility_functions as uf
import stats_by_position_functions as spf
from data_visualisation_tools import scatter_plot_default 

# Using the utility function get_player_stats() to load player stats dataframe
season_stats_df = uf.get_player_stats()

# Use the utility function clean_player_positions() to change the player position string for easier analysis 
season_stats_updated_df = uf.clean_player_positions(season_stats_df)
def gk_analysis():
    # Analysing Goalkeeper performance 
    # Filter players to only show Goalkeepers
    gk_stats_df = season_stats_updated_df.loc[season_stats_updated_df["Best Pos"] == "GK"]

    # Reset the index numbers
    gk_stats_df = gk_stats_df.reset_index(drop = True)

    # Filter dataframe keys to those applicable to GKs (Full list can be found in stats_by_position_functions.py) and sort by minutes played
    gk_stats_general_df = gk_stats_df[spf.GK_stats].sort_values(by = "Mins", ascending= False).reset_index(drop = True)
    gk_stats_summary_df = gk_stats_general_df[["Name", "Apps", "Av Rat", "Clean Sheets", 
                                            "Con/90", "Pas %", "Ps C/90", "Sv %", "xSv %", 
                                            "Pens Saved Ratio"]]
    
    scatter_plot_default(gk_stats_summary_df, "Clean Sheets", "Apps")
    scatter_plot_default(gk_stats_summary_df, "Sv %", "xSv %")
    scatter_plot_default(gk_stats_summary_df, "Ps C/90", "Pas %")
    scatter_plot_default(gk_stats_summary_df, "Con/90", "Sv %")

gk_analysis()