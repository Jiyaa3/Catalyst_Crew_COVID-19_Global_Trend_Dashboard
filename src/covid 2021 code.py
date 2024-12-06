import matplotlib.pyplot as plt
import numpy as np

# Dataset
countries = [
    "United States", "India", "Brazil", "United Kingdom", "South Africa",
    "Germany", "Canada", "Australia", "Russia", "China",
    "Japan", "France", "Italy", "Spain", "Mexico"
]
covid_cases = [
    35000000, 25000000, 14000000, 7000000, 3000000,
    5000000, 1500000, 800000, 6000000, 10000000,
    5000000, 7000000, 6000000, 5000000, 4000000
]
vaccinated_individuals = [
    200000000, 900000000, 120000000, 50000000, 25000000,
    60000000, 30000000, 15000000, 80000000, 1100000000,
    70000000, 50000000, 45000000, 40000000, 35000000
]

# Creating a grouped bar chart
x = np.arange(len(countries))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(14, 8))
bars1 = ax.bar(x - width/2, covid_cases, width, label='COVID-19 Cases', color='skyblue')
bars2 = ax.bar(x + width/2, vaccinated_individuals, width, label='Vaccinated Individuals', color='lightgreen')

# Adding titles and labels
ax.set_title("COVID-19 Cases and Vaccinated Individuals by Country", fontsize=16)
ax.set_xlabel("Country", fontsize=12)
ax.set_ylabel("Number of People", fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha='right', fontsize=10)
ax.legend()

# Adding data labels to bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f'{height:,}',  # Format numbers with commas
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom', fontsize=8
        )

add_labels(bars1)
add_labels(bars2)

plt.tight_layout()

# Display the graph
plt.show()
