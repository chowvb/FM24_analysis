import pandas as pd
import numpy as np
from utility_functions import get_player_attributes, role_and_duty_dict, attribute_weightings
from itables import init_notebook_mode
init_notebook_mode(all_interactive=True)

data = get_player_attributes()

position_coefficient_df = data[["Name", "Age", "Best Pos"]]

rd_df = pd.DataFrame(role_and_duty_dict)

def avg_attributes(df, key_attributes, secondary_attributes):
        key_df = df[key_attributes]
        avg_attributes = (key_df.sum(axis=1) / len(key_attributes)) *2

        second_df = df[secondary_attributes]
        secondary_avg = (second_df.sum(axis=1) / len(secondary_attributes)) 

        role_score = (avg_attributes + secondary_avg) / 2
        role_score = round(role_score, 2)

        return role_score

"""
***Note***
I Spent at the most part 5 hours developing a attributes weight for different positions. All for it to ruin my coefficient.
I'm Leaving the weighting code there in case I want to tinker with it in the future
"""


attribute_weightings_df = pd.DataFrame.from_dict(attribute_weightings)
augmented_attributes_df = pd.DataFrame()
for i, player in enumerate(data["Name"]):
    print(player)
    player_data = data.loc[data["Name"] == player]
    position = player_data.iloc[0]["Best Pos"]
    print(position)
    weightings_df = attribute_weightings_df[["Attribute",position]]
    weightings_df = weightings_df.set_index("Attribute").T
    #weightings_df = ((weightings_df/100))
    weightings_df["Name"] = player
    df = pd.concat([player_data, weightings_df]).reset_index(drop=True)
    df = df.groupby("Name", as_index=False).sum()[df.columns]
    augmented_attributes_df = pd.concat([augmented_attributes_df, df], ignore_index= True)
#augmented_attributes_df = augmented_attributes_df.groupby("Name", as_index=False).sum()[augmented_attributes_df.columns]



for i, role in enumerate(rd_df):
    #print(role)
    role_df = rd_df[role]
    others = ["Name", "Age", "Best Pos"]
    key_attributes = role_df["key_attributes"]
    secondary_attributes = role_df["secondary_attributes"]
    filtered_df = augmented_attributes_df[others + key_attributes + secondary_attributes]
    #filtered_df = data[others + key_attributes + secondary_attributes]
    position_coefficient_df[f"{role}"] = avg_attributes(filtered_df, key_attributes=key_attributes, secondary_attributes=secondary_attributes)




