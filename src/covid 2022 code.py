import matplotlib.pyplot as plt
import numpy as np

# Dataset
countries = [
    "United States", "India", "Brazil", "United Kingdom", "South Africa",
    "Germany", "Canada", "Australia", "Russia", "China",
    "Japan", "France", "Italy", "Spain", "Mexico"
]
covid_cases = [
    50000000, 43000000, 22000000, 11000000, 6000000,
    8000000, 2500000, 1200000, 10000000, 12000000,
    8000000, 9000000, 7000000, 6000000, 5000000
]
vaccinated_individuals = [
    260000000, 1100000000, 180000000, 70000000, 40000000,
    85000000, 45000000, 20000000, 100000000, 1200000000,
    95000000, 75000000, 65000000, 55000000, 50000000
]

# Creating a grouped bar chart
x = np.arange(len(countries))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(16, 8))
bars1 = ax.bar(x - width/2, covid_cases, width, label='COVID-19 Cases', color='skyblue')
bars2 = ax.bar(x + width/2, vaccinated_individuals, width, label='Vaccinated Individuals', color='lightgreen')

# Adding titles and labels
ax.set_title("COVID-19 Cases and Vaccinated Individuals by Country", fontsize=18)
ax.set_xlabel("Country", fontsize=14)
ax.set_ylabel("Number of People", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha='right', fontsize=12)
ax.legend(fontsize=12)

# Adding data labels to bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{height:,}',  # Format numbers with commas
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # Offset text by 3 points vertically
            textcoords="offset points",
            ha='center', va='bottom', fontsize=10
        )

add_labels(bars1)
add_labels(bars2)

plt.tight_layout()

# Display the graph
plt.show()
