# Import packages
import markdown

with open("README.md", "r") as f:
    tempMD = f.read()

tempHTML = markdown.markdown(tempMD)

with open("index.html", "w") as f:
    f.write(tempHTML)