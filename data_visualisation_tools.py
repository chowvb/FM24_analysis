import pandas 
import matplotlib.pyplot as plt
import math 
"""
Args - 
    df - Dataframe 
    col1_name - Name of dataframe column you want for x axis (Must be a string)
    col2_name - Name of dataframe column you want for y axis (Must be a string)
"""
def scatter_plot_default(df, col1_name, col2_name):
    # Define plot style
    with plt.style.context("dark_background"):
        
        # Create subplots
        fig, ax = plt.subplots()

        # Get upper and lower limits for x axis (rounded to the next/previous 10)
        xlim_max = math.ceil(df[col1_name].max()/10) * 10
        xlim_min = math.floor(df[col1_name].min()/10) * 10

        # Get upper and lower limits for y axis (rounded to the next/previous 10)
        ylim_max = math.ceil(df[col2_name].max() /10) * 10
        ylim_min = math.floor(df[col2_name].min()/10) * 10

        # Set the plot axis limits from the limits calculated
        plt.xlim(xmin = xlim_min, xmax = xlim_max)
        plt.ylim(ymin = ylim_min, ymax = ylim_max)

        # Set the gridlines with a low alpha 
        plt.grid(which = "major", alpha = 0.2)

        # Plot the scatter points
        ax.scatter(df[col1_name], df[col2_name])

        # Iterate through the names to label each of the data points
        for i, name in enumerate(df["Name"].tolist()):
            ax.annotate(name, (df[col1_name][i], df[col2_name][i]),
                        ha = "left", va = "center_baseline")
        
        # Set the x/y axis label names to the name of the columns
        plt.xlabel(col1_name)
        plt.ylabel(col2_name)
    
    # Show the plot
    plt.show()
