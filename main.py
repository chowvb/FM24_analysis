# Import packages
import pandas as pd
from bs4 import BeautifulSoup

# Open data file 
with open("Untitled.html") as file:
    # Parse html
    soup = BeautifulSoup(file, "html.parser")

# read html as a dataframe
df = pd.read_html(str(soup))

# filter for first row (Containing dataframe)
df = df[0]