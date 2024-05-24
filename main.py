import pandas as pd
from bs4 import BeautifulSoup

with open("Untitled.html") as file:
    soup = BeautifulSoup(file, "html.parser")
df = pd.read_html(str(soup))
df = df[0]