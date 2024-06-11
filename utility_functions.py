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
    
    new_df = clean_player_positions(df)

    return new_df

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


role_and_duty_dict = {

    # Attributes for Goalkeeper Roles
    "GK_D" : {
        "key_attributes" : ["Aer", "Cmd", "Com", "Han", "Kic", "Ref", "Cnt", "Pos", "Agi"],
        "secondary_attributes" : ["1v1", "Thr", "Ant", "Dec"]
    },
    "SK_D" : {
        "key_attributes" : ["Cmd", "Kic", "1v1", "Ref", "Ant", "Cnt", "Pos", "Agi"],
        "secondary_attributes" : ["Aer", "Com", "Fir", "Han", "Pas", "TRO", "Thr", "Cmp", "Dec", "Vis", "Acc"]
    },
    "SK_S" : {
        "key_attributes" : ["Cmd", "Kic", "1v1", "Ref", "TRO", "Ant", "Cmp", "Cnt", "Pos", "Agi"],
        "secondary_attributes" : ["Aer", "Com", "Fir", "Han", "Pas", "Thr", "Dec", "Vis", "Acc"]
    },
    "SK_A" : {
        "key_attributes" : ["Cmd", "Kic", "1v1", "Ref", "TRO", "Ant", "Cmp", "Cnt", "Pos", "Agi"],
        "secondary_attributes" : ["Aer", "Com","Ecc", "Fir", "Han", "Pas", "Thr", "Dec", "Vis", "Acc"]
    },

    # Attributes for Central Defender Roles
    "CD_D" :{
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Pac"]
    },
    "NCB_D" :{
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Agg", "Ant", "Bra", "Cnt", "Pac"]
    },
    "BPD_D" :{
        "key_attributes" : ["Hea", "Mar","Pas", "Tck","Cmp", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Fir", "Tec", "Agg", "Ant", "Bra", "Cnt", "Dec", "Vis", "Pac"]
    },
    "BPD_S" :{
        "key_attributes" : ["Hea", "Pas", "Tck", "Agg", "Bra", "Cmp", "Dec", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Fir", "Mar", "Tec", "Ant", "Cnt", "Vis"]
    },
    "BPD_C" :{
        "key_attributes" : ["Mar", "Pas", "Tck", "Ant", "Cmp", 'Cnt', 'Dec', 'Pos', "Pac"],
        "secondary_attributes" : ['Fir', "Hea", "Tec", "Bra", "Vis", "Jum", "Str"]
    },
    "L_D" : {
        "key_attributes" : ["Fir", "Hea", "Mar", "Pas", "Tck", "Tec", "Cmp", "Dec", "Pos", "Tea", "Jum", "Str"],
        "secondary_attributes" : ["Ant", "Bra", "Cnt", "Pac", "Sta"]
    },
    "L_S" : {
        "key_attributes" : ["Fir", "Hea", "Mar", "Pas", "Tck", "Tec", "Cmp", "Dec", "Pos", "Tea", "Jum", "Str"],
        "secondary_attributes" : ["Ant", "Bra", "Cnt", "Pac", "Sta", "Vis", "Dri"]
    },
    "WCB_D" : {
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Dri", "Fir", "Pas", "Tec", "Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Wor", "Agi", "Pac"]
    },
    "WCB_S" : {
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Jum", "Str"],
        "secondary_attributes" : ["Dri", "Fir", "Pas", "Tec", "Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Wor", "Agi", "Pac", "Cro", "OtB", "Sta"]
    },
    "WCB_A" : {
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Jum", "Str", "Cro", "OtB", "Sta"],
        "secondary_attributes" : ["Dri", "Fir", "Pas", "Tec", "Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Wor", "Agi", "Pac"]
    },

    # Attributes for Fullbacks and Wingbacks
    "FB_D" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Cnt", "Pos"],
        "secondary_attributes" : ["Cro", "Pas", "Dec", "Tea", "Wor", "Pac", "Sta"]
    },
    "FB_S" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Cnt", "Pos"],
        "secondary_attributes" : ["Cro", "Pas", "Dec", "Tea", "Wor", "Pac", "Sta", "Dri", "Tec"]
    },
    "FB_A" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Cnt", "Pos", "Cro"],
        "secondary_attributes" : ["Fir", "Pas", "Dec", "Tea", "Wor", "Pac", "Sta", "Dri", "Tec", "OtB", "Agi"]
    },
    "IFB_D" : {
        "key_attributes" : ["Hea", "Mar", "Tck", "Pos", "Str"],
        "secondary_attributes" : ["Dri", "Fir", "Pas", "Tec", "Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Wor", "Agi", "Jum", "Pac"]
    },
    "NFB_D" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Pos", "Str"],
        "secondary_attributes" : ["Hea", "Agg", "Bra", "Cnt", "Tea"]
    },
    "WB_D" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Pos", "Tea", "Wor", "Acc", "Sta"],
        "secondary_attributes" : ["Cro", "Dri", "Fir", "Pas", "Tec", "Cnt", "Dec", "OtB", "Agi", "Bal", "Pac"]
    },
    "WB_S" : {
        "key_attributes" : ["Cro", "Dri", "Mar", "Tck", "OtB", "Tea", "Wor", "Acc", "Sta"],
        "secondary_attributes" : ["Fir", "Pas", "Tec", "Cnt", "Dec", "Pos", "Agi", "Bal", "Pac", "Ant"]
    },
    "WB_A" : {
        "key_attributes" : ["Cro", "Dri", "Tec", "Tck", "OtB", "Tea", "Wor", "Acc", "Sta", "Pac"],
        "secondary_attributes" : ["Fir", "Pas", "Mar", "Cnt", "Dec", "Pos", "Agi", "Bal", "Fla", "Ant"]
    },
    "CWB_S" : {
        "key_attributes" : ["Cro", "Dri", "Tec", "OtB", "Tea", "Wor", "Acc", "Sta"],
        "secondary_attributes" : ["Fir", "Mar", "Pas", "Tck", "Ant", "Dec", "Fla", "Pos", "Agi", "Bal", "Pac"]
    },
    "CWB_A" : {
        "key_attributes" : ["Cro", "Dri", "Tec", "OtB", "Tea", "Wor", "Acc", "Sta", "Fla"],
        "secondary_attributes" : ["Fir", "Mar", "Pas", "Tck", "Ant", "Dec", "Pos", "Agi", "Bal", "Pac"]
    },
    "IWB_D" : {
        "key_attributes" : ["Pas", "Tck", "Ant", "Dec", "Pos", "Tea"],
        "secondary_attributes" : ["Fir", "Mar", "Tec", "Cmp", "Cnt", "OtB", "Wor", "Acc", "Agi", "Sta"]
    },
    "IWB_S" : {
        "key_attributes" : ["Fir", "Pas", "Tck", "Cmp", "Dec", "Tea"],
        "secondary_attributes" : ["Mar", "Tec", "Ant", "Cnt", "OtB", "Pos", "Vis", "Wor", "Acc", "Agi", "Sta"]
    },
    "IWB_A" : {
        "key_attributes" : ["Fir", "Pas", "Tck", "Tec", "Cmp", "Dec", "OtB", "Tea", "Vis", "Acc"],
        "secondary_attributes" : ["Cro", "Dri", "Lon", "Mar", "Ant", "Cnt", "Fla", "Pos", "Wor", "Agi", "Pac", "Sta"]
    },

    # Attributes for Central Defensive Midfield roles
    "A_D" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Cnt", "Dec", "Pos"],
        "secondary_attributes" : ["Cmp", "Tea", "Str"]
    },
    "HB_D" : {
        "key_attributes" : ["Mar", "Tck", "Ant", "Cmp", "Cnt", "Dec", "Pos", "Tea"],
        "secondary_attributes" : ["Fir", "Pas", "Agg", "Bra", "Wor", "Jum", "Sta", "Str"]
    },
    "DM_D" : {
        "key_attributes" : ["Tck", "Ant", "Cnt", "Pos", "Tea"],
        "secondary_attributes" : ["Mar", "Pas", "Agg", "Cmp", "Dec", "Wor", "Sta", "Str"]
    },
    "DM_S" : {
        "key_attributes" : ["Tck", "Ant", "Cnt", "Pos", "Tea"],
        "secondary_attributes" : ["Mar", "Pas", "Agg", "Cmp", "Dec", "Wor", "Sta", "Str", "Fir"]
    },
    "RGA_S" : {
        "key_attributes": ["Fir", "Pas", "Tec", "Cmp", "Dec", "Fla", "OtB", "Tea", "Vis"],
        "secondary_attributes" : ["Dri", "Lon", "Ant", "Bal"]
    },
    "VOL_S" : {
        "key_attributes" : ["Mar", "Pas", "Tck", "OtB", "Pos", "Wor", "Pac", "Sta"],
        "secondary_attributes" : ["Fin", "Fir", "Lon", "Ant", "Cmp", "Cnt", "Dec", "Acc", "Bal", "Str"]
    },
    "VOL_A" : {
        "key_attributes" : ["Mar", "Pas", "Tck", "OtB", "Pos", "Wor", "Pac", "Sta", "Fin", "Lon", "Ant"],
        "secondary_attributes" : ["Fir", "Cmp", "Cnt", "Dec", "Acc", "Bal", "Str"]
    },

    # Overlapping roles for both Central Defensive and Central Midfielder 
    "DLP_D" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "Tea", "Vis"],
        "secondary_attributes" : ["Tck", "Ant", "Pos", "Bal"]
    },
    "DLP_S" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "Tea", "Vis"],
        "secondary_attributes" : ["OtB", "Ant", "Pos", "Bal"]
    },
    "RPM_S" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Ant", "Cmp", "Dec", "OtB", "Tea", "Vis", "Wor", "Acc", "Sta"],
        "secondary_attributes" : ["Dri", "Lon", "Cnt", "Pos", "Agi", "Bal", "Pac"]
    },
    "BWM_D" : {
        "key_attributes" : ["Tck", "Agg", "Ant", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Mar", "Bra", "Cnt", "Pos", "Agi", "Pac", "Str"]
    },
    "BWM_S" : {
        "key_attributes" : ["Tck", "Agg", "Ant", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Mar", "Pas", "Bra", "Cnt", "Agi", "Pac", "Str"]
    },

    # Central Midfield Roles
    "BBM_S" : {
        "key_attributes" : ["Pas", "Tck", "OtB", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Dri", "Fin", "Fir", "Lon", "Tec", "Agg", "Ant", "Cmp", "Dec", "Pos", "Acc", "Bal", "Pac", "Str"]
    },
    "CAR_S" : {
        "key_attributes" : ["Fir", "Pas", "Tck", "Dec", "Pos", "Tea", "Sta"],
        "secondary_attributes" : ["Tec", "Ant", "Cmp", "Cnt", "OtB", "Vis", "Wor"]
    },
    "MEZ_S" : {
        "key_attributes" : ["Pas", "Tec", "Dec", "OtB", "Wor", "Acc"],
        "secondary_attributes" : ["Dri", "Fir", "Lon", "Tck", "Ant", "Cmp", "Vis", "Bal", "Sta"]
    },
    "MEZ_A" : {
        "key_attributes" : ["Dri", "Pas", "Tec", "Dec", "OtB", "Vis", "Wor", "Acc"],
        "secondary_attributes" : ["Fin", "Fir", "Lon", "Ant", "Cmp", "Fla", "Bal", "Sta"]
    },
    "CM_D" : {
        "key_attributes" : ["Tck", "Cnt", "Dec", "Pos", "Tea"],
        "secondary_attributes" : ["Fir", "Mar", "Pas", "Tec", "Agg", "Ant", "Cmp", "Wor", "Sta"]
    },
    "CM_S" : {
        "key_attributes" : ["Fir", "Pas", "Tck", "Dec", "Tea"],
        "secondary_attributes" : ["Tec", "Ant", "Cmp", "Cnt", "OtB", "Vis", "Wor", "Sta"]
    },
    "CM_A" : {
        "key_attributes" : ["Fir", "Pas", "Dec", "OtB"],
        "secondary_attributes" : ["Lon", "Tck", "Tec", "Ant", "Cmp", "Tea", "Vis", "Wor", "Acc", "Sta"]
    },

    # Overlapping roles for Central and Central Attacking Midfield roles
    "AP_S" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Tea", "Vis"],
        "secondary_attributes" : ["Dri", "Ant", "Fla", "Agi"]
    },
    "AP_A" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Tea", "Vis"],
        "secondary_attributes" : ["Dri", "Ant", "Fla", "Acc", "Agi"]
    },

    # Central Attacking Midfield Roles
    "AM_S" : {
        "key_attributes" : ["Fir", "Lon", "Pas", "Tec", "Ant", "Dec", "Fla", "OtB"],
        "secondary_attributes" : ["Dri", "Cmp", "Vis", "Agi"]
    },
    "AM_A" : {
        "key_attributes" : ["Dri", "Fir", "Lon", "Pas", "Tec", "Ant", "Dec", "Fla", "OtB"],
        "secondary_attributes" : ["Fin", "Cmp", "Vis", "Agi"]
    },
    "EG_A" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "Vis"],
        "secondary_attributes" : ["Dri", "Ant", "Fla", "OtB", "Tea", "Agi"]
    },
    "SS_A" : {
        "key_attributes" : ["Dri", "Fin", "Fir", "Ant", "Cmp", "OtB", "Acc"],
        "secondary_attributes" : ["Pas", "Tec", "Cnt", "Dec", "Wor", "Agi", "Bal", "Pac", "Sta"]
    },
    
    # Wide Midfield Roles
    "DW_D" : {
        "key_attributes" : ["Tec", "Ant", "OtB", "Pos", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Cro", "Dri", "Fir", "Mar", "Tck", "Agg", "Cnt", "Dec", "Acc"]
    },
    "DW_S" : {
        "key_attributes" : ["Cro", "Tec", "OtB", "Wor", "Sta"],
        "secondary_attributes" : ["Dri", "Fir", "Mar", "Pas", "Tck", "Agg", "Ant", "Cmp", "Cnt", "Dec", "Pos", "Acc"]
    },
    "WM_D" : {
        "key_attributes" : ["Pas", "Tck", "Cnt", "Dec", "Pos", "Tea", "Wor"],
        "secondary_attributes" : ["Cro", "Fir", "Mar", "Tec", "Ant", "Cmp", "Sta"]
    },
    "WM_S" : {
        "key_attributes" : ["Pas", "Tck", "Dec", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Cro", "Fir", "Tec", "Ant", "Cmp", "Cnt", "OtB", "Pos", "Vis"]
    },
    "WM_A" : {
        "key_attributes" : ["Cro", "Fir", "Pas", "Dec", "Tea", "Wor", "Sta"],
        "secondary_attributes" : ["Tck", "Tec", "Ant", "Cmp", "OtB", "Vis"]
    },
    "WP_A" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "Tea", "Vis"],
        "secondary_attributes" : ["Dri", "OtB", "Agi"]
    },
    "WP_A" : {
        "key_attributes" : ["Dri", "Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Tea", "Vis"],
        "secondary_attributes" : ["Ant", "Fla", "Acc", "Agi"]
    },

    # Overlapping Roles for Wide Midfielder and Wide Forwards
    "W_S" : {
        "key_attributes" : ["Cro", "Dri", "Tec", "Acc", "Agi"],
        "secondary_attributes" : ["Fir", "Pas", "OtB", "Wor", "Bal", "Pac", "Sta"]
    },
    "W_A" : {
        "key_attributes" : ["Cro", "Dri", "Tec", "Acc", "Agi"],
        "secondary_attributes" : ["Fir", "Pas", "Ant", "Fla", "OtB", "Wor", "Bal", "Pac", "Sta"]
    },
    "IW_S" : {
        "key_attributes" : ["Cro", "Dri", "Pas", "Tec", "Acc", "Agi"],
        "secondary_attributes" : ["Fir", "Lon", "Cmp", "Dec", "OtB", "Vis", "Wor", "Bal", "Pac", "Sta"]
    },
    "IW_A" : {
        "key_attributes" : ["Cro", "Dri", "Pas", "Tec", "Acc", "Agi"],
        "secondary_attributes" : ["Fir", "Lon", "Cmp", "Dec", "OtB", "Vis", "Wor", "Bal", "Pac", "Sta", "Ant", "Fla"]
    },

    # Roles for wide forwards
    "IF_S" : {
        "key_attributes" : ["Dri", "Fin", "Fir", "Tec", "OtB", "Acc", "Agi"],
        "secondary_attributes" : ["Lon", "Pas", "Ant", "Cmp", "Fla", "Vis", "Wor", "Bal", "Pac", "Sta"]
    },
    "IF_A" : {
        "key_attributes" : ["Dri", "Fin", "Fir", "Tec", "Ant", "OtB", "Acc", "Agi"],
        "secondary_attributes" : ["Lon", "Pas", "Cmp", "Fla", "Wor", "Bal", "Pac", "Sta"]
    },
    "RMD_A" : {
        "key_attributes" : ["Fin", "Ant", "Cmp", "Cnt", "Dec", "OtB", "Bal"],
        "secondary_attributes" : ["Fir", "Tec", "Wor", "Acc", "Sta"]
    },
    "WT_S" : {
        "key_attributes" : ["Hea", "Bra", "Tea", "Jum", "Str"],
        "secondary_attributes" : ["Cro", "Fir", "Ant", "OtB", "Wor", "Bal", "Sta"]
    },
    "WT_A" : {
        "key_attributes" : ["Hea", "Bra", "OtB", "Jum", "Str"],
        "secondary_attributes" : ["Cro", "Fin", "Fir", "Ant", "Tea", "Wor", "Bal", "Sta"]
    },

    # Overlapping roles for Attacking Midfield/Wide Forwards/Strikers
    "T_A" : {
        "key_attributes" : ["Dri", "Fir", "Pas", "Tec", "Cmp", "Dec", "Fla", "OtB", "Vis", "Acc"],
        "secondary_attributes" : ["Fin", "Ant", "Agi", "Bal"]
    },

    # Roles for Strikers
    "AF_A" : {
        "key_attributes" : ["Dri", "Fin", "Fir", "Tec", "Cmp", "OtB", "Acc"],
        "secondary_attributes" : ["Pas", "Ant", "Dec", "Wor", "Agi", "Bal", "Pac", "Sta"]
    },
    "CF_S" : {
        "key_attributes" : ["Dri", "Fir", "Hea", "Lon", "Tec", "Ant", "Cmp", "Dec", "OtB", "Vis", "Acc", "Agi", "Str"],
        "secondary_attributes" : ["Fin", "Tea", "Wor", "Bal", "Jum", "Pac", "Sta"]
    },
    "CF_A" : {
        "key_attributes" : ["Dri", "Fin", "Fir", "Hea", "Tec", "Ant", "Cmp", "OtB", "Acc", "Agi", "Str"],
        "secondary_attributes" : ["Lon", "Pas", "Dec", "Tea", "Vis", "Wor", "Bal", "Jum", "Pac", "Sta"]
    },
    "DLF_S" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Tea"],
        "secondary_attributes" : ["Fin", "Ant", "Fla", "Vis", "Bal", "Str"]
    },
    "DLF_A" : {
        "key_attributes" : ["Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Tea"],
        "secondary_attributes" : ["Dri", "Fin", "Ant", "Fla", "Vis", "Bal", "Str"]
    },
    "F9_S" : {
        "key_attributes" : ["Dri", "Fir", "Pas", "Tec", "Cmp", "Dec", "OtB", "Vis", "Acc", "Agi"],
        "secondary_attributes" : ["Fin", "Ant", "Fla", "Tea", "Bal"]
    },
    "P_A" : {
        "key_attributes" : ["Fin", "Ant", "Cmp", "OtB"],
        "secondary_attributes" : ["Fir", "Hea", "Tec", "Dec", "Acc"]
    },
    "TF_S" : {
        "key_attributes" : ["Hea", "Bra", "Tea", "Bal", "Jum", "Str"],
        "secondary_attributes" : ["Fin", "Fir", "Agg", "Ant", "Cmp", "Dec", "OtB"]
    },
    "TF_A" : {
        "key_attributes" : ["Fin", "Hea", "Bra", "Cmp", "OtB", "Bal", "Jum", "Str"],
        "secondary_attributes" : ["Fir", "Agg", "Ant", "Dec", "Tea"]
    },
    "PF_D" : {
        "key_attributes" : ["Agg", "Ant", "Bra", "Dec", "Tea", "Wor", "Acc", "Pac", "Sta"],
        "secondary_attributes" : ["Fir", "Cmp", "Cnt", "Agi", "Bal", "Str"]
    },
    "PD_S" : {
        "key_attributes" : ["Agg", "Ant", "Bra", "Dec", "Tea", "Wor", "Acc", "Pac", "Sta"],
        "secondary_attributes" : ["Fir", "Pas", "Cmp", "Cnt", "OtB", "Agi", "Bal", "Str"]
    },
    "PF_A" : {
        "key_attributes" : ["Agg", "Ant", "Bra", "OtB", "Tea", "Wor", "Acc", "Pac", "Sta"],
        "secondary_attributes" : ["Fin", "Fir", "Cmp", "Cnt", "Dec", "Agi", "Bal", "Str"]
    }
}

