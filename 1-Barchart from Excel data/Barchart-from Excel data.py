import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("data.xlsx")

# Extract the "Name" and "Height" columns
names = df["Name"]
heights = df["Height"]

# Create a bar chart using matplotlib
plt.bar(names, heights)

# Set the chart title and axis labels
plt.title("Height by Name")
plt.xlabel("Name")
plt.ylabel("Height")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90)

# Show the chart
plt.show()
