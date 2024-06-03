import pandas as pd
import utility_functions as uf
import stats_by_position_functions as spf
from data_visualisation_tools import scatter_plot_default 
from IPython.display import display
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
    
    scatter_plot_default(gk_stats_summary_df, "xSv %", "Sv %", interactive=True)
    return gk_stats_summary_df

def defence_analysis():
    # Analysing defenders performance
    d_stats_df = season_stats_updated_df.loc[season_stats_updated_df["Best Pos"].isin(["DC", "DR", "DL", "WBR", "WBL"])]
    other_players = season_stats_updated_df.loc[season_stats_updated_df["Name"] == "Trent Alexander-Arnold"]
    d_stats_df = pd.concat([d_stats_df, other_players])
    d_stats_df = d_stats_df.reset_index(drop= True)

    d_stats_general = d_stats_df[spf.DC_stats].sort_values(by = "Mins", ascending = False).reset_index(drop= True)
    for variable in spf.DC_stats:
        try:
            df = d_stats_df[["Name", "Apps", variable]].sort_values(by = variable, ascending= False)
            df = df.loc[df["Name"].isin(["Trent Alexander-Arnold", "Conor Bradley", "Joe Gomez"])]
            display(df)
        except:
            pass
    
    scatter_plot_default(d_stats_df, "Tck A", "Tck R", interactive= True)

def midfield_analysis():
    # Analysing midfields performance
    m_stats_df = season_stats_updated_df.loc[season_stats_updated_df["Best Pos"].isin(["DM", "MC", "AMC"])]
    m_stats_df = m_stats_df.reset_index(drop= True)

    m_stats_general = m_stats_df[spf.CM_stats].sort_values(by = "Mins", ascending = False).reset_index(drop= True)
    for variable in spf.CM_stats:
        try:
            df = m_stats_df[["Name", "Apps", variable]].sort_values(by = variable, ascending= False)
            display(df)
        except:
            pass
    
    scatter_plot_default(m_stats_df, "Ps C/90", "Pas %", interactive= True)

def forward_analysis():
    # Analysing Forwards performance
    f_stats_df = season_stats_updated_df.loc[season_stats_updated_df["Best Pos"].isin(["AML", "AMR", "STC"])]
    f_stats_df = f_stats_df.reset_index(drop = True)
    
    for variable in spf.ST_stats:
        try:
            df = f_stats_df[["Name", "Best Pos", "Apps", variable]].sort_values(by = variable, ascending = False)
            display(df)
        except:
            pass
    
    scatter_plot_default(f_stats_df, "Gls", "xG", interactive= True)