attribute_weightings = {
    "Attribute" : ["Cor", "Cro", "Dri", "Fin", "Fir", "Fre", "Hea", "Lon", "L Th", "Mar", "Pas", "Pen", "Tck", "Tec", "Agg", "Ant", "Bra", "Cmp", "Cnt", "Dec", "Det", "Fla", "Ldr", "OtB", "Pos", "Tea", "Vis", "Wor", "Acc", "Agi", "Bal", "Jum", "Nat", "Pac", "Sta", "Str", "Aer", "Cmd", "Com", "Ecc", "Han", "Kic", "1v1", "Pun", "Ref", "TRO", "Thr"],
    "GK" : [0,0,0,0,1,0,1,0,0,0,3,0,0,1,0,3,6,2,6,10,0,0,2,0,5,2,1,1,6,8,2,1,0,3,1,4,6,6,5,0,8,5,4,0,8,0,3],
    "DR" : [1,2,1,1,3,1,2,1,1,3,2,1,4,2,0,3,2,2,4,7,0,0,1,1,4,2,2,2,7,6,2,2,0,5,6,4,0,0,0,0,0,0,0,0,0,0,0],
    "DL" : [1,2,1,1,3,1,2,1,1,3,2,1,4,2,0,3,2,2,4,7,0,0,1,1,4,2,2,2,7,6,2,2,0,5,6,4,0,0,0,0,0,0,0,0,0,0,0],
    "DC" : [1,1,1,1,2,1,5,1,1,8,2,1,5,1,0,5,2,2,4,10,0,0,2,1,8,1,1,2,6,6,2,6,0,5,3,6,0,0,0,0,0,0,0,0,0,0,0],
    "WBR": [1,3,2,1,3,1,1,1,1,2,3,1,3,3,0,3,1,2,3,5,0,0,1,2,3,2,2,2,8,5,2,1,0,6,7,4,0,0,0,0,0,0,0,0,0,0,0],
    "WBL": [1,3,2,1,3,1,1,1,1,2,3,1,3,3,0,3,1,2,3,5,0,0,1,2,3,2,2,2,8,5,2,1,0,6,7,4,0,0,0,0,0,0,0,0,0,0,0],
    "DM" : [1,1,2,2,4,1,1,3,1,3,4,1,7,3,0,5,1,2,3,8,0,0,1,1,5,2,4,4,6,6,2,1,0,4,4,5,0,0,0,0,0,0,0,0,0,0,0],
    "MR" : [1,5,3,2,4,1,1,2,1,1,3,1,2,4,0,3,1,3,2,5,0,0,1,2,1,2,3,3,8,6,2,1,0,6,5,3,0,0,0,0,0,0,0,0,0,0,0],
    "ML" : [1,5,3,2,4,1,1,2,1,1,3,1,2,4,0,3,1,3,2,5,0,0,1,2,1,2,3,3,8,6,2,1,0,6,5,3,0,0,0,0,0,0,0,0,0,0,0],    
    "MC" : [1,1,2,2,6,1,1,3,1,3,6,1,3,4,0,3,1,3,2,7,0,0,1,3,3,2,6,3,6,6,2,1,0,6,5,4,0,0,0,0,0,0,0,0,0,0,0],
    "AMR": [1,5,5,2,5,1,1,2,1,1,2,1,2,4,0,3,1,3,2,5,0,0,1,2,1,2,3,3,10,6,2,1,0,10,7,3,0,0,0,0,0,0,0,0,0,0,0],
    "AML": [1,5,5,2,5,1,1,2,1,1,2,1,2,4,0,3,1,3,2,5,0,0,1,2,1,2,3,3,10,6,2,1,0,10,7,3,0,0,0,0,0,0,0,0,0,0,0],
    "AMC": [1,1,3,3,5,1,1,3,1,1,4,1,2,5,0,3,1,3,2,6,0,0,1,3,2,2,6,3,9,6,2,1,0,7,6,3,0,0,0,0,0,0,0,0,0,0,0],
    "STC" : [1,2,5,8,6,1,6,2,1,1,2,1,1,4,0,6,1,6,2,5,0,0,1,6,2,1,2,2,10,6,2,5,0,7,6,6,0,0,0,0,0,0,0,0,0,0,0]
}