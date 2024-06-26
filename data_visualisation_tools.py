import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import math 
import mplcursors
import mpld3
from mpld3 import plugins

"""
Args - 
    df - Dataframe 
    col1_name - Name of dataframe column you want for x axis (Must be a string)
    col2_name - Name of dataframe column you want for y axis (Must be a string)
"""
def scatter_plot_default(df, col1_name, col2_name, interactive = False):
    # Define plot style
    with plt.style.context("classic"):
        
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
        points = ax.scatter(df[col1_name], df[col2_name])

        # Set the x/y axis label names to the name of the columns
        plt.xlabel(col1_name)
        plt.ylabel(col2_name)

        if interactive == True:
            # Add an interactive cursor to show players when mouse is hovered over data point (on python image viewer)
            mplcursors.cursor(hover = True).connect("add", lambda sel: sel.annotation.set_text(df["Name"].tolist()[sel.index]))


            # Add interactive tooltips using mpld3
            labels = df["Name"].tolist()
            tooltip = plugins.PointLabelTooltip(points, labels=labels)
            plugins.connect(fig, tooltip)
            # Save html code to a variable to print and copy and paste into html file later
            text = mpld3.fig_to_html(fig, figid = "fig1")
    
            # Print html code
            print(text)
        else:
            # Iterate through the names to label each of the data points
            for i, name in enumerate(df["Name"].tolist()):
                ax.annotate(name, (df[col1_name][i], df[col2_name][i]),
                            ha = "left", va = "center")
        

    # Show the plot
    plt.show()
    #mpld3.show()

    
