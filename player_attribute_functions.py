# Import Modules
import pandas as pd
import numpy as np
from utility_functions import get_player_attributes, role_and_duty_dict, attribute_weightings
from itables import init_notebook_mode

# Call init_notebook_mode so displayed dataframes are interactive.  
init_notebook_mode(all_interactive=True)

# Import 
data = get_player_attributes()

# Create a base dataframe containing player names, age and their best position
position_coefficient_df = data[["Name", "Age", "Best Pos"]]

# Create a dataframe from the role and duty dictionary pre-defined in the utility_functions, Note: This is a nested dictionary.
rd_df = pd.DataFrame(role_and_duty_dict)


# Define a function to create an average of attributes for roles based on the role's key attributes and secondary attributes for the specific role.
def avg_attributes(df, key_attributes, secondary_attributes):
        
        # Filter the inputted dataframe for only the key attributes needed
        key_df = df[key_attributes]

        # Calculate an average of the key attributes and apply a x2 multiplier to the average to highlight the importance
        avg_attributes = (key_df.sum(axis=1) / len(key_attributes)) *2

        # Filter the inputted dataframe for only the secondary attributes needed
        second_df = df[secondary_attributes]

        # Calculate the average for the secondary attributes, no multiplier is applied here.
        secondary_avg = (second_df.sum(axis=1) / len(secondary_attributes)) 

        # Combine the two scores and divide by 2 to get an average
        role_score = (avg_attributes + secondary_avg) / 2

        # Round the combined store to 2 decimal places 
        role_score = round(role_score, 2)

        # Return the role scores.
        return role_score

"""
***Note***
I Spent at the most part 5 hours developing a attributes weight for different positions. All for it to ruin my coefficient.
I'm Leaving the weighting code there in case I want to tinker with it in the future

12/06/2024 - Fixed the code so it now works. 
"""
# Store the attribute weightings defined in the utility_funcitons
attribute_weightings_df = pd.DataFrame.from_dict(attribute_weightings)

# Create an empty dataframe for the new augmented player attributes.
augmented_attributes_df = pd.DataFrame()

# Enumerate through the data df
for i, player in enumerate(data["Name"]):

    # Print the player name (Purely for debugging to see where code breaks or returns an error)
    #print(player)
    
    # Extract the specific enumerated player from their name and store in a new dataframe
    player_data = data.loc[data["Name"] == player]

    # Extract the players best position and store in a variable
    position = player_data.iloc[0]["Best Pos"]

    # Print player position (Purely for debugging for if the code returns an error)
    #print(position)
    
    # Create weightings_df which will store the extracted players position into a new dataframe
    weightings_df = attribute_weightings_df[["Attribute",position]]

    # Transpose the dataframe
    weightings_df = weightings_df.set_index("Attribute").T

    # Add the selected players name into the datadframe, this will make it easier to join/add the values together
    weightings_df["Name"] = player

    # Concat the extracted player attributes and the position_multiplier values into one new dataframe 
    df = pd.concat([player_data, weightings_df]).reset_index(drop=True)

    # Groupby players with the same name (Will only be one player in the dataframe but two rows of values). Sum together all the atrributes via the columns.
    df = df.groupby("Name", as_index=False).sum()[df.columns]

    # Concat together the newly joined data with the pre-existing augmented_attributes_df defined at the top, as the loop progresses, the full dataframe will automatically populate with all the players in the squad.
    augmented_attributes_df = pd.concat([augmented_attributes_df, df], ignore_index= True)



# Loop through all the role_duties dataframe to create a position coefficient.
for i, role in enumerate(rd_df):
    # Print the role (Purely for debugging to see where the code returns an error in the loop)
    #print(role)

    # For the role eg., Ball_Playing_Center_Back_Defend filter through the first layer of the nested dataframe.
    role_df = rd_df[role]

    # Store dataframe columns that we will want later on
    others = ["Name", "Age", "Best Pos"]

    # Extract the key attributes for the desired role/duty and store in a list.
    key_attributes = role_df["key_attributes"]

    # Extract the secondary attributes for the desired role/duty and store in a list.
    secondary_attributes = role_df["secondary_attributes"]

    # Filter the augmented_attributes_df for only the player name, age, best position and the attributes we want to analyse for the desired role.
    filtered_df = augmented_attributes_df[others + key_attributes + secondary_attributes]

    # Call upon the avg_attributes function defined above and store the position scores in a new column named after the role, enumerated in rd_df
    position_coefficient_df[f"{role}"] = avg_attributes(filtered_df, key_attributes=key_attributes, secondary_attributes=secondary_attributes)




